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
"""This module contains the decision maker class."""
import hashlib
import logging
import threading
import uuid
from abc import ABC, abstractmethod
from queue import Queue
from threading import Thread
from types import SimpleNamespace
from typing import List, Optional

from aea.crypto.wallet import Wallet
from aea.decision_maker.messages.base import InternalMessage
from aea.decision_maker.messages.state_update import StateUpdateMessage
from aea.decision_maker.messages.transaction import TransactionMessage
from aea.helpers.async_friendly_queue import AsyncFriendlyQueue
from aea.identity.base import Identity

logger = logging.getLogger(__name__)


def _hash(access_code: str) -> str:
    """
    Get the hash of the access code.

    :param access_code: the access code
    :return: the hash
    """
    result = hashlib.sha224(access_code.encode("utf-8")).hexdigest()
    return result


class OwnershipState(ABC):
    """Represent the ownership state of an agent."""

    @abstractmethod
    def set(self, **kwargs) -> None:
        """
        Set values on the ownership state.

        :param kwargs: the relevant keyword arguments
        :return: None
        """

    @abstractmethod
    def apply_delta(self, **kwargs) -> None:
        """
        Apply a state update to the ownership state.

        This method is used to apply a raw state update without a transaction.

        :param kwargs: the relevant keyword arguments
        :return: None
        """

    @property
    @abstractmethod
    def is_initialized(self) -> bool:
        """Get the initialization status."""

    @abstractmethod
    def is_affordable_transaction(self, tx_message: TransactionMessage) -> bool:
        """
        Check if the transaction is affordable (and consistent).

        :param tx_message: the transaction message
        :return: True if the transaction is legal wrt the current state, false otherwise.
        """

    @abstractmethod
    def apply_transactions(
        self, transactions: List[TransactionMessage]
    ) -> "OwnershipState":
        """
        Apply a list of transactions to (a copy of) the current state.

        :param transactions: the sequence of transaction messages.
        :return: the final state.
        """

    @abstractmethod
    def __copy__(self) -> "OwnershipState":
        """Copy the object."""


class LedgerStateProxy(ABC):
    """Class to represent a proxy to a ledger state."""

    @property
    @abstractmethod
    def is_initialized(self) -> bool:
        """Get the initialization status."""

    @abstractmethod
    def is_affordable_transaction(self, tx_message: TransactionMessage) -> bool:
        """
        Check if the transaction is affordable on the default ledger.

        :param tx_message: the transaction message
        :return: whether the transaction is affordable on the ledger
        """


class Preferences(ABC):
    """Class to represent the preferences."""

    @abstractmethod
    def set(self, **kwargs,) -> None:
        """
        Set values on the preferences.

        :param kwargs: the relevant key word arguments
        """

    @property
    @abstractmethod
    def is_initialized(self) -> bool:
        """
        Get the initialization status.

        Returns True if exchange_params_by_currency_id and utility_params_by_good_id are not None.
        """

    @abstractmethod
    def marginal_utility(self, ownership_state: OwnershipState, **kwargs,) -> float:
        """
        Compute the marginal utility.

        :param ownership_state: the ownership state against which to compute the marginal utility.
        :param kwargs: optional keyword argyments
        :return: the marginal utility score
        """

    @abstractmethod
    def utility_diff_from_transaction(
        self, ownership_state: OwnershipState, tx_message: TransactionMessage
    ) -> float:
        """
        Simulate a transaction and get the resulting utility difference (taking into account the fee).

        :param ownership_state: the ownership state against which to apply the transaction.
        :param tx_message: a transaction message.
        :return: the score.
        """

    @abstractmethod
    def __copy__(self) -> "Preferences":
        """Copy the object."""


class ProtectedQueue(Queue):
    """A wrapper of a queue to protect which object can read from it."""

    def __init__(self, access_code: str):
        """
        Initialize the protected queue.

        :param access_code: the access code to read from the queue
        """
        super().__init__()
        self._access_code_hash = _hash(access_code)

    def put(
        self, internal_message: Optional[InternalMessage], block=True, timeout=None
    ) -> None:
        """
        Put an internal message on the queue.

        If optional args block is true and timeout is None (the default),
        block if necessary until a free slot is available. If timeout is
        a positive number, it blocks at most timeout seconds and raises
        the Full exception if no free slot was available within that time.
        Otherwise (block is false), put an item on the queue if a free slot
        is immediately available, else raise the Full exception (timeout is
        ignored in that case).

        :param internal_message: the internal message to put on the queue
        :raises: ValueError, if the item is not an internal message
        :return: None
        """
        if not (
            type(internal_message)
            in {InternalMessage, TransactionMessage, StateUpdateMessage}
            or internal_message is None
        ):
            raise ValueError("Only internal messages are allowed!")
        super().put(internal_message, block=True, timeout=None)

    def put_nowait(self, internal_message: Optional[InternalMessage]) -> None:
        """
        Put an internal message on the queue.

        Equivalent to put(item, False).

        :param internal_message: the internal message to put on the queue
        :raises: ValueError, if the item is not an internal message
        :return: None
        """
        if not (
            type(internal_message)
            in {InternalMessage, TransactionMessage, StateUpdateMessage}
            or internal_message is None
        ):
            raise ValueError("Only internal messages are allowed!")
        super().put_nowait(internal_message)

    def get(self, block=True, timeout=None) -> None:
        """
        Inaccessible get method.

        :raises: ValueError, access not permitted.
        :return: None
        """
        raise ValueError("Access not permitted!")

    def get_nowait(self) -> None:
        """
        Inaccessible get_nowait method.

        :raises: ValueError, access not permitted.
        :return: None
        """
        raise ValueError("Access not permitted!")

    def protected_get(
        self, access_code: str, block=True, timeout=None
    ) -> Optional[InternalMessage]:
        """
        Access protected get method.

        :param access_code: the access code
        :param block: If optional args block is true and timeout is None (the default), block if necessary until an item is available.
        :param timeout: If timeout is a positive number, it blocks at most timeout seconds and raises the Empty exception if no item was available within that time.
        :raises: ValueError, if caller is not permitted
        :return: internal message
        """
        if not self._access_code_hash == _hash(access_code):
            raise ValueError("Wrong code, access not permitted!")
        internal_message = super().get(
            block=block, timeout=timeout
        )  # type: Optional[InternalMessage]
        return internal_message


class DecisionMakerHandler(ABC):
    """This class implements the decision maker."""

    def __init__(self, identity: Identity, wallet: Wallet, **kwargs):
        """
        Initialize the decision maker handler.

        :param identity: the identity
        :param wallet: the wallet
        :param kwargs: the key word arguments
        """
        self._identity = identity
        self._wallet = wallet
        self._context = SimpleNamespace(**kwargs)
        self._message_out_queue = AsyncFriendlyQueue()  # type: AsyncFriendlyQueue

    @property
    def agent_name(self) -> str:
        return self.identity.name

    @property
    def identity(self) -> Identity:
        """The identity of the agent."""
        return self._identity

    @property
    def wallet(self) -> Wallet:
        """The wallet of the agent."""
        return self._wallet

    @property
    def context(self) -> SimpleNamespace:
        """Get the context."""
        return self._context

    @property
    def message_out_queue(self) -> AsyncFriendlyQueue:
        """Get (out) queue."""
        return self._message_out_queue

    @abstractmethod
    def handle(self, message: InternalMessage) -> None:
        """
        Handle an internal message from the skills.

        :param message: the internal message
        :return: None
        """


class DecisionMaker:
    """This class implements the decision maker."""

    def __init__(
        self, decision_maker_handler: DecisionMakerHandler,
    ):
        """
        Initialize the decision maker.

        :param agent_name: the agent name
        :param decision_maker_handler: the decision maker handler
        """
        self._agent_name = decision_maker_handler.identity.name
        self._queue_access_code = uuid.uuid4().hex
        self._message_in_queue = ProtectedQueue(
            self._queue_access_code
        )  # type: ProtectedQueue
        self._decision_maker_handler = decision_maker_handler
        self._thread = None  # type: Optional[Thread]
        self._lock = threading.Lock()
        self._message_out_queue = decision_maker_handler.message_out_queue
        self._stopped = True

    @property
    def message_in_queue(self) -> ProtectedQueue:
        """Get (in) queue."""
        return self._message_in_queue

    @property
    def message_out_queue(self) -> AsyncFriendlyQueue:
        """Get (out) queue."""
        return self._message_out_queue

    @property
    def decision_maker_handler(self) -> DecisionMakerHandler:
        """Get the decision maker handler."""
        return self._decision_maker_handler

    def start(self) -> None:
        """Start the decision maker."""
        with self._lock:
            if not self._stopped:  # pragma: no cover
                logger.debug(
                    "[{}]: Decision maker already started.".format(self._agent_name)
                )
                return

            self._stopped = False
            self._thread = Thread(target=self.execute)
            self._thread.start()

    def stop(self) -> None:
        """Stop the decision maker."""
        with self._lock:
            self._stopped = True
            self.message_in_queue.put(None)
            if self._thread is not None:
                self._thread.join()
            logger.debug("[{}]: Decision Maker stopped.".format(self._agent_name))
            self._thread = None

    def execute(self) -> None:
        """
        Execute the decision maker.

        Performs the following while not stopped:

        - gets internal messages from the in queue and calls handle() on them

        :return: None
        """
        while not self._stopped:
            message = self.message_in_queue.protected_get(
                self._queue_access_code, block=True
            )  # type: Optional[InternalMessage]

            if message is None:
                logger.debug(
                    "[{}]: Received empty message. Quitting the processing loop...".format(
                        self._agent_name
                    )
                )
                continue

            if message.protocol_id == InternalMessage.protocol_id:
                self.handle(message)
            else:
                logger.warning(
                    "[{}]: Message received by the decision maker is not of protocol_id=internal.".format(
                        self._agent_name
                    )
                )

    def handle(self, message: InternalMessage) -> None:
        """
        Handle an internal message from the skills.

        :param message: the internal message
        :return: None
        """
        self.decision_maker_handler.handle(message)
