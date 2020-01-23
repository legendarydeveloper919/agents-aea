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
"""This module contains the tests for aea/aea.py."""

import os
import tempfile
import time
from pathlib import Path
from threading import Thread

import pytest

import yaml

from aea import AEA_DIR
from aea.aea import AEA
from aea.configurations.base import ProtocolConfig, PublicId
from aea.crypto.default import DEFAULT
from aea.crypto.ledger_apis import LedgerApis
from aea.crypto.wallet import Wallet
from aea.mail.base import Envelope
from aea.protocols.base import Protocol
from aea.protocols.default.message import DefaultMessage
from aea.protocols.default.serialization import DefaultSerializer
from aea.registries.base import Resources
from aea.skills.base import Skill

from packages.fetchai.connections.local.connection import LocalNode, OEFLocalConnection
from packages.fetchai.protocols.fipa.message import FIPAMessage
from packages.fetchai.protocols.fipa.serialization import FIPASerializer

from .conftest import CUR_PATH


def test_initialise_aea():
    """Tests the initialisation of the AEA."""
    node = LocalNode()
    address_1 = "address"
    connections1 = [
        OEFLocalConnection(
            address_1, node, connection_id=PublicId("fetchai", "local", "0.1.0")
        )
    ]
    private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
    wallet = Wallet({"default": private_key_pem_path})
    ledger_apis = LedgerApis({}, "default")
    my_AEA = AEA(
        "Agent0",
        connections1,
        wallet,
        ledger_apis,
        resources=Resources(str(Path(CUR_PATH, "aea"))),
    )
    assert my_AEA.context == my_AEA._context, "Cannot access the Agent's Context"
    assert (
        not my_AEA.context.connection_status.is_connected
    ), "AEA should not be connected."
    my_AEA.setup()
    assert my_AEA.resources is not None, "Resources must not be None after setup"
    my_AEA.resources = Resources(str(Path(CUR_PATH, "aea")))
    assert my_AEA.resources is not None, "Resources must not be None after set"
    assert (
        my_AEA.context.shared_state is not None
    ), "Shared state must not be None after set"
    assert (
        my_AEA.context.public_key is not None
    ), "Public key must not be None after set."
    my_AEA.stop()
    assert (
        my_AEA.context.task_queue is not None
    ), "Task queue must not be None after set."


def test_act():
    """Tests the act function of the AEA."""
    with LocalNode() as node:
        agent_name = "MyAgent"
        private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
        wallet = Wallet({"default": private_key_pem_path})
        ledger_apis = LedgerApis({}, "default")
        address = wallet.addresses["default"]
        connections = [
            OEFLocalConnection(
                address, node, connection_id=PublicId("fetchai", "local", "0.1.0")
            )
        ]
        resources = Resources(str(Path(CUR_PATH, "data", "dummy_aea")))

        agent = AEA(
            agent_name, connections, wallet, ledger_apis, resources, programmatic=False
        )
        t = Thread(target=agent.start)
        try:
            t.start()
            time.sleep(1.0)

            behaviour = agent.resources.behaviour_registry.fetch(
                (PublicId.from_string("dummy_author/dummy:0.1.0"), "dummy")
            )
            assert behaviour.nb_act_called > 0, "Act() wasn't called"
        finally:
            agent.stop()
            t.join()


def test_react():
    """Tests income messages."""
    with LocalNode() as node:
        agent_name = "MyAgent"
        private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
        wallet = Wallet({"default": private_key_pem_path})
        ledger_apis = LedgerApis({}, "default")
        address = wallet.addresses["default"]
        connection = OEFLocalConnection(
            address, node, PublicId.from_string("fetchai/local:0.1.0")
        )
        connections = [connection]
        resources = Resources(str(Path(CUR_PATH, "data", "dummy_aea")))

        msg = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
        msg.counterparty = address
        message_bytes = DefaultSerializer().encode(msg)

        envelope = Envelope(
            to=address,
            sender=address,
            protocol_id="fetchai/default:0.1.0",
            message=message_bytes,
        )

        agent = AEA(
            agent_name, connections, wallet, ledger_apis, resources, programmatic=False
        )
        t = Thread(target=agent.start)
        try:
            t.start()
            time.sleep(1.0)
            agent.outbox.put(envelope)
            time.sleep(2.0)
            default_protocol_public_id = PublicId.from_string("fetchai/default:0.1.0")
            dummy_skill_public_id = PublicId.from_string("dummy_author/dummy:0.1.0")
            handler = agent.resources.handler_registry.fetch_by_protocol_and_skill(
                default_protocol_public_id, dummy_skill_public_id
            )
            assert handler is not None, "Handler is not set."
            assert (
                msg in handler.handled_messages
            ), "The message is not inside the handled_messages."
        except Exception:
            raise
        finally:
            agent.stop()
            t.join()


@pytest.mark.asyncio
async def test_handle():
    """Tests handle method of an agent."""
    with LocalNode() as node:
        agent_name = "MyAgent"
        private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
        wallet = Wallet({"default": private_key_pem_path})
        ledger_apis = LedgerApis({}, "default")
        address = wallet.addresses["default"]
        connection = OEFLocalConnection(
            address, node, connection_id=PublicId("fetchai", "local", "0.1.0")
        )
        connections = [connection]
        resources = Resources(str(Path(CUR_PATH, "data", "dummy_aea")))

        msg = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
        msg.counterparty = agent_name
        message_bytes = DefaultSerializer().encode(msg)

        envelope = Envelope(
            to=address,
            sender=address,
            protocol_id=PublicId.from_string("unknown_author/unknown_protocol:0.1.0"),
            message=message_bytes,
        )

        agent = AEA(
            agent_name, connections, wallet, ledger_apis, resources, programmatic=False
        )
        t = Thread(target=agent.start)
        try:
            t.start()
            time.sleep(2.0)
            dummy_skill = agent.resources.get_skill(
                PublicId.from_string("dummy_author/dummy:0.1.0")
            )
            dummy_handler = dummy_skill.handlers["dummy"]

            expected_envelope = envelope
            agent.outbox.put(expected_envelope)
            time.sleep(2.0)
            assert len(dummy_handler.handled_messages) == 1

            #   DECODING ERROR
            msg = "hello".encode("utf-8")
            envelope = Envelope(
                to=address,
                sender=address,
                protocol_id=DefaultMessage.protocol_id,
                message=msg,
            )
            expected_envelope = envelope
            agent.outbox.put(expected_envelope)
            time.sleep(2.0)
            assert len(dummy_handler.handled_messages) == 2

            #   UNSUPPORTED SKILL
            msg = FIPASerializer().encode(
                FIPAMessage(
                    performative=FIPAMessage.Performative.ACCEPT,
                    message_id=0,
                    dialogue_reference=(str(0), ""),
                    target=1,
                )
            )
            envelope = Envelope(
                to=address,
                sender=address,
                protocol_id=FIPAMessage.protocol_id,
                message=msg,
            )
            expected_envelope = envelope
            agent.outbox.put(expected_envelope)
            time.sleep(2.0)
            assert len(dummy_handler.handled_messages) == 3

        finally:
            agent.stop()
            t.join()


class TestInitializeAEAProgrammaticallyFromResourcesDir:
    """Test that we can initialize the agent by providing the resource object loaded from dir."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.node = LocalNode()
        cls.node.start()
        cls.agent_name = "MyAgent"
        cls.private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
        cls.wallet = Wallet({DEFAULT: cls.private_key_pem_path})
        cls.ledger_apis = LedgerApis({}, DEFAULT)
        cls.connection = OEFLocalConnection(
            cls.agent_name,
            cls.node,
            connection_id=PublicId("fetchai", "local", "0.1.0"),
        )
        cls.connections = [cls.connection]

        cls.resources = Resources(os.path.join(CUR_PATH, "data", "dummy_aea"))
        cls.aea = AEA(
            cls.agent_name,
            cls.connections,
            cls.wallet,
            cls.ledger_apis,
            cls.resources,
            programmatic=False,
        )

        cls.expected_message = DefaultMessage(
            type=DefaultMessage.Type.BYTES, content=b"hello"
        )
        cls.expected_message.counterparty = cls.agent_name
        envelope = Envelope(
            to=cls.agent_name,
            sender=cls.agent_name,
            protocol_id="fetchai/default:0.1.0",
            message=DefaultSerializer().encode(cls.expected_message),
        )

        cls.t = Thread(target=cls.aea.start)
        cls.t.start()

        time.sleep(0.5)
        cls.aea.outbox.put(envelope)
        time.sleep(0.5)

    def test_initialize_aea_programmatically(self):
        """Test that we can initialize an AEA programmatically."""
        dummy_skill_id = PublicId("dummy_author", "dummy", "0.1.0")
        dummy_behaviour_name = "dummy"
        dummy_behaviour = self.aea.resources.behaviour_registry.fetch(
            (dummy_skill_id, dummy_behaviour_name)
        )
        assert dummy_behaviour is not None
        assert dummy_behaviour.nb_act_called > 0

        dummy_task_name = "dummy"
        dummy_task = self.aea.resources.task_registry.fetch(
            (dummy_skill_id, dummy_task_name)
        )
        assert dummy_task is not None
        assert dummy_task.nb_execute_called > 0

        dummy_handler = self.aea.resources.handler_registry.fetch_by_protocol_and_skill(
            PublicId("fetchai", "default", "0.1.0"), dummy_skill_id
        )
        dummy_handler_alt = self.aea.resources.handler_registry.fetch(
            (dummy_skill_id, "dummy")
        )
        assert dummy_handler == dummy_handler_alt
        assert dummy_handler is not None
        assert len(dummy_handler.handled_messages) == 1
        assert dummy_handler.handled_messages[0] == self.expected_message

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        cls.aea.stop()
        cls.t.join()
        cls.node.stop()


class TestInitializeAEAProgrammaticallyBuildResources:
    """Test that we can initialize the agent by building the resource object."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.node = LocalNode()
        cls.node.start()
        cls.agent_name = "MyAgent"
        cls.private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
        cls.wallet = Wallet({"default": cls.private_key_pem_path})
        cls.ledger_apis = LedgerApis({}, "default")
        cls.connection = OEFLocalConnection(
            cls.agent_name, cls.node, PublicId("fetchai", "local", "0.1.0")
        )
        cls.connections = [cls.connection]

        cls.temp = tempfile.mkdtemp(prefix="test_aea_resources")
        cls.resources = Resources(cls.temp)
        cls.aea = AEA(
            cls.agent_name,
            cls.connections,
            cls.wallet,
            cls.ledger_apis,
            resources=cls.resources,
        )

        default_protocol_id = DefaultMessage.protocol_id

        cls.default_protocol_configuration = ProtocolConfig.from_json(
            yaml.safe_load(open(Path(AEA_DIR, "protocols", "default", "protocol.yaml")))
        )
        cls.default_protocol = Protocol(
            default_protocol_id, DefaultSerializer(), cls.default_protocol_configuration
        )
        cls.resources.protocol_registry.register(
            default_protocol_id, cls.default_protocol
        )

        cls.error_skill = Skill.from_dir(
            Path(AEA_DIR, "skills", "error"), cls.aea.context
        )
        cls.dummy_skill = Skill.from_dir(
            Path(CUR_PATH, "data", "dummy_skill"), cls.aea.context
        )
        cls.resources.add_skill(cls.dummy_skill)
        cls.resources.add_skill(cls.error_skill)

        cls.expected_message = DefaultMessage(
            type=DefaultMessage.Type.BYTES, content=b"hello"
        )
        cls.expected_message.counterparty = cls.agent_name

        cls.t = Thread(target=cls.aea.start)
        cls.t.start()
        time.sleep(0.5)

        cls.aea.outbox.put(
            Envelope(
                to=cls.agent_name,
                sender=cls.agent_name,
                protocol_id=default_protocol_id,
                message=DefaultSerializer().encode(cls.expected_message),
            )
        )

    def test_initialize_aea_programmatically(self):
        """Test that we can initialize an AEA programmatically."""
        time.sleep(0.5)

        dummy_skill_id = PublicId("dummy_author", "dummy", "0.1.0")
        dummy_behaviour_name = "dummy"
        dummy_behaviour = self.aea.resources.behaviour_registry.fetch(
            (dummy_skill_id, dummy_behaviour_name)
        )
        assert dummy_behaviour is not None
        assert dummy_behaviour.nb_act_called > 0

        dummy_task_name = "dummy"
        dummy_task = self.aea.resources.task_registry.fetch(
            (dummy_skill_id, dummy_task_name)
        )
        assert dummy_task is not None
        assert dummy_task.nb_execute_called > 0

        dummy_handler_name = "dummy"
        dummy_handler = self.aea.resources.handler_registry.fetch(
            (dummy_skill_id, dummy_handler_name)
        )
        dummy_handler_alt = self.aea.resources.handler_registry.fetch_by_protocol_and_skill(
            PublicId("fetchai", "default", "0.1.0"), dummy_skill_id
        )
        assert dummy_handler == dummy_handler_alt
        assert dummy_handler is not None
        assert len(dummy_handler.handled_messages) == 1
        assert dummy_handler.handled_messages[0] == self.expected_message

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        cls.aea.stop()
        cls.t.join()
        cls.node.stop()
        Path(cls.temp).rmdir()
