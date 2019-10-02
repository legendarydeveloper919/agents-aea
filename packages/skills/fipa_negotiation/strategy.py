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

"""This module contains the abstract class defining an agent's strategy for the TAC."""

from abc import abstractmethod
from enum import Enum
from typing import List, Set, Optional

from aea.protocols.oef.models import Description

from tac.agents.participant.v1.base.states import WorldState


class RegisterAs(Enum):
    """This class defines the service registration options."""

    SELLER = 'seller'
    BUYER = 'buyer'
    BOTH = 'both'


class SearchFor(Enum):
    """This class defines the service search options."""

    SELLERS = 'sellers'
    BUYERS = 'buyers'
    BOTH = 'both'


class Strategy:
    """This class defines an abstract strategy for the agent."""

    def __init__(self, register_as: RegisterAs = RegisterAs.BOTH, search_for: SearchFor = SearchFor.BOTH, is_world_modeling: bool = False) -> None:
        """
        Initialize the strategy of the agent.

        :param register_as: determines whether the agent registers as seller, buyer or both
        :param search_for: determines whether the agent searches for sellers, buyers or both
        :param is_world_modeling: determines whether the agent has a model of the world

        :return: None
        """
        self._register_as = register_as
        self._search_for = search_for
        self._is_world_modeling = is_world_modeling
        if is_world_modeling:
            self._world_state = None  # TODO

    @property
    def is_world_modeling(self) -> bool:
        """Check if the world is modeled by the agent."""
        return self._is_world_modeling

    # @property
    # def world_state(self) -> WorldState:
    #     """Get the world state."""
    #     assert self._is_world_modeling, "World state is not modeled!"
    #     return self._world_state

    @property
    def is_registering_as_seller(self) -> bool:
        """Check if the agent registers as a seller on the OEF."""
        return self._register_as == RegisterAs.SELLER or self._register_as == RegisterAs.BUYER

    @property
    def is_searching_for_sellers(self) -> bool:
        """Check if the agent searches for sellers on the OEF."""
        return self._search_for == SearchFor.SELLERS or self._search_for == SearchFor.BOTH

    @property
    def is_registering_as_buyer(self) -> bool:
        """Check if the agent registers as a buyer on the OEF."""
        return self._register_as == RegisterAs.BUYER or self._register_as == RegisterAs.BOTH

    @property
    def is_searching_for_buyers(self) -> bool:
        """Check if the agent searches for buyers on the OEF."""
        return self._search_for == SearchFor.BUYERS or self._search_for == SearchFor.BOTH


    def get_own_service_description(self, is_supply: bool) -> Description:

    def get_own_services_query(self, is_searching_for_sellers: bool) -> Query:

    def generate_proposal_description_for_query(query: Query, is_seller: bool) -> Optional[Description]:
        """
        Generate proposal (in the form of a description) which matches the query.

        :param query: the query
        :is_seller: whether the agent making the proposal is a seller or not

        :return: a description
        """
        candidate_proposals = self._generate_candidate_proposals(is_seller)
        proposals = []
        for proposal in candidate_proposals:
            if not query.check(proposal): continue
            proposals.append(proposal)
        if not proposals:
            return None
        else:
            return random.choice(proposals)

    def _generate_candidate_proposals(self, is_seller: bool):
        """
        Generate proposals from the agent in the role of seller/buyer.

        :param is_seller: the bool indicating whether the agent is a seller.

        :return: a list of proposals in Description form
        """


    def _supplied_good_pbks_to_quantities(self) -> Dict[str, int]:
        """
        Generate the dictionary of goods and quantities supplied by the agent

        :return: a dictionary of goods and quantities
        """


    def _demanded_good_pbks_to_quantities(self) -> Dict[str, int]:
        """
        Generate the dictionary of goods and quantities demanded by the agent

        :return: a dictionary of goods and quantities
        """


    def is_profitable_transaction(self, transaction_msg: TransactionMessage, dialogue: Dialogue) -> Tuple[bool, str]:
        """
        Check if a transaction is profitable.

        Is it a profitable transaction?
        - apply all the locks for role.
        - check if the transaction is consistent with the locks (enough money/holdings)
        - check that we gain score.

        :param transaction: the transaction
        :param dialogue: the dialogue

        :return: True if the transaction is good (as stated above), False otherwise.
        """
        state_after_locks = self.state_after_locks(dialogue.is_seller)

        if not state_after_locks.check_transaction_is_consistent(transaction, self.game_configuration.tx_fee):
            message = "[{}]: the proposed transaction is not consistent with the state after locks.".format(self.agent_name)
            return False, message
        proposal_delta_score = state_after_locks.get_score_diff_from_transaction(transaction, self.game_configuration.tx_fee)

        result = self.strategy.is_acceptable_proposal(proposal_delta_score)
        message = "[{}]: is good proposal for {}? {}: tx_id={}, delta_score={}, amount={}".format(self.agent_name, dialogue.role, result, transaction.transaction_id, proposal_delta_score, transaction.amount)
        return result, message

    def is_acceptable_proposal(self, proposal_delta_score: float) -> bool:
        """
        Determine whether a proposal is acceptable to the agent.

        :param proposal_delta_score: the difference in score the proposal causes

        :return: a boolean indicating whether the proposal is acceptable or not
        """
        result = proposal_delta_score >= 0
        return result

    def get_service_description(self, is_supply: bool) -> Description:
        """
        Get the description of the supplied goods (as a seller), or the demanded goods (as a buyer).

        :param is_supply: Boolean indicating whether it is supply or demand.

        :return: the description (to advertise on the Service Directory).
        """
        desc = get_goods_quantities_description(self.game_configuration.good_pbks,
                                                self.get_goods_quantities(is_supply),
                                                is_supply=is_supply)
        return desc

    def build_services_query(self, is_searching_for_sellers: bool) -> Optional[Query]:
        """
        Build a query to search for services.

        In particular, build the query to look for agents
            - which supply the agent's demanded goods (i.e. sellers), or
            - which demand the agent's supplied goods (i.e. buyers).

        :param is_searching_for_sellers: Boolean indicating whether the search is for sellers or buyers.

        :return: the Query, or None.
        """
        good_pbks = self.get_goods_pbks(is_supply=not is_searching_for_sellers)

        res = None if len(good_pbks) == 0 else build_query(good_pbks, is_searching_for_sellers)
        return res

    def build_services_dict(self, is_supply: bool) -> Optional[Dict[str, Sequence[str]]]:
        """
        Build a dictionary containing the services demanded/supplied.

        :param is_supply: Boolean indicating whether the services are demanded or supplied.

        :return: a Dict.
        """
        good_pbks = self.get_goods_pbks(is_supply=is_supply)

        res = None if len(good_pbks) == 0 else build_dict(good_pbks, is_supply)
        return res

    def is_matching(self, cfp_services: Dict[str, Union[bool, List[Any]]], goods_description: Description) -> bool:
        """
        Check for a match between the CFP services and the goods description.

        :param cfp_services: the services associated with the cfp.
        :param goods_description: a description of the goods.

        :return: Bool
        """
        services = cfp_services['services']
        services = cast(List[Any], services)
        if cfp_services['description'] is goods_description.data_model.name:
            # The call for proposal description and the goods model name cannot be the same for trading agent pairs.
            return False
        for good_pbk in goods_description.data_model.attributes_by_name.keys():
            if good_pbk not in services: continue
            return True
        return False

    def get_goods_pbks(self, is_supply: bool) -> Set[str]:
        """
        Wrap the function which determines supplied and demanded good public keys.

        :param is_supply: Boolean indicating whether it is referencing the supplied or demanded public keys.

        :return: a list of good public keys
        """
        state_after_locks = self.state_after_locks(is_seller=is_supply)
        good_pbks = self.strategy.supplied_good_pbks(self.game_configuration.good_pbks, state_after_locks.current_holdings) if is_supply else self.strategy.demanded_good_pbks(self.game_configuration.good_pbks, state_after_locks.current_holdings)
        return good_pbks

    def get_goods_quantities(self, is_supply: bool) -> List[int]:
        """
        Wrap the function which determines supplied and demanded good quantities.

        :param is_supply: Boolean indicating whether it is referencing the supplied or demanded quantities.

        :return: the vector of good quantities offered/requested.
        """
        state_after_locks = self.state_after_locks(is_seller=is_supply)
        quantities = self.strategy.supplied_good_quantities(state_after_locks.current_holdings) if is_supply else self.strategy.demanded_good_quantities(state_after_locks.current_holdings)
        return quantities

    def state_after_locks(self, is_seller: bool) -> AgentState:
        """
        Apply all the locks to the current state of the agent.

        This assumes, that all the locked transactions will be successful.

        :param is_seller: Boolean indicating the role of the agent.

        :return: the agent state with the locks applied to current state
        """
        assert self._agent_state is not None, "Agent state not assigned!"
        transactions = list(self.transaction_manager.locked_txs_as_seller.values()) if is_seller \
            else list(self.transaction_manager.locked_txs_as_buyer.values())
        state_after_locks = self._agent_state.apply(transactions, self.game_configuration.tx_fee)
        return state_after_locks






def generate_transaction_id(agent_pbk: Address, opponent_pbk: Address, dialogue_label: DialogueLabel, agent_is_seller: bool) -> str:
    """
    Make a transaction id.

    :param agent_pbk: the pbk of the agent.
    :param opponent_pbk: the public key of the opponent.
    :param dialogue_label: the dialogue label
    :param agent_is_seller: boolean indicating if the agent is a seller
    :return: a transaction id
    """
    # the format is {buyer_pbk}_{seller_pbk}_{dialogue_id}_{dialogue_starter_pbk}
    assert opponent_pbk == dialogue_label.dialogue_opponent_pbk
    buyer_pbk, seller_pbk = (opponent_pbk, agent_pbk) if agent_is_seller else (agent_pbk, opponent_pbk)
    transaction_id = "{}_{}_{}_{}".format(buyer_pbk, seller_pbk, dialogue_label.dialogue_id, dialogue_label.dialogue_starter_pbk)
    return transaction_id


def dialogue_label_from_transaction_id(agent_pbk: Address, transaction_id: TransactionId) -> DialogueLabel:
    """
    Recover dialogue label from transaction id.

    :param agent_pbk: the pbk of the agent.
    :param transaction_id: the transaction id
    :return: a dialogue label
    """
    buyer_pbk, seller_pbk, dialogue_id, dialogue_starter_pbk = transaction_id.split('_')
    if agent_pbk == buyer_pbk:
        dialogue_opponent_pbk = seller_pbk
    else:
        dialogue_opponent_pbk = buyer_pbk
    dialogue_label = DialogueLabel(int(dialogue_id), dialogue_opponent_pbk, dialogue_starter_pbk)
    return dialogue_label


def build_datamodel(good_pbks: List[str], is_supply: bool) -> DataModel:
    """
    Build a data model for supply and demand (i.e. for offered or requested goods).

    :param good_pbks: the list of good public keys
    :param is_supply: Boolean indicating whether it is a supply or demand data model

    :return: the data model.
    """
    goods_quantities_attributes = [Attribute(good_pbk, int, False)
                                   for good_pbk in good_pbks]
    price_attribute = Attribute("price", float, False)
    description = TAC_SUPPLY_DATAMODEL_NAME if is_supply else TAC_DEMAND_DATAMODEL_NAME
    data_model = DataModel(description, goods_quantities_attributes + [price_attribute])
    return data_model


def get_goods_quantities_description(good_pbks: List[str], good_quantities: List[int], is_supply: bool) -> Description:
    """
    Get the TAC description for supply or demand.

    That is, a description with the following structure:
    >>> description = {
    ...     "tac_good_0": 1,
    ...     "tac_good_1": 0,
    ...     #...
    ...
    ... }
    >>>

     where the keys indicate the good_pbk and the values the quantity.

     >>> desc = get_goods_quantities_description(['tac_good_0', 'tac_good_1', 'tac_good_2', 'tac_good_3'], [0, 0, 1, 2], True)
     >>> desc.data_model.name == TAC_SUPPLY_DATAMODEL_NAME
     True
     >>> desc.values == {
     ...    "tac_good_0": 0,
     ...    "tac_good_1": 0,
     ...    "tac_good_2": 1,
     ...    "tac_good_3": 2}
     ...
     True

    :param good_pbks: the public keys of the goods.
    :param good_quantities: the quantities per good.
    :param is_supply: True if the description is indicating supply, False if it's indicating demand.

    :return: the description to advertise on the Service Directory.
    """
    data_model = build_datamodel(good_pbks, is_supply=is_supply)
    desc = Description({good_pbk: quantity for good_pbk, quantity in zip(good_pbks, good_quantities)},
                       data_model=data_model)
    return desc


def build_query(good_pbks: Set[str], is_searching_for_sellers: bool) -> Query:
    """
    Build buyer or seller search query.

    Specifically, build the search query
        - to look for sellers if the agent is a buyer, or
        - to look for buyers if the agent is a seller.

    In particular, if the agent is a buyer and the demanded good public keys are {'tac_good_0', 'tac_good_2', 'tac_good_3'}, the resulting constraint expression is:

        tac_good_0 >= 1 OR tac_good_2 >= 1 OR tac_good_3 >= 1

    That is, the OEF will return all the sellers that have at least one of the good in the query
    (assuming that the sellers are registered with the data model specified).

    :param good_pbks: the good public keys to put in the query
    :param is_searching_for_sellers: Boolean indicating whether the query is for sellers (supply) or buyers (demand).

    :return: the query
    """
    data_model = None if good_pbks is None else build_datamodel(list(good_pbks), is_supply=is_searching_for_sellers)
    constraints = [Constraint(good_pbk, GtEq(1)) for good_pbk in good_pbks]

    if len(good_pbks) > 1:
        constraints = [Or(constraints)]

    query = Query(constraints, model=data_model)
    return query


def build_dict(good_pbks: Set[str], is_supply: bool) -> Dict[str, Sequence[str]]:
    """
    Build supply or demand services dictionary.

    :param good_pbks: the good public keys to put in the query
    :param is_supply: Boolean indicating whether the services are for supply or demand.

    :return: the dictionary
    """
    description = TAC_SUPPLY_DATAMODEL_NAME if is_supply else TAC_DEMAND_DATAMODEL_NAME
    result = {'description': description, 'services': list(good_pbks)}
    return result


    def supplied_good_quantities(self, current_holdings: List[int]) -> List[int]:
        """
        Generate a list of quantities which are supplied.

        :param current_holdings: a list of current good holdings
        :return: a list of quantities
        """
        return [quantity - 1 for quantity in current_holdings]

    def supplied_good_pbks(self, good_pbks: List[str], current_holdings: List[int]) -> Set[str]:
        """
        Generate a set of good public keys which are supplied.

        :param good_pbks: a list of good public keys
        :param current_holdings: a list of current good holdings

        :return: a set of public keys
        """
        return {good_pbk for good_pbk, quantity in zip(good_pbks, current_holdings) if quantity > 1}

    def demanded_good_quantities(self, current_holdings: List[int]) -> List[int]:
        """
        Generate a list of quantities which are demanded.

        :param current_holdings: a list of current good holdings

        :return: a list of quantities
        """
        return [1 for _ in current_holdings]

    def demanded_good_pbks(self, good_pbks: List[str], current_holdings: List[int]) -> Set[str]:
        """
        Generate a set of good public keys which are demanded.

        :param good_pbks: a list of good public keys
        :param current_holdings: a list of current good holdings

        :return: a set of public keys
        """
        return {good_pbk for good_pbk, quantity in zip(good_pbks, current_holdings)}

    def get_proposals(self, good_pbks: List[str], current_holdings: List[int], utility_params: List[float], tx_fee: float, is_seller: bool, world_state: Optional[WorldState]) -> List[Description]:
        """
        Generate a proposals from the seller/buyer.

        :param good_pbks: a list of good public keys
        :param current_holdings: a list of current good holdings
        :param utility_params: a list of utility params
        :param tx_fee: the transaction fee
        :param is_seller: Boolean indicating the role of the agent
        :param world_state: the world state module

        :return: a list of proposals in Description form
        """
        quantities = self.supplied_good_quantities(current_holdings) if is_seller else self.demanded_good_quantities(current_holdings)
        share_of_tx_fee = round(tx_fee / 2.0, 2)
        rounding_adjustment = 0.01
        proposals = []
        for good_id, good_pbk in zip(range(len(quantities)), good_pbks):
            if is_seller and quantities[good_id] == 0: continue
            proposal = [0] * len(quantities)
            proposal[good_id] = 1
            desc = get_goods_quantities_description(good_pbks, proposal, is_supply=is_seller)
            delta_holdings = [i * -1 for i in proposal] if is_seller else proposal
            switch = -1 if is_seller else 1
            marginal_utility_from_delta_holdings = marginal_utility(utility_params, current_holdings, delta_holdings) * switch
            if self.is_world_modeling:
                assert world_state is not None, "Need to provide world state if is_world_modeling=True."
                desc.values["price"] = world_state.expected_price(good_pbk, round(marginal_utility_from_delta_holdings, 2), is_seller, share_of_tx_fee)
            else:
                if is_seller:
                    desc.values["price"] = round(marginal_utility_from_delta_holdings, 2) + share_of_tx_fee + rounding_adjustment
                else:
                    desc.values["price"] = round(marginal_utility_from_delta_holdings, 2) - share_of_tx_fee - rounding_adjustment
            if not desc.values["price"] > 0: continue
            proposals.append(desc)
        return proposals