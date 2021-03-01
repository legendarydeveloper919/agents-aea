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
"""This module contains tests for the logical behaviour of the tac negotiation skill."""
import copy
from pathlib import Path
from unittest.mock import patch

from aea.decision_maker.gop import GoalPursuitReadiness, OwnershipState, Preferences
from aea.helpers.preference_representations.base import (
    linear_utility,
    logarithmic_utility,
)
from aea.test_tools.test_skill import BaseSkillTestCase

from packages.fetchai.skills.tac_control.helpers import (
    determine_scaling_factor,
    generate_utility_params,
)
from packages.fetchai.skills.tac_negotiation.dialogues import FipaDialogue
from packages.fetchai.skills.tac_negotiation.strategy import Strategy

from tests.conftest import ROOT_DIR


class TestLogical(BaseSkillTestCase):
    """Logical Tests for tac negotiation."""

    path_to_skill = Path(ROOT_DIR, "packages", "fetchai", "skills", "tac_negotiation")

    @classmethod
    def setup(cls):
        """Setup the test class."""
        tac_dm_context_kwargs = {
            "goal_pursuit_readiness": GoalPursuitReadiness(),
            "ownership_state": OwnershipState(),
            "preferences": Preferences(),
        }
        super().setup(dm_context_kwargs=tac_dm_context_kwargs)
        cls.register_as = "both"
        cls.search_for = "both"
        cls.is_contract_tx = False
        cls.ledger_id = "some_ledger_id"
        cls.location = {"longitude": 0.1270, "latitude": 51.5194}
        cls.search_radius = 5.0
        cls.service_key = "tac_service"

        cls.strategy = Strategy(
            register_as=cls.register_as,
            search_for=cls.search_for,
            is_contract_tx=cls.is_contract_tx,
            ledger_id=cls.ledger_id,
            location=cls.location,
            service_key=cls.service_key,
            search_radius=cls.search_radius,
            name="strategy",
            skill_context=cls._skill.skill_context,
        )

        cls.sender = "some_sender_address"
        cls.counterparty = "some_counterparty_address"

        cls.mocked_currency_id = "12"
        cls.mocked_currency_amount = 2000000
        cls.mocked_amount_by_currency_id = {
            cls.mocked_currency_id: cls.mocked_currency_amount
        }
        cls.mocked_good_ids = ["13", "14", "15", "16", "17", "18", "19", "20", "21"]
        cls.mocked_good_quantities = [5, 7, 4, 3, 5, 4, 3, 5, 6]
        cls.mocked_quantities_by_good_id = dict(
            zip(cls.mocked_good_ids, cls.mocked_good_quantities)
        )
        cls.mocked_ownership_state = (
            cls._skill.skill_context.decision_maker_handler_context.ownership_state
        )
        cls.mocked_ownership_state.set(
            cls.mocked_amount_by_currency_id, cls.mocked_quantities_by_good_id
        )

        cls.exchange_params_by_currency_id = {cls.mocked_currency_id: 1.0}
        cls.utility_params_by_good_id = generate_utility_params(
            [cls._skill.skill_context.agent_address],
            cls.mocked_good_ids,
            determine_scaling_factor(cls.mocked_currency_amount),
        )[cls._skill.skill_context.agent_address]
        cls.mocked_preferences = (
            cls._skill.skill_context.decision_maker_handler_context.preferences
        )
        cls.mocked_preferences.set(
            exchange_params_by_currency_id=cls.exchange_params_by_currency_id,
            utility_params_by_good_id=cls.utility_params_by_good_id,
        )

    @staticmethod
    def _calculate_score(preferences, ownership_state):
        """Calculate the score given a preferences and an ownership_state object."""
        goods_score = logarithmic_utility(
            preferences.utility_params_by_good_id,
            ownership_state.quantities_by_good_id,
        )
        money_score = linear_utility(
            preferences.exchange_params_by_currency_id,
            ownership_state.amount_by_currency_id,
        )
        return goods_score + money_score

    def test_generated_proposals_increase_score_seller(self):
        """Test whether the proposals generated by _generate_candidate_proposals method of the Strategy class actually increases agent's score where role is seller."""
        # setup
        is_searching_for_sellers = True

        # operation
        with patch.object(
            self.skill.skill_context.transactions,
            "ownership_state_after_locks",
            return_value=self.mocked_ownership_state,
        ) as mock_ownership:
            actual_proposals = self.strategy._generate_candidate_proposals(
                is_searching_for_sellers
            )

        # after
        mock_ownership.assert_any_call(is_seller=is_searching_for_sellers)

        current_score = self._calculate_score(
            self.mocked_preferences, self.mocked_ownership_state
        )
        for proposal in actual_proposals:
            # applying proposal on a new ownership_state
            terms = self.strategy.terms_from_proposal(
                proposal, self.sender, self.counterparty, FipaDialogue.Role.SELLER
            )
            new_ownership_state = copy.copy(self.mocked_ownership_state)
            new_ownership_state.apply_delta(
                terms.amount_by_currency_id, terms.quantities_by_good_id
            )

            # new score
            new_score = self._calculate_score(
                self.mocked_preferences, new_ownership_state
            )

            assert new_score >= current_score

    def test_generated_proposals_increase_score_buyer(self):
        """Test whether the proposals generated by _generate_candidate_proposals method of the Strategy class actually increases agent's score  where role is buyer."""
        # setup
        is_searching_for_sellers = False

        # operation
        with patch.object(
            self.skill.skill_context.transactions,
            "ownership_state_after_locks",
            return_value=self.mocked_ownership_state,
        ) as mock_ownership:
            actual_proposals = self.strategy._generate_candidate_proposals(
                is_searching_for_sellers
            )

        # after
        mock_ownership.assert_any_call(is_seller=is_searching_for_sellers)

        current_score = self._calculate_score(
            self.mocked_preferences, self.mocked_ownership_state
        )
        for proposal in actual_proposals:
            # applying proposal on a new ownership_state
            terms = self.strategy.terms_from_proposal(
                proposal, self.sender, self.counterparty, FipaDialogue.Role.BUYER
            )
            new_ownership_state = copy.copy(self.mocked_ownership_state)
            new_ownership_state.apply_delta(
                terms.amount_by_currency_id, terms.quantities_by_good_id
            )

            # new score
            new_score = self._calculate_score(
                self.mocked_preferences, new_ownership_state
            )

            assert new_score >= current_score
