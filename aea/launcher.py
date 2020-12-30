# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""This module contains the implementation of multiple AEA configs launcher."""
import logging
import multiprocessing
from asyncio.events import AbstractEventLoop
from concurrent.futures.process import BrokenProcessPool
from multiprocessing.synchronize import Event
from os import PathLike
from threading import Thread
from typing import Any, Callable, Dict, Optional, Sequence, Tuple, Type, Union

from aea.aea import AEA
from aea.aea_builder import AEABuilder
from aea.exceptions import AEAException
from aea.helpers.base import cd
from aea.helpers.multiple_executor import (
    AbstractExecutorTask,
    AbstractMultipleExecutor,
    AbstractMultipleRunner,
    AbstractMultiprocessExecutorTask,
    AsyncExecutor,
    ExecutorExceptionPolicies,
    ProcessExecutor,
    TaskAwaitable,
    ThreadExecutor,
)
from aea.runtime import AsyncRuntime


_default_logger = logging.getLogger(__name__)


def load_agent(agent_dir: Union[PathLike, str]) -> AEA:
    """
    Load AEA from directory.

    :param agent_dir: agent configuration directory

    :return: AEA instance
    """
    with cd(agent_dir):
        return AEABuilder.from_aea_project(".", verify_or_create_keys=False).build()


def _set_logger(
    log_level: Optional[str],
):  # pragma: nocover # used in spawned process and pytest does not see this code
    from aea.cli.utils.loggers import (  # pylint: disable=import-outside-toplevel
        default_logging_config,
    )

    logger_ = logging.getLogger("aea")
    logger_ = default_logging_config(logger_)
    if log_level is not None:
        level = logging.getLevelName(log_level)
        logger_.setLevel(level)


def _run_agent(
    agent_dir: Union[PathLike, str], stop_event: Event, log_level: Optional[str] = None
) -> None:
    """
    Load and run agent in a dedicated process.

    :param agent_dir: agent configuration directory
    :param stop_event: multithreading Event to stop agent run.
    :param log_level: debug level applied for AEA in subprocess

    :return: None
    """
    import asyncio  # pylint: disable=import-outside-toplevel
    import select  # pylint: disable=import-outside-toplevel
    import selectors  # pylint: disable=import-outside-toplevel

    if hasattr(select, "kqueue"):  # pragma: nocover  # cause platform specific
        selector = selectors.SelectSelector()
        loop = asyncio.SelectorEventLoop(selector)  # type: ignore
        asyncio.set_event_loop(loop)

    _set_logger(log_level=log_level)

    agent = load_agent(agent_dir)

    def stop_event_thread():
        try:
            stop_event.wait()
        except (KeyboardInterrupt, EOFError, BrokenPipeError) as e:  # pragma: nocover
            _default_logger.error(
                f"Exception raised in stop_event_thread {e} {type(e)}. Skip it, looks process is closed."
            )
        finally:
            _default_logger.debug("_run_agent: stop event raised. call agent.stop")
            agent.runtime.stop()

    Thread(target=stop_event_thread, daemon=True).start()
    try:
        agent.start()
    except KeyboardInterrupt:  # pragma: nocover
        _default_logger.debug("_run_agent: keyboard interrupt")
    except BaseException as e:  # pragma: nocover
        _default_logger.exception("exception in _run_agent")
        exc = AEAException(f"Raised {type(e)}({e})")
        exc.__traceback__ = e.__traceback__
        raise exc
    finally:
        _default_logger.debug("_run_agent: call agent.stop")
        agent.stop()


class AEADirTask(AbstractExecutorTask):
    """Task to run agent from agent configuration directory."""

    def __init__(self, agent_dir: Union[PathLike, str]) -> None:
        """
        Init aea config dir task.

        :param agent_dir: direcory with aea config.
        """
        self._agent_dir = agent_dir
        self._agent: AEA = load_agent(self._agent_dir)
        super().__init__()

    def start(self) -> None:
        """Start task."""
        self._agent.start()

    def stop(self):
        """Stop task."""
        if not self._agent:  # pragma: nocover
            raise ValueError("Task was not started!")
        self._agent.stop()

    def create_async_task(self, loop: AbstractEventLoop) -> TaskAwaitable:
        """Return asyncio Task for task run in asyncio loop."""
        self._agent.runtime.set_loop(loop)
        if not isinstance(self._agent.runtime, AsyncRuntime):  # pragma: nocover
            raise ValueError(
                "Agent runtime is not async compatible. Please use runtime_mode=async"
            )
        return loop.create_task(self._agent.runtime.start_and_wait_completed())

    @property
    def id(self) -> Union[PathLike, str]:
        """Return agent_dir."""
        return self._agent_dir


class AEADirMultiprocessTask(AbstractMultiprocessExecutorTask):
    """
    Task to run agent from agent configuration directory.

    Version for multiprocess executor mode.
    """

    def __init__(
        self, agent_dir: Union[PathLike, str], log_level: Optional[str] = None
    ):
        """
        Init aea config dir task.

        :param agent_dir: direcory with aea config.
        :param log_level: debug level applied for AEA in subprocess
        """
        self._agent_dir = agent_dir
        self._manager = multiprocessing.Manager()
        self._stop_event = self._manager.Event()
        self._log_level = log_level
        super().__init__()

    def start(self) -> Tuple[Callable, Sequence[Any]]:
        """Return function and arguments to call within subprocess."""
        return (_run_agent, (self._agent_dir, self._stop_event, self._log_level))

    def stop(self):
        """Stop task."""
        if self._future.done():
            _default_logger.debug("Stop called, but task is already done.")
            return
        try:
            self._stop_event.set()
        except (FileNotFoundError, BrokenPipeError, EOFError) as e:  # pragma: nocover
            _default_logger.error(
                f"Exception raised in task.stop {e} {type(e)}. Skip it, looks process is closed."
            )

    @property
    def id(self) -> Union[PathLike, str]:
        """Return agent_dir."""
        return self._agent_dir

    @property
    def failed(self) -> bool:
        """
        Return was exception failed or not.

        If it's running it's not failed.

        :rerurn: bool
        """
        if not self._future:
            return False

        if (
            self._future.done()
            and self._future.exception()
            and isinstance(self._future.exception(), BrokenProcessPool)
        ):  # pragma: nocover
            return False

        return super().failed


class AEALauncher(AbstractMultipleRunner):
    """Run multiple AEA instances."""

    SUPPORTED_MODES: Dict[str, Type[AbstractMultipleExecutor]] = {
        "threaded": ThreadExecutor,
        "async": AsyncExecutor,
        "multiprocess": ProcessExecutor,
    }

    def __init__(
        self,
        agent_dirs: Sequence[Union[PathLike, str]],
        mode: str,
        fail_policy: ExecutorExceptionPolicies = ExecutorExceptionPolicies.propagate,
        log_level: Optional[str] = None,
    ) -> None:
        """
        Init AEARunner.

        :param agent_dirs: sequence of AEA config directories.
        :param mode: executor name to use.
        :param fail_policy: one of ExecutorExceptionPolicies to be used with Executor
        :param log_level: debug level applied for AEA in subprocesses
        """
        self._agent_dirs = agent_dirs
        self._log_level = log_level
        super().__init__(mode=mode, fail_policy=fail_policy)

    def _make_tasks(self) -> Sequence[AbstractExecutorTask]:
        """Make tasks to run with executor."""
        if self._mode == "multiprocess":
            return [
                AEADirMultiprocessTask(agent_dir, log_level=self._log_level)
                for agent_dir in self._agent_dirs
            ]
        return [AEADirTask(agent_dir) for agent_dir in self._agent_dirs]
