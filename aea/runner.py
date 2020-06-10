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
"""This module contains the implementation of AEA multiple instances runner."""

from asyncio.events import AbstractEventLoop
from typing import Awaitable, Dict, Sequence, Type, cast

from aea.aea import AEA
from aea.helpers.multiple_executor import (
    AbstractExecutorTask,
    AbstractMultipleExecutor,
    AbstractMultipleRunner,
    AsyncExecutor,
    ThreadExecutor,
)
from aea.runtime import AsyncRuntime


class AEAInstanceTask(AbstractExecutorTask):
    """Task to run agent instance."""

    def __init__(self, agent: AEA):
        """
        Init aea instance task.

        :param agent: AEA instance to run within task.
        """
        self._agent = agent
        super().__init__()

    def start(self):
        """Start task."""
        self._agent.start()

    def stop(self):
        """Stop task."""
        self._agent.stop()

    def create_async_task(self, loop: AbstractEventLoop) -> Awaitable:
        """Return asyncio Task for task run in asyncio loop."""
        self._agent._runtime.set_loop(loop)
        if not hasattr(self._agent._runtime, "_run_runtime"):
            raise ValueError(
                "Agent runtime is not async compatible. Please use runtime_mode=async"
            )
        return loop.create_task(cast(AsyncRuntime, self._agent._runtime)._run_runtime())

    @property
    def id(self):
        """Return agent name."""
        self._agent.name


class AEARunner(AbstractMultipleRunner):
    """Run multiple AEA instances."""

    SUPPORTED_MODES: Dict[str, Type[AbstractMultipleExecutor]] = {
        "threaded": ThreadExecutor,
        "async": AsyncExecutor,
    }

    def __init__(self, agents: Sequence[AEA], mode: str) -> None:
        """
        Init AEARunner.

        :param agents: sequence of AEA instances to run.
        :param mode: executor name to use.
        """
        self._agents = agents
        super().__init__(mode)

    def _make_tasks(self) -> Sequence[AbstractExecutorTask]:
        """Make tasks to run with executor."""
        return [AEAInstanceTask(agent) for agent in self._agents]
