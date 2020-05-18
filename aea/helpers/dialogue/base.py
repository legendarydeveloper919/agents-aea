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

- DialogueLabel: The dialogue label class acts as an identifier for dialogues.
- Dialogue: The dialogue class maintains state of a dialogue and manages it.
- Dialogues: The dialogues class keeps track of all dialogues.
"""

import itertools
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Optional, Tuple, cast

from aea.mail.base import Address
from aea.protocols.base import Message


class DialogueLabel:
    """The dialogue label class acts as an identifier for dialogues."""

    def __init__(
        self,
        dialogue_reference: Tuple[str, str],
        dialogue_opponent_addr: Address,
        dialogue_starter_addr: Address,
    ) -> None:
        """
        Initialize a dialogue label.

        :param dialogue_reference: the reference of the dialogue.
        :param dialogue_opponent_addr: the addr of the agent with which the dialogue is kept.
        :param dialogue_starter_addr: the addr of the agent which started the dialogue.

        :return: None
        """
        self._dialogue_reference = dialogue_reference
        self._dialogue_opponent_addr = dialogue_opponent_addr
        self._dialogue_starter_addr = dialogue_starter_addr

    @property
    def dialogue_reference(self) -> Tuple[str, str]:
        """Get the dialogue reference."""
        return self._dialogue_reference

    @property
    def dialogue_starter_reference(self) -> str:
        """Get the dialogue starter reference."""
        return self._dialogue_reference[0]

    @property
    def dialogue_responder_reference(self) -> str:
        """Get the dialogue responder reference."""
        return self._dialogue_reference[1]

    @property
    def dialogue_opponent_addr(self) -> str:
        """Get the address of the dialogue opponent."""
        return self._dialogue_opponent_addr

    @property
    def dialogue_starter_addr(self) -> str:
        """Get the address of the dialogue starter."""
        return self._dialogue_starter_addr

    def __eq__(self, other) -> bool:
        """Check for equality between two DialogueLabel objects."""
        if type(other) == DialogueLabel:
            return (
                self.dialogue_reference == other.dialogue_reference
                and self.dialogue_starter_addr == other.dialogue_starter_addr
                and self.dialogue_opponent_addr == other.dialogue_opponent_addr
            )
        return False

    def __hash__(self) -> int:
        """Turn object into hash."""
        return hash(
            (
                self.dialogue_reference,
                self.dialogue_opponent_addr,
                self.dialogue_starter_addr,
            )
        )

    @property
    def json(self) -> Dict:
        """Return the JSON representation."""
        return {
            "dialogue_starter_reference": self.dialogue_starter_reference,
            "dialogue_responder_reference": self.dialogue_responder_reference,
            "dialogue_opponent_addr": self.dialogue_opponent_addr,
            "dialogue_starter_addr": self.dialogue_starter_addr,
        }

    @classmethod
    def from_json(cls, obj: Dict[str, str]) -> "DialogueLabel":
        """Get dialogue label from json."""
        dialogue_label = DialogueLabel(
            (
                cast(str, obj.get("dialogue_starter_reference")),
                cast(str, obj.get("dialogue_responder_reference")),
            ),
            cast(str, obj.get("dialogue_opponent_addr")),
            cast(str, obj.get("dialogue_starter_addr")),
        )
        return dialogue_label

    def __str__(self):
        """Get the string representation."""
        return "{}_{}_{}_{}".format(
            self.dialogue_starter_reference,
            self.dialogue_responder_reference,
            self.dialogue_opponent_addr,
            self.dialogue_starter_addr,
        )


class Dialogue(ABC):
    """The dialogue class maintains state of a dialogue and manages it."""

    STARTING_MESSAGE_ID = 1
    STARTING_TARGET = 0

    class Role(Enum):
        """This class defines the agent's role in a dialogue."""

        def __str__(self):
            """Get the string representation."""
            return self.value

    class EndState(Enum):
        """This class defines the end states of a dialogue."""

        def __str__(self):
            """Get the string representation."""
            return self.value

    def __init__(self, dialogue_label: DialogueLabel, role: Role = None) -> None:
        """
        Initialize a dialogue.

        :param dialogue_label: the identifier of the dialogue
        :param role: the role of the agent this dialogue is maintained for

        :return: None
        """
        self._dialogue_label = dialogue_label
        self._role = role

        self._is_self_initiated = (
            dialogue_label.dialogue_opponent_addr
            is not dialogue_label.dialogue_starter_addr
        )

        self._outgoing_messages = []  # type: List[Message]
        self._incoming_messages = []  # type: List[Message]

    @property
    def dialogue_label(self) -> DialogueLabel:
        """
        Get the dialogue label.

        :return: The dialogue label
        """
        return self._dialogue_label

    @property
    def role(self) -> "Role":
        """
        Get the agent's role in the dialogue.

        :return: the agent's role
        """
        assert self._role is not None, "Role is not set."
        return self._role

    @role.setter
    def role(self, role: "Role") -> None:
        """
        Set the agent's role in the dialogue.

        :param role: the agent's role
        :return: None
        """
        self._role = role

    @property
    def is_self_initiated(self) -> bool:
        """
        Check whether the agent initiated the dialogue.

        :return: True if the agent initiated the dialogue, False otherwise
        """
        return self._is_self_initiated

    @property
    def last_incoming_message(self) -> Optional[Message]:
        """
        Get the last incoming message.

        :return: the last incoming message if it exists, None otherwise
        """
        return self._incoming_messages[-1] if len(self._incoming_messages) > 0 else None

    @property
    def last_outgoing_message(self) -> Optional[Message]:
        """
        Get the last outgoing message.

        :return: the last outgoing message if it exists, None otherwise
        """
        return self._outgoing_messages[-1] if len(self._outgoing_messages) > 0 else None

    @property
    def last_message(self) -> Optional[Message]:
        """
        Get the last message.

        :return: the last message if it exists, None otherwise
        """
        if (
            self.last_incoming_message is not None
            and self.last_outgoing_message is not None
        ):
            last_incoming_message_id = cast(
                int, self.last_incoming_message.get("message_id")
            )
            last_outgoing_message_id = cast(
                int, self.last_outgoing_message.get("message_id")
            )
            last_message = (
                self.last_outgoing_message
                if last_outgoing_message_id > last_incoming_message_id
                else self.last_incoming_message
            )
        elif (
            self.last_incoming_message is not None
            and self.last_outgoing_message is None
        ):
            last_message = self.last_incoming_message
        elif (
            self.last_incoming_message is None
            and self.last_outgoing_message is not None
        ):
            last_message = self.last_outgoing_message
        else:
            last_message = None

        return last_message

    @property
    def is_empty(self) -> bool:
        """
        Check whether the dialogue is empty

        :return: True if empty, False otherwise
        """
        return len(self._outgoing_messages) == 0 and len(self._incoming_messages) == 0

    def outgoing_extend(self, message: "Message") -> None:
        """
        Extend the list of outgoing messages with 'message'

        :param message: a message to be added
        :return: None
        """
        self._outgoing_messages.extend([message])

    def incoming_extend(self, message: "Message") -> None:
        """
        Extend the list of incoming messages with 'message'

        :param message: a message to be added
        :return: None
        """
        self._incoming_messages.extend([message])

    def outgoing_safe_extend(self, message: "Message") -> bool:
        """
        Extend the list of outgoing messages with 'message', if 'message' is valid

        :param message: a message to be added
        :return: True if message successfully added, false otherwise
        """
        is_extendable = self.is_valid_next_message(message)
        if is_extendable:
            self.outgoing_extend(message)
        return is_extendable

    def incoming_safe_extend(self, message: "Message") -> bool:
        """
        Extend the list of incoming messages with 'message', if 'message' is valid

        :param message: a message to be added
        :return: True if message successfully added, false otherwise
        """
        is_extendable = self.is_valid_next_message(message)
        if is_extendable:
            self.incoming_extend(message)
        return is_extendable

    def update(self, message: "Message") -> bool:
        """
        Extend the list of incoming/outgoing messages with 'message', if 'message' is valid

        :param message: a message to be added
        :return: True if message successfully added, false otherwise
        """
        if message.is_incoming:
            is_successful = self.incoming_safe_extend(message)
        else:
            is_successful = self.outgoing_safe_extend(message)
        return is_successful

    @abstractmethod
    def is_valid_next_message(self, message: "Message") -> bool:
        """
        Check whether 'message' is a valid next message in this dialogue.

        :param message: the message to be validated
        :return: True if yes, False otherwise.
        """

    @staticmethod
    @abstractmethod
    def role_from_first_message(message: Message) -> "Role":
        """
        Infer the role of the agent from an incoming/outgoing first message

        :param message: an incoming/outgoing first message
        :return: The role of the agent
        """

    @staticmethod
    def _interleave(list_1, list_2) -> List:
        all_elements = [
            element
            for element in itertools.chain(*itertools.zip_longest(list_1, list_2))
            if element is not None
        ]

        return all_elements

    def __str__(self) -> str:
        """
        Get the string representation.

        :return: The string representation of the dialogue
        """
        representation = "Dialogue Label: " + str(self.dialogue_label) + "\n"

        if self.is_self_initiated:
            all_messages = self._interleave(
                self._outgoing_messages, self._incoming_messages
            )
        else:
            all_messages = self._interleave(
                self._incoming_messages, self._outgoing_messages
            )

        for msg in all_messages:
            representation += str(msg.get("performative")) + "( )\n"

        representation = representation[:-1]
        return representation


class Dialogues:
    """The dialogues class keeps track of all dialogues for an agent."""

    def __init__(self, agent_address: Address = "") -> None:
        """
        Initialize dialogues.

        :param agent_address: the address of the agent for whom dialogues are maintained
        :return: None
        """
        self._dialogues = {}  # type: Dict[DialogueLabel, Dialogue]
        self._agent_address = agent_address
        self._dialogue_nonce = 0

    @property
    def dialogues(self) -> Dict[DialogueLabel, Dialogue]:
        """Get dictionary of dialogues in which the agent engages."""
        return self._dialogues

    @property
    def agent_address(self) -> Address:
        """Get the address of the agent for whom dialogues are maintained."""
        assert self._agent_address != "", "agent_address is not set."
        return self._agent_address

    @abstractmethod
    def get_dialogue(self, message: Message) -> Optional[Dialogue]:
        """
        Retrieve the dialogue 'message' belongs to

        :param message: a message
        :return: the dialogue if such a dialogue is found, None otherwise
        """

    @abstractmethod
    def update(self, message: Message) -> Optional[Dialogue]:
        """
        Update the state of dialogues with a new message.

        If the message is for a new dialogue, a new dialogue is created with 'message' as its first message and returned.
        If the message is addressed to an existing dialogue, the dialogue is retrieved, extended with this message and returned.
        If there are any errors, e.g. the message dialogue reference does not exists or the message is invalid w.r.t. the dialogue, return None.

        :param message: a new message
        :return: the new or existing dialogue the message is intended for, or None in case of any errors.
        """

    def _next_dialogue_nonce(self) -> int:
        """
        Increment the nonce and return it.

        :return: the next nonce
        """
        self._dialogue_nonce += 1
        return self._dialogue_nonce

    def new_self_initiated_dialogue_reference(self) -> Tuple[str, str]:
        """
        Return a dialogue label for a new self initiated dialogue

        :return: the next nonce
        """
        return str(self._dialogue_nonce + 1), ""

    # ToDo the following methods are left for backwards compatibility reasons and will be removed in the future
    def is_belonging_to_registered_dialogue(
        self, msg: Message, agent_addr: Address
    ) -> bool:
        """
        DEPRECATED

        Check whether an agent message is part of a registered dialogue.

        :param msg: the agent message
        :param agent_addr: the address of the agent

        :return: boolean indicating whether the message belongs to a registered dialogue
        """
        pass

    def is_permitted_for_new_dialogue(self, msg: Message) -> bool:
        """
        DEPRECATED

        Check whether an agent message is permitted for a new dialogue.

        :param msg: the agent message
        :return: a boolean indicating whether the message is permitted for a new dialogue
        """
        pass
