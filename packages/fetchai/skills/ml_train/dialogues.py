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

"""
This module contains the classes required for dialogue management.

- DefaultDialogue: The dialogue class maintains state of a dialogue of type default and manages it.
- DefaultDialogues: The dialogues class keeps track of all dialogues of type default.
- LedgerApiDialogue: The dialogue class maintains state of a dialogue of type ledger_api and manages it.
- LedgerApiDialogues: The dialogues class keeps track of all dialogues of type ledger_api.
- MlTradeDialogue: The dialogue class maintains state of a dialogue of type ml_trade and manages it.
- MlTradeDialogues: The dialogues class keeps track of all dialogues of type ml_trade.
"""

from typing import Optional, Type

from aea.common import Address
from aea.exceptions import AEAEnforceError, enforce
from aea.helpers.dialogue.base import Dialogue as BaseDialogue
from aea.helpers.dialogue.base import DialogueLabel as BaseDialogueLabel
from aea.protocols.base import Message
from aea.protocols.default.dialogues import DefaultDialogue as BaseDefaultDialogue
from aea.protocols.default.dialogues import DefaultDialogues as BaseDefaultDialogues
from aea.protocols.signing.dialogues import SigningDialogue as BaseSigningDialogue
from aea.protocols.signing.dialogues import SigningDialogues as BaseSigningDialogues
from aea.protocols.signing.message import SigningMessage
from aea.skills.base import Model


from packages.fetchai.protocols.ledger_api.dialogues import (
    LedgerApiDialogue as BaseLedgerApiDialogue,
)
from packages.fetchai.protocols.ledger_api.dialogues import (
    LedgerApiDialogues as BaseLedgerApiDialogues,
)
from packages.fetchai.protocols.ledger_api.dialogues import LedgerApiMessage
from packages.fetchai.protocols.ml_trade.dialogues import (
    MlTradeDialogue as BaseMlTradeDialogue,
)
from packages.fetchai.protocols.ml_trade.dialogues import (
    MlTradeDialogues as BaseMlTradeDialogues,
)
from packages.fetchai.protocols.oef_search.dialogues import (
    OefSearchDialogue as BaseOefSearchDialogue,
)
from packages.fetchai.protocols.oef_search.dialogues import (
    OefSearchDialogues as BaseOefSearchDialogues,
)

DefaultDialogue = BaseDefaultDialogue


class DefaultDialogues(Model, BaseDefaultDialogues):
    """The dialogues class keeps track of all dialogues."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :return: None
        """
        Model.__init__(self, **kwargs)

        def role_from_first_message(
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return DefaultDialogue.Role.AGENT

        BaseDefaultDialogues.__init__(
            self,
            agent_address=self.context.agent_address,
            role_from_first_message=role_from_first_message,
        )


MlTradeDialogue = BaseMlTradeDialogue


class MlTradeDialogues(Model, BaseMlTradeDialogues):
    """The dialogues class keeps track of all dialogues."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :return: None
        """
        Model.__init__(self, **kwargs)

        def role_from_first_message(
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return BaseMlTradeDialogue.Role.BUYER

        BaseMlTradeDialogues.__init__(
            self,
            agent_address=self.context.agent_address,
            role_from_first_message=role_from_first_message,
        )


class LedgerApiDialogue(BaseLedgerApiDialogue):
    """The dialogue class maintains state of a dialogue and manages it."""

    def __init__(
        self,
        dialogue_label: BaseDialogueLabel,
        agent_address: Address,
        role: BaseDialogue.Role,
        message_class: Type[LedgerApiMessage] = LedgerApiMessage,
    ) -> None:
        """
        Initialize a dialogue.

        :param dialogue_label: the identifier of the dialogue
        :param agent_address: the address of the agent for whom this dialogue is maintained
        :param role: the role of the agent this dialogue is maintained for

        :return: None
        """
        BaseLedgerApiDialogue.__init__(
            self,
            dialogue_label=dialogue_label,
            agent_address=agent_address,
            role=role,
            message_class=message_class,
        )
        self._associated_ml_trade_dialogue = None  # type: Optional[MlTradeDialogue]

    @property
    def associated_ml_trade_dialogue(self) -> MlTradeDialogue:
        """Get associated_ml_trade_dialogue."""
        if self._associated_ml_trade_dialogue is None:
            raise AEAEnforceError("MlTradeDialogue not set!")
        return self._associated_ml_trade_dialogue

    @associated_ml_trade_dialogue.setter
    def associated_ml_trade_dialogue(self, ml_trade_dialogue: MlTradeDialogue) -> None:
        """Set associated_ml_trade_dialogue"""
        enforce(
            self._associated_ml_trade_dialogue is None, "MlTradeDialogue already set!"
        )
        self._associated_ml_trade_dialogue = ml_trade_dialogue


class LedgerApiDialogues(Model, BaseLedgerApiDialogues):
    """The dialogues class keeps track of all dialogues."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :return: None
        """
        Model.__init__(self, **kwargs)

        def role_from_first_message(
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return BaseLedgerApiDialogue.Role.AGENT

        BaseLedgerApiDialogues.__init__(
            self,
            agent_address=self.context.agent_address,
            role_from_first_message=role_from_first_message,
            dialogue_class=LedgerApiDialogue,
        )


OefSearchDialogue = BaseOefSearchDialogue


class OefSearchDialogues(Model, BaseOefSearchDialogues):
    """This class keeps track of all oef_search dialogues."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :param agent_address: the address of the agent for whom dialogues are maintained
        :return: None
        """
        Model.__init__(self, **kwargs)

        def role_from_first_message(
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return BaseOefSearchDialogue.Role.AGENT

        BaseOefSearchDialogues.__init__(
            self,
            agent_address=self.context.agent_address,
            role_from_first_message=role_from_first_message,
        )


class SigningDialogue(BaseSigningDialogue):
    """The dialogue class maintains state of a dialogue and manages it."""

    def __init__(
        self,
        dialogue_label: BaseDialogueLabel,
        agent_address: Address,
        role: BaseDialogue.Role,
        message_class: Type[SigningMessage] = SigningMessage,
    ) -> None:
        """
        Initialize a dialogue.

        :param dialogue_label: the identifier of the dialogue
        :param agent_address: the address of the agent for whom this dialogue is maintained
        :param role: the role of the agent this dialogue is maintained for

        :return: None
        """
        BaseSigningDialogue.__init__(
            self,
            dialogue_label=dialogue_label,
            agent_address=agent_address,
            role=role,
            message_class=message_class,
        )
        self._associated_ledger_api_dialogue = None  # type: Optional[LedgerApiDialogue]

    @property
    def associated_ledger_api_dialogue(self) -> LedgerApiDialogue:
        """Get associated_ledger_api_dialogue."""
        if self._associated_ledger_api_dialogue is None:
            raise AEAEnforceError("LedgerApiDialogue not set!")
        return self._associated_ledger_api_dialogue

    @associated_ledger_api_dialogue.setter
    def associated_ledger_api_dialogue(
        self, ledger_api_dialogue: LedgerApiDialogue
    ) -> None:
        """Set associated_ledger_api_dialogue"""
        enforce(
            self._associated_ledger_api_dialogue is None,
            "LedgerApiDialogue already set!",
        )
        self._associated_ledger_api_dialogue = ledger_api_dialogue


class SigningDialogues(Model, BaseSigningDialogues):
    """This class keeps track of all oef_search dialogues."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :param agent_address: the address of the agent for whom dialogues are maintained
        :return: None
        """
        Model.__init__(self, **kwargs)

        def role_from_first_message(
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return BaseSigningDialogue.Role.SKILL

        BaseSigningDialogues.__init__(
            self,
            agent_address=self.context.agent_address,
            role_from_first_message=role_from_first_message,
            dialogue_class=SigningDialogue,
        )
