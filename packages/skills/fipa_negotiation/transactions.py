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

"""This module contains a class to manage transactions."""

import datetime
import logging
from collections import defaultdict, deque
from typing import Dict, Tuple, Deque, cast, TYPE_CHECKING

from aea.decision_maker.base import OwnershipState
from aea.decision_maker.messages.transaction import TransactionMessage, TransactionId
from aea.skills.base import SharedClass

if TYPE_CHECKING:
    from packages.skills.fipa_negotiation.dialogues import DialogueLabel
else:
    from fipa_negotiation_skill.dialogues import DialogueLabel

logger = logging.getLogger("aea.fipa_negotiation_skill")

MESSAGE_ID = int


class Transactions(SharedClass):
    """Class to handle pending transaction proposals/acceptances and locked transactions."""

    def __init__(self, pending_transaction_timeout: int, **kwargs) -> None:
        """Initialize the transactions."""
        super().__init__(**kwargs)
        self._pending_proposals = defaultdict(lambda: {})  # type: Dict[DialogueLabel, Dict[MESSAGE_ID, TransactionMessage]]
        self._pending_initial_acceptances = defaultdict(lambda: {})  # type: Dict[DialogueLabel, Dict[MESSAGE_ID, TransactionMessage]]
        self._pending_transaction_timeout = pending_transaction_timeout

        self._locked_txs = {}  # type: Dict[TransactionId, TransactionMessage]
        self._locked_txs_as_buyer = {}  # type: Dict[TransactionId, TransactionMessage]
        self._locked_txs_as_seller = {}  # type: Dict[TransactionId, TransactionMessage]

        self._last_update_for_transactions = deque()  # type: Deque[Tuple[datetime.datetime, TransactionId]]

    @property
    def pending_proposals(self) -> Dict[DialogueLabel, Dict[MESSAGE_ID, TransactionMessage]]:
        """Get the pending proposals."""
        return self._pending_proposals

    @property
    def pending_initial_acceptances(self) -> Dict[DialogueLabel, Dict[MESSAGE_ID, TransactionMessage]]:
        """Get the pending initial acceptances."""
        return self._pending_initial_acceptances

    def cleanup_pending_transactions(self) -> None:
        """
        Remove all the pending messages (i.e. either proposals or acceptances) that have been stored for an amount of time longer than the timeout.

        :return: None
        """
        queue = self._last_update_for_transactions
        timeout = datetime.timedelta(0, self._pending_transaction_timeout)

        if len(queue) == 0:
            return

        next_date, next_item = queue[0]

        while datetime.datetime.now() - next_date > timeout:

            # remove the element from the queue
            queue.popleft()

            # extract dialogue label and message id
            transaction_id = next_item
            logger.debug("Removing transaction: {}".format(transaction_id))

            # remove (safely) the associated pending proposal (if present)
            self._locked_txs.pop(transaction_id, None)
            self._locked_txs_as_buyer.pop(transaction_id, None)
            self._locked_txs_as_seller.pop(transaction_id, None)

            # check the next transaction, if present
            if len(queue) == 0:
                break
            next_date, next_item = queue[0]

    def add_pending_proposal(self, dialogue_label: DialogueLabel, proposal_id: int, transaction_msg: TransactionMessage) -> None:
        """
        Add a proposal (in the form of a transaction) to the pending list.

        :param dialogue_label: the dialogue label associated with the proposal
        :param proposal_id: the message id of the proposal
        :param transaction_msg: the transaction message
        :raise AssertionError: if the pending proposal is already present.

        :return: None
        """
        assert dialogue_label not in self._pending_proposals and proposal_id not in self._pending_proposals[dialogue_label]
        self._pending_proposals[dialogue_label][proposal_id] = transaction_msg

    def pop_pending_proposal(self, dialogue_label: DialogueLabel, proposal_id: int) -> TransactionMessage:
        """
        Remove a proposal (in the form of a transaction) from the pending list.

        :param dialogue_label: the dialogue label associated with the proposal
        :param proposal_id: the message id of the proposal
        :raise AssertionError: if the pending proposal is not present.

        :return: the transaction message
        """
        assert dialogue_label in self._pending_proposals and proposal_id in self._pending_proposals[dialogue_label]
        transaction_msg = self._pending_proposals[dialogue_label].pop(proposal_id)
        return transaction_msg

    def add_pending_initial_acceptance(self, dialogue_label: DialogueLabel, proposal_id: int, transaction_msg: TransactionMessage) -> None:
        """
        Add an acceptance (in the form of a transaction) to the pending list.

        :param dialogue_label: the dialogue label associated with the proposal
        :param proposal_id: the message id of the proposal
        :param transaction_msg: the transaction message
        :raise AssertionError: if the pending acceptance is already present.

        :return: None
        """
        assert dialogue_label not in self._pending_initial_acceptances and proposal_id not in self._pending_initial_acceptances[dialogue_label]
        self._pending_initial_acceptances[dialogue_label][proposal_id] = transaction_msg

    def pop_pending_initial_acceptance(self, dialogue_label: DialogueLabel, proposal_id: int) -> TransactionMessage:
        """
        Remove an acceptance (in the form of a transaction) from the pending list.

        :param dialogue_label: the dialogue label associated with the proposal
        :param proposal_id: the message id of the proposal
        :raise AssertionError: if the pending acceptance is not present.

        :return: the transaction message
        """
        assert dialogue_label in self._pending_initial_acceptances and proposal_id in self._pending_initial_acceptances[dialogue_label]
        transaction_msg = self._pending_initial_acceptances[dialogue_label].pop(proposal_id)
        return transaction_msg

    def _register_transaction_with_time(self, transaction_id: TransactionId) -> None:
        """
        Register a transaction with a creation datetime.

        :param transaction_id: the transaction id

        :return: None
        """
        now = datetime.datetime.now()
        self._last_update_for_transactions.append((now, transaction_id))

    def add_locked_tx(self, transaction_msg: TransactionMessage, as_seller: bool) -> None:
        """
        Add a lock (in the form of a transaction).

        :param transaction_msg: the transaction message
        :param as_seller: whether the agent is a seller or not
        :raise AssertionError: if the transaction is already present.

        :return: None
        """
        transaction_id = cast(TransactionId, transaction_msg.get("transaction_id"))
        assert transaction_id not in self._locked_txs
        self._register_transaction_with_time(transaction_id)
        self._locked_txs[transaction_id] = transaction_msg
        if as_seller:
            self._locked_txs_as_seller[transaction_id] = transaction_msg
        else:
            self._locked_txs_as_buyer[transaction_id] = transaction_msg

    def pop_locked_tx(self, transaction_msg: TransactionMessage) -> TransactionMessage:
        """
        Remove a lock (in the form of a transaction).

        :param transaction_msg: the transaction message
        :raise AssertionError: if the transaction with the given transaction id has not been found.

        :return: the transaction
        """
        transaction_id = cast(TransactionId, transaction_msg.get("transaction_id"))
        assert transaction_id in self._locked_txs
        transaction_msg = self._locked_txs.pop(transaction_id)
        self._locked_txs_as_buyer.pop(transaction_id, None)
        self._locked_txs_as_seller.pop(transaction_id, None)
        return transaction_msg

    def ownership_state_after_locks(self, ownership_state: OwnershipState, is_seller: bool) -> OwnershipState:
        """
        Apply all the locks to the current ownership state of the agent.

        This assumes, that all the locked transactions will be successful.

        :param is_seller: Boolean indicating the role of the agent.

        :return: the agent state with the locks applied to current state
        """
        transaction_msgs = list(self._locked_txs_as_seller.values()) if is_seller else list(self._locked_txs_as_buyer.values())
        ownershio_state_after_locks = ownership_state.apply(transaction_msgs)
        return ownershio_state_after_locks

    def reset(self) -> None:
        """Reset the class."""
        self._pending_proposals = defaultdict(lambda: {})
        self._pending_initial_acceptances = defaultdict(lambda: {})
        self._locked_txs = {}
        self._locked_txs_as_buyer = {}
        self._locked_txs_as_seller = {}
        self._last_update_for_transactions = deque()
