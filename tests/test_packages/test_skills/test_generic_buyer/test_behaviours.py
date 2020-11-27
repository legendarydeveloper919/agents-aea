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
"""This module contains the tests of the behaviour classes of the generic buyer skill."""

import logging
from pathlib import Path
from typing import cast
from unittest.mock import patch

from aea.helpers.transaction.base import RawTransaction
from aea.protocols.dialogue.base import DialogueMessage
from aea.test_tools.test_skill import BaseSkillTestCase

from packages.fetchai.connections.ledger.base import CONNECTION_ID as LEDGER_PUBLIC_ID
from packages.fetchai.protocols.ledger_api.message import LedgerApiMessage
from packages.fetchai.protocols.oef_search.message import OefSearchMessage
from packages.fetchai.skills.generic_buyer.behaviours import (
    GenericSearchBehaviour,
    GenericTransactionBehaviour,
)
from packages.fetchai.skills.generic_buyer.dialogues import (
    LedgerApiDialogue,
    LedgerApiDialogues,
)
from packages.fetchai.skills.generic_buyer.handlers import LEDGER_API_ADDRESS
from packages.fetchai.skills.generic_buyer.strategy import GenericStrategy

from tests.conftest import ROOT_DIR


FETCHAI = "fetchai"


class TestSearchBehaviour(BaseSkillTestCase):
    """Test Search behaviour of generic buyer."""

    path_to_skill = Path(ROOT_DIR, "packages", "fetchai", "skills", "generic_buyer")

    @classmethod
    def setup(cls):
        """Setup the test class."""
        super().setup()
        cls.search_behaviour = cast(
            GenericSearchBehaviour, cls._skill.skill_context.behaviours.search
        )
        cls.strategy = cast(GenericStrategy, cls._skill.skill_context.strategy)

    def test_setup_is_ledger_tx(self):
        """Test the setup method of the search behaviour where is_ledger_tx is True."""
        # operation
        self.search_behaviour.setup()

        # after
        self.assert_quantity_in_outbox(1)
        has_attributes, error_str = self.message_has_attributes(
            actual_message=self.get_message_from_outbox(),
            message_type=LedgerApiMessage,
            performative=LedgerApiMessage.Performative.GET_BALANCE,
            to=str(LEDGER_PUBLIC_ID),
            sender=self.skill.skill_context.agent_address,
            ledger_id=FETCHAI,
            address=self.skill.skill_context.agent_address,
        )
        assert has_attributes, error_str

    def test_setup_not_is_ledger_tx(self):
        """Test the setup method of the search behaviour where is_ledger_tx is False."""
        # setup
        self.strategy._is_ledger_tx = False

        # before
        assert not self.strategy.is_searching

        # operation
        self.search_behaviour.setup()

        # after
        assert self.strategy.is_searching

    def test_act_is_searching(self):
        """Test the act method of the search behaviour where is_searching is True."""
        # setup
        self.strategy._is_searching = True

        # operation
        self.search_behaviour.act()

        # after
        self.assert_quantity_in_outbox(1)
        has_attributes, error_str = self.message_has_attributes(
            actual_message=self.get_message_from_outbox(),
            message_type=OefSearchMessage,
            performative=OefSearchMessage.Performative.SEARCH_SERVICES,
            to=self.skill.skill_context.search_service_address,
            sender=self.skill.skill_context.agent_address,
            query=self.skill.skill_context.strategy.get_location_and_service_query(),
        )
        assert has_attributes, error_str

    def test_act_not_is_searching(self):
        """Test the act method of the search behaviour where is_searching is False."""
        # setup
        self.strategy._is_searching = False

        # operation
        self.search_behaviour.act()

        # after
        self.assert_quantity_in_outbox(0)

    def test_teardown(self):
        """Test the teardown method of the search behaviour."""
        assert self.search_behaviour.teardown() is None
        self.assert_quantity_in_outbox(0)


class TestTransactionBehaviour(BaseSkillTestCase):
    """Test transaction behaviour of generic buyer."""

    path_to_skill = Path(ROOT_DIR, "packages", "fetchai", "skills", "generic_buyer")

    @classmethod
    def setup(cls):
        """Setup the test class."""
        super().setup()
        cls.transaction_behaviour = cast(
            GenericTransactionBehaviour, cls._skill.skill_context.behaviours.transaction
        )
        cls.logger = cls._skill.skill_context.logger
        cls.ledger_api_dialogues = cast(
            LedgerApiDialogues, cls._skill.skill_context.ledger_api_dialogues
        )
        cls.strategy = cast(GenericStrategy, cls._skill.skill_context.strategy)

    def test_setup(self):
        """Test the setup method of the transaction behaviour."""
        assert self.transaction_behaviour.teardown() is None
        self.assert_quantity_in_outbox(0)

    def test_act_i(self):
        """Test the act method of the transaction behaviour."""
        # setup
        processing_time = 5.0
        max_processing = 120
        self.transaction_behaviour.processing = None
        self.transaction_behaviour.max_processing = max_processing
        self.transaction_behaviour.processing_time = processing_time

        ledger_api_dialogue = cast(
            LedgerApiDialogue,
            self.prepare_skill_dialogue(
                dialogues=self.ledger_api_dialogues,
                messages=(
                    DialogueMessage(
                        LedgerApiMessage.Performative.GET_RAW_TRANSACTION,
                        {"terms": "some_terms"},
                    ),
                ),
                counterparty=LEDGER_API_ADDRESS,
            ),
        )
        ledger_api_message = cast(
            LedgerApiMessage,
            self.build_incoming_message_for_skill_dialogue(
                dialogue=ledger_api_dialogue,
                performative=LedgerApiMessage.Performative.RAW_TRANSACTION,
                raw_transaction=RawTransaction("some_ledger_id", "some_body"),
            ),
        )
        self.transaction_behaviour.waiting = [(ledger_api_dialogue, ledger_api_message)]

        # before
        assert self.transaction_behaviour.processing_time == processing_time
        assert self.transaction_behaviour.processing is None

        # operation
        with patch.object(self.logger, "log") as mock_logger:
            self.transaction_behaviour.act()

        # after
        self.assert_quantity_in_outbox(1)

        assert self.transaction_behaviour.processing_time == 0.0
        assert self.transaction_behaviour.processing is ledger_api_dialogue

        mock_logger.assert_any_call(
            logging.INFO,
            f"requesting transfer transaction from ledger api for message={ledger_api_message}...",
        )
        message = self.get_message_from_outbox()
        assert message == ledger_api_message

    def test_act_ii(self):
        """Test the act method of the transaction behaviour where processing is not None and processing_time < max_processing."""
        # setup
        processing_time = 5.0
        self.transaction_behaviour.processing = "some_dialogue"
        self.transaction_behaviour.max_processing = 120
        self.transaction_behaviour.processing_time = processing_time

        # operation
        self.transaction_behaviour.act()

        # after
        self.assert_quantity_in_outbox(0)
        assert (
            self.transaction_behaviour.processing_time
            == processing_time + self.transaction_behaviour.tick_interval
        )

    def test_act_iii(self):
        """Test the act method of the transaction behaviour where len(waiting) == 0."""
        # setup
        self.transaction_behaviour.processing = None
        self.transaction_behaviour.waiting = []

        # operation
        self.transaction_behaviour.act()

        # after
        self.assert_quantity_in_outbox(0)

    def test_teardown(self):
        """Test the teardown method of the transaction behaviour."""
        assert self.transaction_behaviour.teardown() is None
        self.assert_quantity_in_outbox(0)
