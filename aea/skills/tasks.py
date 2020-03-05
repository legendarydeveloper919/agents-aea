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

"""This module contains the classes for tasks."""
import logging
import signal
import threading
from abc import abstractmethod
from multiprocessing.pool import AsyncResult, Pool
from typing import Any, Callable, Dict, Optional, Sequence, cast

logger = logging.getLogger(__name__)


class Task:
    """This class implements an abstract task."""

    def __init__(self, **kwargs):
        """Initialize a task."""
        self._is_executed = False
        # this is where we store the result.
        self._result = None
        self.config = kwargs

    def __call__(self, *args, **kwargs):
        """
        Execute the task.

        :param args: positional arguments forwarded to the 'execute' method.
        :param kwargs: keyword arguments forwarded to the 'execute' method.
        :return the task instance
        :raises ValueError: if the task has already been executed.
        """
        if self._is_executed:
            raise ValueError("Task already executed.")

        self.setup()
        try:
            self._result = self.execute(*args, **kwargs)
            return self
        except Exception as e:
            logger.debug(
                "Got exception of type {} with message '{}' while executing task.".format(
                    type(e), str(e)
                )
            )
        finally:
            self._is_executed = True
            self.teardown()

    @property
    def is_executed(self) -> bool:
        """Check if the task has already been executed."""
        return self._is_executed

    @property
    def result(self) -> Any:
        """
        Get the result.

        :return the result from the execute method.
        :raises ValueError: if the task has not been executed yet.
        """
        if not self._is_executed:
            raise ValueError("Task not executed yet.")
        return self._result

    @abstractmethod
    def setup(self) -> None:
        """
        Implement the behaviour setup.

        :return: None
        """

    @abstractmethod
    def execute(self, *args, **kwargs) -> None:
        """
        Run the task logic.

        :return: None
        """

    @abstractmethod
    def teardown(self) -> None:
        """
        Implement the behaviour teardown.

        :return: None
        """


def init_worker():
    """
    Initialize a worker.

    Disable the SIGINT handler.
    Related to a well-known bug: https://bugs.python.org/issue8296
    """
    signal.signal(signal.SIGINT, signal.SIG_IGN)


class TaskManager:
    """A Task manager."""

    def __init__(self, nb_workers: int = 5):
        """
        Initialize the task manager.

        :param nb_workers: the number of worker processes.
        """
        self._nb_workers = nb_workers
        self._pool = None  # type: Optional[Pool]
        self._stopped = True
        self._lock = threading.Lock()

        self._task_enqueued_counter = 0
        self._results_by_task_id = {}  # type: Dict[int, Any]

    @property
    def nb_workers(self) -> int:
        """Get the number of workers."""
        return self._nb_workers

    def enqueue_task(
        self, func: Callable, args: Sequence = (), kwds: Optional[Dict[str, Any]] = None
    ) -> int:
        """
        Enqueue a task with the executor.

        :param func: the callable instance to be enqueued
        :param args: the positional arguments to be passed to the function.
        :param kwds: the keyword arguments to be passed to the function.
        :return the task id to get the the result.
        :raises ValueError: if the task manager is not running.
        """
        with self._lock:
            if self._stopped:
                raise ValueError("Task manager not running.")
            self._pool = cast(Pool, self._pool)
            task_id = self._task_enqueued_counter
            self._task_enqueued_counter += 1
            async_result = self._pool.apply_async(
                func, args=args, kwds=kwds if kwds is not None else {}
            )
            self._results_by_task_id[task_id] = async_result
            return task_id

    def get_task_result(self, task_id: int) -> AsyncResult:
        """Get the result from a task."""
        task_result = self._results_by_task_id.get(
            task_id, None
        )  # type: Optional[AsyncResult]
        if task_result is None:
            raise ValueError("Task id {} not present.".format(task_id))

        return task_result

    def start(self) -> None:
        """Start the task manager."""
        with self._lock:
            if self._stopped is False:
                logger.debug("Task manager already running.")
            else:
                logger.debug("Start the task manager.")
                self._stopped = False
                self._pool = Pool(self._nb_workers, initializer=init_worker)

    def stop(self) -> None:
        """Stop the task manager."""
        with self._lock:
            if self._stopped is True:
                logger.debug("Task manager already stopped.")
            else:
                logger.debug("Stop the task manager.")
                self._stopped = True
                self._pool = cast(Pool, self._pool)
                self._pool.terminate()
                self._pool.join()
                self._pool = None
