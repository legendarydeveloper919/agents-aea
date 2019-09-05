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

"""This module contains the implementation of an Autonomous Economic Agent."""
import base64
import importlib.util
import inspect
import logging
import re
from abc import abstractmethod, ABC
from typing import Optional, Dict, List

from aea.agent import Agent
from aea.mail.base import Envelope, ProtocolId
from aea.protocols.base.protocol import Protocol
from aea.protocols.default.message import DefaultMessage
from aea.protocols.default.serialization import DefaultSerializer

logger = logging.getLogger(__name__)

SkillId = str


class Behaviour(ABC):
    """This class implements an abstract behaviour."""

    @abstractmethod
    def act(self) -> None:
        """
        Implement the behaviour.

        :return: None
        """

    @abstractmethod
    def teardown(self) -> None:
        """
        Implement the behaviour teardown.

        :return: None
        """


class Handler(ABC):
    """This class implements an abstract behaviour."""

    SUPPORTED_PROTOCOL = None  # type: Optional[ProtocolId]

    @abstractmethod
    def handle_envelope(self, envelope: Envelope) -> None:
        """
        Implement the reaction to an envelope.

        :param envelope: the envelope
        :return: None
        """

    @abstractmethod
    def teardown(self) -> None:
        """
        Implement the handler teardown.

        :return: None
        """


class DefaultHandler(Handler):
    """This class implements the default handler."""

    SUPPORTED_PROTOCOL = 'default'  # type: Optional[ProtocolId]

    def handle_envelope(self, envelope: Envelope) -> None:
        """
        Implement the reaction to an envelope.

        :param envelope: the envelope
        :return: None
        """
        pass  # TODO: this could be the ping method? > no, then on error from other agent causes endless loop; just print out the response and raise a warning?

    def teardown(self) -> None:
        """
        Implement the handler teardown.

        :return: None
        """
        pass

    def on_unsupported_protocol(self, envelope: Envelope) -> None:
        """
        Handle the received envelope in case the protocol is not supported.

        :param envelope: the envelope
        :return: None
        """
        logger.warning("Unsupported protocol: {}".format(envelope.protocol_id))
        reply = DefaultMessage(type=DefaultMessage.Type.ERROR,
                               error_code=DefaultMessage.ErrorCode.UNSUPPORTED_PROTOCOL,
                               error_msg="Unsupported protocol.",
                               error_data={"protocol_id": envelope.protocol_id})
        # TODO: outbox not available in handler yet
        self.outbox.put_message(to=envelope.sender, sender=self.name, protocol_id=DefaultMessage.protocol_id,
                                message=DefaultSerializer().encode(reply))

    def on_decoding_error(self, envelope: Envelope) -> None:
        """
        Handle a decoding error.

        :param envelope: the envelope
        :return: None
        """
        logger.warning("Decoding error: {}.".format(envelope))
        encoded_envelope = base64.b85encode(envelope.encode()).decode("utf-8")
        reply = DefaultMessage(type=DefaultMessage.Type.ERROR,
                               error_code=DefaultMessage.ErrorCode.DECODING_ERROR,
                               error_msg="Decoding error.",
                               error_data={"envelope": encoded_envelope})
        self.outbox.put_message(to=envelope.sender, sender=self.name, protocol_id=DefaultMessage.protocol_id,
                                message=DefaultSerializer().encode(reply))

    def on_invalid_message(self, envelope: Envelope) -> None:
        """
        Handle an message that is invalid wrt a protocol.

        :param envelope: the envelope
        :return: None
        """
        logger.warning("Invalid message wrt protocol: {}.".format(envelope.protocol_id))
        encoded_envelope = base64.b85encode(envelope.encode()).decode("utf-8")
        reply = DefaultMessage(type=DefaultMessage.Type.ERROR,
                               error_code=DefaultMessage.ErrorCode.INVALID_MESSAGE,
                               error_msg="Invalid message.",
                               error_data={"envelope": encoded_envelope})
        self.outbox.put_message(to=envelope.sender, sender=self.name, protocol_id=DefaultMessage.protocol_id,
                                message=DefaultSerializer().encode(reply))

    def on_unsupported_skill(self, envelope: Envelope, protocol: Protocol) -> None:
        """
        Handle the received envelope in case the skill is not supported.

        :param envelope: the envelope
        :param protocol: the protocol
        :return: None
        """
        logger.warning("Cannot handle envelope: no handler registered for the protocol '{}'.".format(protocol.name))
        encoded_envelope = base64.b85encode(envelope.encode()).decode("utf-8")
        reply = DefaultMessage(type=DefaultMessage.Type.ERROR,
                               error_code=DefaultMessage.ErrorCode.UNSUPPORTED_SKILL,
                               error_msg="Unsupported skill.",
                               error_data={"envelope": encoded_envelope})
        self.outbox.put_message(to=envelope.sender, sender=self.name, protocol_id=DefaultMessage.protocol_id,
                                message=DefaultSerializer().encode(reply))


class Task(ABC):
    """This class implements an abstract task."""

    @abstractmethod
    def execute(self) -> None:
        """
        Run the task logic.

        :return: None
        """

    @abstractmethod
    def teardown(self) -> None:
        """
        Teardown the task.

        :return: None
        """


class Skill:
    """This class implements a skill."""

    def __init__(self, handler: Handler,
                 behaviours: List[Behaviour],
                 tasks: List[Task]):
        """
        Initialize a skill.

        :param handler: the handler to handle incoming envelopes.
        :param behaviours: the list of behaviours that defines the proactive component of the agent.
        :param tasks: the list of tasks executed at every iteration of the main loop.
        """
        self.handler = handler
        self.behaviours = behaviours
        self.tasks = tasks


class Registry(ABC):
    """This class implements an abstract registry."""

    @abstractmethod
    def populate(self, directory: str) -> None:
        """
        Load into the registry as specified in the config and apply consistency checks.

        :param directory: the filepath to the agent's resource directory.
        :return: None
        """

    @abstractmethod
    def teardown(self) -> None:
        """
        Teardown the registry.

        :return: None
        """


class ProtocolRegistry(Registry):
    """This class implements the handlers registry."""

    def __init__(self) -> None:
        """
        Instantiate the registry.

        :return: None
        """
        self._protocols = {}  # type: Dict[ProtocolId, Protocol]

    def populate(self, directory: str) -> None:
        """
        Load the handlers as specified in the config and apply consistency checks.

        :param directory: the filepath to the agent's resource directory.
        :return: None
        """
        import pdb
        pdb.set_trace()
        protocols_spec = importlib.util.find_spec("protocols")
        if protocols_spec is None:
            logger.warning("No protocol found.")
            return

        protocols_packages = list(filter(lambda x: not x.startswith("__"), protocols_spec.loader.contents()))
        logger.debug("Processing the following protocol package: {}".format(protocols_packages))
        for protocol_name in protocols_packages:
            try:
                self._add_protocol(directory, protocol_name)
            except Exception:
                logger.exception("Not able to add protocol {}.".format(protocol_name))

    def fetch_protocol(self, protocol_id: ProtocolId) -> Optional[Protocol]:
        """
        Fetch the protocol for the envelope.

        :pass protocol_id: the protocol id
        :return: the protocol id or None if the protocol is not registered
        """
        return self._protocols.get(protocol_id, None)

    def teardown(self) -> None:
        """
        Teardown the registry.

        :return: None
        """
        self._protocols = {}

    def _add_protocol(self, directory: str, protocol_name: str):
        """
        Add a protocol.

        :param directory: the agent's resources directory.
        :param protocol_name: the name of the protocol to be added.
        :return: None
        """
        # get the serializer
        serialization_module = importlib.import_module(".".join(["protocols", protocol_name, "serialization"]))
        classes = inspect.getmembers(serialization_module, inspect.isclass)
        serializer_classes = list(filter(lambda x: re.match("\\w+Serializer", x[0]), classes))
        serializer_class = serializer_classes[0][1]

        logger.debug("Found serializer class {serializer_class} for protocol {protocol_name}"
                     .format(serializer_class=serializer_class, protocol_name=protocol_name))
        serializer = serializer_class()

        # instantiate the protocol manager.
        protocol = Protocol(protocol_name, serializer)
        self._protocols[protocol_name] = protocol


class HandlerRegistry(Registry):
    """This class implements the handlers registry."""

    def __init__(self) -> None:
        """
        Instantiate the registry.

        :return: None
        """
        self._handlers = {}  # type: Dict[SkillId, Handler]

    def populate(self, directory: str) -> None:
        """
        Load the handlers as specified in the config and apply consistency checks.

        :param directory: the agent's resources directory.
        :return: None
        """
        skills_spec = importlib.util.find_spec("skills")
        if skills_spec is None:
            logger.warning("No skill found.")
            return

        skills_packages = list(filter(lambda x: not x.startswith("__"), skills_spec.loader.contents()))
        logger.debug("Processing the following skill package: {}".format(skills_packages))
        for skill_name in skills_packages:
            try:
                self._add_skill_handler(directory, skill_name)
            except Exception:
                logger.exception("Not able to add handler for skill {}.".format(skill_name))

    def fetch_handler(self, protocol_id: ProtocolId) -> Optional[Handler]:
        """
        Fetch the handler for the protocol_id.

        :param protocol_id: the protocol id
        :return: the handler
        """
        return self._handlers.get(protocol_id, None)

    def fetch_default(self) -> Handler:
        """
        Fetch the handler for the default protocol.

        :return: the handler
        """
        return self._handlers.get('default')  # TODO: 'default' handler must always be present. So it should be a reserved handler distributed with the base aea. However, this might clash with what people want to use default protocol for?

    def teardown(self) -> None:
        """
        Teardown the registry.

        :return: None
        """
        for handler in self._handlers.values():
            handler.teardown()
        self._handlers = {}

    def _add_skill_handler(self, directory, skill_name):
        """Add a skill handler."""
        handler_module = importlib.import_module(".".join([directory, "skills", skill_name, "handler"]))
        classes = inspect.getmembers(handler_module, inspect.isclass)
        handler_classes = list(filter(lambda x: re.match("\\w+Handler", x[0]), classes))
        handler_class = handler_classes[0][1]

        logger.debug("Found handler class {handler_class} for skill {skill_name}"
                     .format(handler_class=handler_class, skill_name=skill_name))
        handler = handler_class()
        self._handlers[handler.SUPPORTED_PROTOCOL] = handler


class BehaviourRegistry(Registry):
    """This class implements the behaviour registry."""

    def __init__(self) -> None:
        """
        Instantiate the registry.

        :return: None
        """
        self._behaviours = {}  # type: Dict[SkillId, Behaviour]

    def populate(self, directory: str) -> None:
        """
        Load the behaviours as specified in the config and apply consistency checks.

        :param directory: the agent's resources directory.
        :return: None
        """
        pass

    def fetch_behaviours(self) -> List[Behaviour]:
        """
        Return a list of behaviours for processing.

        :return: the list of behaviours
        """
        return []

    def teardown(self) -> None:
        """
        Teardown the registry.

        :return: None
        """
        for behaviour in self._behaviours.values():
            behaviour.teardown()
        self._behaviours = {}


class TaskRegistry(Registry):
    """This class implements the task registry."""

    def __init__(self) -> None:
        """
        Instantiate the registry.

        :return: None
        """
        self._tasks = {}  # type: Dict[SkillId, Task]

    def populate(self, directory: str) -> None:
        """
        Load the tasks as specified in the config and apply consistency checks.

        :param directory: the agent's resources directory.
        :return: None
        """
        pass

    def fetch_tasks(self) -> List[Task]:
        """
        Return a list of tasks for processing.

        :return: a list of tasks.
        """
        return []

    def teardown(self) -> None:
        """
        Teardown the registry.

        :return: None
        """
        for task in self._tasks.values():
            task.teardown()
        self._tasks = {}


class Resources(object):
    """This class implements the resources of an AEA."""

    def __init__(self):
        """Instantiate the resources."""
        self.protocol_registry = ProtocolRegistry()
        self.handler_registry = HandlerRegistry()
        self.behaviour_registry = BehaviourRegistry()
        self.task_registry = TaskRegistry()
        self._skills = dict()  # type: Dict[SkillId, Skill]

        self._registries = [self.protocol_registry, self.handler_registry, self.behaviour_registry, self.task_registry]

    def populate(self, directory: str) -> None:
        """
        Populate the resources based on the registries.

        :param directory: the agent's resources directory.
        :return: None
        """
        for r in self._registries:
            r.populate(directory)

    def teardown(self):
        """
        Teardown the resources.

        :return: None
        """
        for r in self._registries:
            r.teardown()


class AEA(Agent):
    """This class implements an autonomous economic agent."""

    def __init__(self, name: str,
                 private_key_pem_path: Optional[str] = None,
                 timeout: Optional[float] = 1.0,  # TODO we might want to set this to 0 for the aea and let the skills take care of slowing things down on a skill level
                 debug: bool = False,
                 max_reactions: int = 20) -> None:
        """
        Instantiate the agent.

        :param name: the name of the agent
        :param private_key_pem_path: the path to the private key of the agent.
        :param timeout: the time in (fractions of) seconds to time out an agent between act and react
        :param debug: if True, run the agent in debug mode.
        :param max_reactions: the processing rate of messages per iteration.

        :return: None
        """
        super().__init__(name=name, private_key_pem_path=private_key_pem_path, timeout=timeout, debug=debug)

        self.max_reactions = max_reactions
        self._directory = self.name  # TODO fix, should be inferred from directory of the agent

        self.resources = Resources()

    def setup(self) -> None:
        """
        Set up the agent.

        :return: None
        """
        self.resources.populate(self._directory)

    def act(self) -> None:
        """
        Perform actions.

        :return: None
        """
        for behaviour in self.resources.behaviour_registry.fetch_behaviours():  # the skill should be able to register things here as active so we hand control fully to the skill and let this just spin through
            behaviour.act()
        # NOTE: we must ensure that these are non-blocking.

    def react(self) -> None:
        """
        React to incoming events (envelopes).

        :return: None
        """
        counter = 0
        while not self.inbox.empty() and counter < self.max_reactions:
            counter += 1
            envelope = self.inbox.get_nowait()  # type: Optional[Envelope]
            if envelope is not None:
                self.handle(envelope)
        # Note: here things are processed sequentially, but on a skill level anything can be done (e.g. wait for several messages/ create templates etc.)
        # NOTE: we must ensure that these are non-blocking.

    def handle(self, envelope: Envelope) -> None:
        """
        Handle an envelope.

        :param envelope: the envelope to handle.
        :return: None
        """
        protocol = self.resources.protocol_registry.fetch_protocol(envelope.protocol_id)

        if protocol is None:
            default_handler = self.resources.handler_registry.fetch_default()
            default_handler.on_unsupported_protocol(envelope)
            return

        try:
            msg = protocol.serializer.decode(envelope.message)
        except Exception:
            default_handler = self.resources.handler_registry.fetch_default()
            default_handler.on_decoding_error(envelope)
            return

        if not protocol.check(msg):
            default_handler = self.resources.handler_registry.fetch_default()
            default_handler.on_invalid_message(envelope)
            return

        handler = self.resources.handler_registry.fetch_handler(protocol.name)  # what is id vs name? TODO: so handler_registry is responsible for deciding which handler gets to serve the protocol!..is that what we want? again, seems like the skills should register themselves with the registry as well and be able to do so programmatically,
        if handler is None:
            default_handler = self.resources.handler_registry.fetch_default()
            default_handler.on_unsupported_skill(envelope)
            return

        handler.handle_envelope(envelope)

    def update(self) -> None:
        """Update the current state of the agent.

        :return None
        """
        for task in self._task_registry.fetch_tasks():
            task.execute()

    def teardown(self) -> None:
        """
        Tear down the agent.

        :return: None
        """
        self.resources.teardown()

        # TODO: docs step 1: what can an aea with no skills do? > it just sends the default responses
        # step 2: add ping skill
        # step 3: add negotiation_skill
