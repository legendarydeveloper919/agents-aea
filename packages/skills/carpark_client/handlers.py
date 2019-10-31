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

"""This package contains a scaffold of a handler."""
import logging
import pprint
from typing import Optional, cast, List, TYPE_CHECKING

from aea.configurations.base import ProtocolId
from aea.protocols.base import Message
from aea.protocols.default.message import DefaultMessage
from aea.protocols.default.serialization import DefaultSerializer
from aea.protocols.fipa.message import FIPAMessage
from aea.protocols.fipa.serialization import FIPASerializer
from aea.protocols.oef.message import OEFMessage
from aea.protocols.oef.models import Description
from aea.skills.base import Handler
from aea.decision_maker.messages.transaction import TransactionMessage

if TYPE_CHECKING:
    from packages.skills.carpark_client.dialogues import Dialogue, Dialogues
    from packages.skills.carpark_client.strategy import Strategy
else:
    from carpark_client_skill.dialogues import Dialogue, Dialogues
    from carpark_client_skill.strategy import Strategy

logger = logging.getLogger("aea.carpark_client_skill")

STARTING_MESSAGE_ID = 1
STARTING_TARGET_ID = 0
DEFAULT_MAX_PRICE = 2.0


class FIPAHandler(Handler):
    """This class scaffolds a handler."""

    SUPPORTED_PROTOCOL = FIPAMessage.protocol_id  # type: Optional[ProtocolId]

    def __init__(self, **kwargs):
        """Initialise the class."""
        super().__init__(**kwargs)

    def setup(self) -> None:
        """
        Implement the setup.

        :return: None
        """
        pass

    def handle(self, message: Message, sender: str) -> None:
        """
        Implement the reaction to a message.

        :param message: the message
        :param sender: the sender
        :return: None
        """
        # convenience representations
        fipa_msg = cast(FIPAMessage, message)
        msg_performative = FIPAMessage.Performative(message.get('performative'))
        message_id = cast(int, message.get("message_id"))
        dialogue_id = cast(int, message.get("dialogue_id"))

        # recover dialogue
        dialogues = cast(Dialogues, self.context.dialogues)
        if dialogues.is_belonging_to_registered_dialogue(fipa_msg, sender, self.context.agent_public_key):
            dialogue = dialogues.get_dialogue(fipa_msg, sender, self.context.agent_public_key)
            dialogue.incoming_extend(fipa_msg)
        else:
            self._handle_unidentified_dialogue(fipa_msg, sender)
            return

        # handle message
        if msg_performative == FIPAMessage.Performative.PROPOSE:
            self._handle_propose(fipa_msg, sender, message_id, dialogue_id, dialogue)
        elif msg_performative == FIPAMessage.Performative.DECLINE:
            self._handle_decline(fipa_msg, sender, message_id, dialogue_id, dialogue)
        elif msg_performative == FIPAMessage.Performative.MATCH_ACCEPT_W_ADDRESS:
            self._handle_match_accept(fipa_msg, sender, message_id, dialogue_id, dialogue)
        elif msg_performative == FIPAMessage.Performative.INFORM:
            self._handle_inform(fipa_msg, sender, message_id, dialogue_id, dialogue)

    def teardown(self) -> None:
        """
        Implement the handler teardown.

        :return: None
        """
        pass

    def _handle_unidentified_dialogue(self, msg: FIPAMessage, sender: str) -> None:
        """
        Handle an unidentified dialogue.

        :param msg: the message
        :param sender: the sender
        """
        logger.info("[{}]: unidentified dialogue.".format(self.context.agent_name))
        default_msg = DefaultMessage(type=DefaultMessage.Type.ERROR,
                                     error_code=DefaultMessage.ErrorCode.INVALID_DIALOGUE.value,
                                     error_msg="Invalid dialogue.",
                                     error_data="fipa_message")  # FIPASerializer().encode(msg))
        self.context.outbox.put_message(to=sender,
                                        sender=self.context.agent_public_key,
                                        protocol_id=DefaultMessage.protocol_id,
                                        message=DefaultSerializer().encode(default_msg))

    def _handle_propose(self, msg: FIPAMessage, sender: str, message_id: int, dialogue_id: int, dialogue: Dialogue) -> None:
        """
        Handle the propose.

        :param msg: the message
        :param sender: the sender
        :param message_id: the message id
        :param dialogue_id: the dialogue id
        :param dialogue: the dialogue object
        :return: None
        """
        new_message_id = message_id + 1
        new_target_id = message_id
        proposals = cast(List[Description], msg.get("proposal"))

        if proposals is not []:
            # only take the first proposal
            proposal = proposals[0]
            logger.info("[{}]: received proposal={} from sender={}".format(self.context.agent_name,
                                                                           proposal.values,
                                                                           sender[-5:]))
            strategy = cast(Strategy, self.context.strategy)
            acceptable = strategy.is_acceptable_proposal(proposal)
            affordable = self.context.ledger_apis.token_balance('fetchai', cast(str, self.context.agent_addresses.get('fetchai'))) >= cast(int, proposal.values.get('price'))
            if acceptable and affordable:
                logger.info("[{}]: accepting the proposal from sender={}".format(self.context.agent_name,
                                                                                 sender[-5:]))
                dialogue.proposal = proposal
                accept_msg = FIPAMessage(message_id=new_message_id,
                                         dialogue_id=dialogue_id,
                                         target=new_target_id,
                                         performative=FIPAMessage.Performative.ACCEPT)
                dialogue.outgoing_extend(accept_msg)
                self.context.outbox.put_message(to=sender,
                                                sender=self.context.agent_public_key,
                                                protocol_id=FIPAMessage.protocol_id,
                                                message=FIPASerializer().encode(accept_msg))
            else:
                logger.info("[{}]: declining the proposal from sender={}".format(self.context.agent_name,
                                                                                 sender[-5:]))
                strategy.unpause_search()
                decline_msg = FIPAMessage(message_id=new_message_id,
                                          dialogue_id=dialogue_id,
                                          target=new_target_id,
                                          performative=FIPAMessage.Performative.DECLINE)
                dialogue.outgoing_extend(decline_msg)
                self.context.outbox.put_message(to=sender,
                                                sender=self.context.agent_public_key,
                                                protocol_id=FIPAMessage.protocol_id,
                                                message=FIPASerializer().encode(decline_msg))


    def _handle_decline(self, msg: FIPAMessage, sender: str, message_id: int, dialogue_id: int, dialogue: Dialogue) -> None:
        """
        Handle the decline.

        :param msg: the message
        :param sender: the sender
        :param message_id: the message id
        :param dialogue_id: the dialogue id
        :param dialogue: the dialogue object
        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        strategy.unpause_search()
        logger.info("[{}]: received DECLINE from sender={}".format(self.context.agent_name, sender[-5:]))
        # target = msg.get("target")
        # dialogues = cast(Dialogues, self.context.dialogues)
        # if target == 1:
        #     dialogues.dialogue_stats.add_dialogue_endstate(Dialogue.EndState.DECLINED_CFP)
        # elif target == 3:
        #     dialogues.dialogue_stats.add_dialogue_endstate(Dialogue.EndState.DECLINED_ACCEPT)

    def _handle_match_accept(self, msg: FIPAMessage, sender: str, message_id: int, dialogue_id: int, dialogue: Dialogue) -> None:
        """
        Handle the match accept.

        :param msg: the message
        :param sender: the sender
        :param message_id: the message id
        :param dialogue_id: the dialogue id
        :param dialogue: the dialogue object
        :return: None
        """
        logger.info("[{}]: received MATCH_ACCEPT_W_ADDRESS from sender={}".format(self.context.agent_name, sender[-5:]))
        address = cast(str, msg.get("address"))
        proposal = cast(Description, dialogue.proposal)
        tx_msg = TransactionMessage(performative=TransactionMessage.Performative.PROPOSE,
                                    skill_id="carpark_client",
                                    transaction_id="transaction0",
                                    sender=self.context.agent_public_keys['fetchai'],
                                    counterparty=address,
                                    is_sender_buyer=True,
                                    currency_pbk="FET",
                                    amount=proposal.values['price'],
                                    sender_tx_fee=0,
                                    counterparty_tx_fee=0,
                                    quantities_by_good_pbk={},
                                    dialogue_label=dialogue.dialogue_label.json)
        self.context.decision_maker_message_queue.put_nowait(tx_msg)
        logger.info("[{}]: proposing the transaction to the decision maker. Waiting for confirmation ...".format(self.context.agent_name))

    def _handle_inform(self, msg: FIPAMessage, sender: str, message_id: int, dialogue_id: int, dialogue: Dialogue) -> None:
        """
        Handle the match inform.

        :param msg: the message
        :param sender: the sender
        :param message_id: the message id
        :param dialogue_id: the dialogue id
        :param dialogue: the dialogue object
        :return: None
        """
        logger.info("[{}]: received INFORM from sender={}".format(self.context.agent_name, sender[-5:]))
        json_data = cast(dict, msg.get("json_data"))
        if 'message_type' in json_data and json_data['message_type'] == 'car_park_data':
            logger.info("[{}]: received the following carpark data={}".format(self.context.agent_name,
                                                                              pprint.pformat(json_data)))
            # dialogues = cast(Dialogues, self.context.dialogues)
            # dialogues.dialogue_stats.add_dialogue_endstate(Dialogue.EndState.SUCCESSFUL)
        else:
            logger.info("[{}]: received no data from sender={}".format(self.context.agent_name,
                                                                       sender[-5:]))


class OEFHandler(Handler):
    """This class scaffolds a handler."""

    SUPPORTED_PROTOCOL = OEFMessage.protocol_id  # type: Optional[ProtocolId]

    def __init__(self, **kwargs):
        """Initialise the oef handler."""
        super().__init__(**kwargs)

    def setup(self) -> None:
        """Call to setup the handler."""
        pass

    def handle(self, message: Message, sender: str) -> None:
        """
        Implement the reaction to a message.

        :param message: the message
        :param sender: the sender
        :return: None
        """
        # convenience representations
        oef_msg = cast(OEFMessage, message)
        oef_msg_type = OEFMessage.Type(oef_msg.get("type"))

        if oef_msg_type is OEFMessage.Type.SEARCH_RESULT:
            agents = cast(List[str], oef_msg.get("agents"))
            self._handle_search(agents)

    def teardown(self) -> None:
        """
        Implement the handler teardown.

        :return: None
        """
        pass

    def _handle_search(self, agents: List[str]) -> None:
        """
        Handle the search response.

        :param agents: the agents returned by the search
        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        if len(agents) > 0:
            logger.info("[{}]: found agents={}, stopping search.".format(self.context.agent_name, list(map(lambda x: x[-5:], agents))))

            # pick first agent found
            opponent_pbk = agents[0]
            dialogues = cast(Dialogues, self.context.dialogues)
            dialogue = dialogues.create_self_initiated(opponent_pbk, self.context.agent_public_key)
            query = strategy.get_service_query()
            logger.info("[{}]: sending CFP to agent={}".format(self.context.agent_name, opponent_pbk[-5:]))
            cfp_msg = FIPAMessage(message_id=STARTING_MESSAGE_ID,
                                  dialogue_id=dialogue.dialogue_label.dialogue_id,
                                  performative=FIPAMessage.Performative.CFP,
                                  target=STARTING_TARGET_ID,
                                  query=query)
            dialogue.outgoing_extend(cfp_msg)
            self.context.outbox.put_message(to=opponent_pbk,
                                            sender=self.context.agent_public_key,
                                            protocol_id=FIPAMessage.protocol_id,
                                            message=FIPASerializer().encode(cfp_msg))
        else:
            strategy.unpause_search()
            logger.info("[{}]: found no agents, continue searching.".format(self.context.agent_name))
