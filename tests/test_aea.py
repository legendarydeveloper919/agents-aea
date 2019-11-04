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
import time
from pathlib import Path
from threading import Thread

import yaml

from aea import AEA_DIR
from aea.aea import AEA
from aea.configurations.base import ProtocolConfig
from aea.connections.local.connection import LocalNode, OEFLocalConnection
from aea.crypto.ledger_apis import LedgerApis
from aea.crypto.wallet import Wallet
from aea.mail.base import MailBox, Envelope
from aea.protocols.base import Protocol
from aea.protocols.default.message import DefaultMessage
from aea.protocols.default.serialization import DefaultSerializer
from aea.protocols.fipa.message import FIPAMessage
from aea.protocols.fipa.serialization import FIPASerializer
from aea.registries.base import Resources
from aea.skills.base import Skill
from .conftest import CUR_PATH, DummyConnection


def test_initialise_AEA():
    """Tests the initialisation of the AEA."""
    node = LocalNode()
    public_key_1 = "mailbox1"
    mailbox1 = MailBox(OEFLocalConnection(public_key_1, node))
    private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
    wallet = Wallet({'default': private_key_pem_path})
    ledger_apis = LedgerApis({})
    my_AEA = AEA("Agent0", mailbox1, wallet, ledger_apis, directory=str(Path(CUR_PATH, "aea")))
    assert AEA("Agent0", mailbox1, wallet, ledger_apis), "Agent is not initialised"
    assert my_AEA.context == my_AEA._context, "Cannot access the Agent's Context"
    my_AEA.setup()
    assert my_AEA.resources is not None,\
        "Resources must not be None after setup"


def test_act():
    """Tests the act function of the AEA."""
    node = LocalNode()
    agent_name = "MyAgent"
    private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
    wallet = Wallet({'default': private_key_pem_path})
    ledger_apis = LedgerApis({})
    public_key = wallet.public_keys['default']
    mailbox = MailBox(OEFLocalConnection(public_key, node))

    agent = AEA(
        agent_name,
        mailbox,
        wallet,
        ledger_apis,
        directory=str(Path(CUR_PATH, "data", "dummy_aea")))
    t = Thread(target=agent.start)
    try:
        t.start()
        time.sleep(1)

        behaviour = agent.resources.behaviour_registry.fetch("dummy")
        assert behaviour[0].nb_act_called > 0, "Act() wasn't called"
    finally:
        agent.stop()
        t.join()


def test_react():
    """Tests income messages."""
    node = LocalNode()
    agent_name = "MyAgent"
    private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
    wallet = Wallet({'default': private_key_pem_path})
    ledger_apis = LedgerApis({})
    public_key = wallet.public_keys['default']
    mailbox = MailBox(OEFLocalConnection(public_key, node))

    msg = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
    message_bytes = DefaultSerializer().encode(msg)

    envelope = Envelope(
        to="Agent1",
        sender=public_key,
        protocol_id="default",
        message=message_bytes)

    agent = AEA(
        agent_name,
        mailbox,
        wallet,
        ledger_apis,
        directory=str(Path(CUR_PATH, "data", "dummy_aea")))
    t = Thread(target=agent.start)
    try:
        t.start()
        agent.mailbox.inbox._queue.put(envelope)
        time.sleep(1)
        handler = agent.resources \
            .handler_registry.fetch_by_skill('default', "dummy")
        assert msg in handler.handled_messages, \
            "The message is not inside the handled_messages."
    finally:
        agent.stop()
        t.join()


def test_handle():
    """Tests handle method of an agent."""
    agent_name = "MyAgent"
    private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
    wallet = Wallet({'default': private_key_pem_path})
    ledger_apis = LedgerApis({})
    public_key = wallet.public_keys['default']
    connection = DummyConnection()
    mailbox = MailBox(connection)

    msg = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
    message_bytes = DefaultSerializer().encode(msg)

    envelope = Envelope(
        to="Agent1",
        sender=public_key,
        protocol_id="unknown_protocol",
        message=message_bytes)

    agent = AEA(
        agent_name,
        mailbox,
        wallet,
        ledger_apis,
        directory=str(Path(CUR_PATH, "data", "dummy_aea")))
    t = Thread(target=agent.start)
    try:
        t.start()
        time.sleep(1.0)
        connection.in_queue.put(envelope)
        env = connection.out_queue.get(block=True, timeout=5.0)
        assert env.protocol_id == "default"

        #   DECODING ERROR
        msg = "hello".encode("utf-8")
        envelope = Envelope(
            to=public_key,
            sender=public_key,
            protocol_id='default',
            message=msg)
        connection.in_queue.put(envelope)
        env = connection.out_queue.get(block=True, timeout=5.0)
        assert env.protocol_id == "default"

        #   UNSUPPORTED SKILL
        msg = FIPASerializer().encode(
            FIPAMessage(performative=FIPAMessage.Performative.ACCEPT,
                        message_id=0,
                        dialogue_id=0,
                        destination=public_key,
                        target=1))
        envelope = Envelope(
            to=public_key,
            sender=public_key,
            protocol_id="fipa",
            message=msg)
        connection.in_queue.put(envelope)
        env = connection.out_queue.get(block=True, timeout=5.0)
        assert env.protocol_id == "default"

    finally:
        agent.stop()
        t.join()


class TestInitializeAEAProgrammaticallyFromResourcesDir:
    """Test that we can initialize the agent by providing the resource object loaded from dir."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.agent_name = "MyAgent"
        cls.private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
        cls.wallet = Wallet({'default': cls.private_key_pem_path})
        cls.ledger_apis = LedgerApis({})
        cls.connection = DummyConnection()
        cls.mailbox = MailBox(cls.connection)

        cls.aea = AEA(cls.agent_name, cls.mailbox, cls.wallet, cls.ledger_apis)
        cls.resources = Resources.from_resource_dir(os.path.join(CUR_PATH, "data", "dummy_aea"), cls.aea.context)
        cls.aea.resources = cls.resources

        cls.expected_message = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
        cls.connection.receive(Envelope(to="", sender="", protocol_id="default", message=DefaultSerializer().encode(cls.expected_message)))

        cls.t = Thread(target=cls.aea.start)
        cls.t.start()

    def test_initialize_aea_programmatically(self):
        """Test that we can initialize an AEA programmatically."""
        time.sleep(1.0)
        dummy_behaviour = self.aea.resources.behaviour_registry.fetch("dummy")[0]
        dummy_task = self.aea.resources.task_registry.fetch("dummy")[0]
        dummy_handler = self.aea.resources.handler_registry.fetch("default")[0]
        assert dummy_behaviour.nb_act_called > 0
        assert dummy_task.nb_execute_called > 0
        assert len(dummy_handler.handled_messages) == 1
        assert dummy_handler.handled_messages[0] == self.expected_message

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        cls.aea.stop()
        cls.t.join()


class TestInitializeAEAProgrammaticallyBuildResources:
    """Test that we can initialize the agent by building the resource object."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.agent_name = "MyAgent"
        cls.private_key_pem_path = os.path.join(CUR_PATH, "data", "priv.pem")
        cls.wallet = Wallet({'default': cls.private_key_pem_path})
        cls.ledger_apis = LedgerApis({})
        cls.connection = DummyConnection()
        cls.mailbox = MailBox(cls.connection)

        cls.resources = Resources()
        cls.aea = AEA(cls.agent_name, cls.mailbox, cls.wallet, cls.ledger_apis, resources=cls.resources)

        cls.default_protocol_configuration = ProtocolConfig.from_json(
            yaml.safe_load(open(Path(AEA_DIR, "protocols", "default", "protocol.yaml"))))
        cls.default_protocol = Protocol("default",
                                        DefaultSerializer(),
                                        cls.default_protocol_configuration)
        cls.resources.protocol_registry.register(("default", None), cls.default_protocol)

        cls.error_skill = Skill.from_dir(Path(AEA_DIR, "skills", "error"), cls.aea.context)
        cls.dummy_skill = Skill.from_dir(Path(CUR_PATH, "data", "dummy_skill"), cls.aea.context)
        cls.resources.add_skill(cls.dummy_skill)
        cls.resources.add_skill(cls.error_skill)

        cls.expected_message = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
        cls.connection.receive(Envelope(to="", sender="", protocol_id="default", message=DefaultSerializer().encode(cls.expected_message)))

        cls.t = Thread(target=cls.aea.start)
        cls.t.start()

    def test_initialize_aea_programmatically(self):
        """Test that we can initialize an AEA programmatically."""
        time.sleep(1.0)
        dummy_behaviour = self.aea.resources.behaviour_registry.fetch("dummy")[0]
        dummy_task = self.aea.resources.task_registry.fetch("dummy")[0]
        dummy_handler = self.aea.resources.handler_registry.fetch("default")[0]
        assert dummy_behaviour.nb_act_called > 0
        assert dummy_task.nb_execute_called > 0
        assert len(dummy_handler.handled_messages) == 1
        assert dummy_handler.handled_messages[0] == self.expected_message

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        cls.aea.stop()
        cls.t.join()
