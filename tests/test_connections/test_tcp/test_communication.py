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

"""This module contains the tests for the TCP connection communication."""
import asyncio
import struct
import unittest.mock
from asyncio import CancelledError

import aea
import pytest

from aea.configurations.base import ConnectionConfig
from aea.connections.tcp.tcp_client import TCPClientConnection
from aea.connections.tcp.tcp_server import TCPServerConnection
from aea.mail.base import MailBox, Envelope
from aea.protocols.default.message import DefaultMessage
from aea.protocols.default.serialization import DefaultSerializer


class TestTCPCommunication:
    """Test that TCP Server and TCP Client can communicate."""

    @classmethod
    def setup_class(cls):
        """Set up the test class."""
        cls.host = "127.0.0.1"
        cls.port = 8082

        cls.server_pbk = "server_pbk"
        cls.client_pbk_1 = "client_pbk_1"
        cls.client_pbk_2 = "client_pbk_2"

        cls.server_conn = TCPServerConnection(cls.server_pbk, cls.host, cls.port)
        cls.client_conn_1 = TCPClientConnection(cls.client_pbk_1, cls.host, cls.port)
        cls.client_conn_2 = TCPClientConnection(cls.client_pbk_2, cls.host, cls.port)

        cls.server_mailbox = MailBox([cls.server_conn])
        cls.client_1_mailbox = MailBox([cls.client_conn_1])
        cls.client_2_mailbox = MailBox([cls.client_conn_2])

        assert not cls.server_conn.connection_status.is_connected
        assert not cls.client_conn_1.connection_status.is_connected
        assert not cls.client_conn_2.connection_status.is_connected

        cls.server_mailbox.connect()
        cls.client_1_mailbox.connect()
        cls.client_2_mailbox.connect()

    def test_is_connected(self):
        """Test that the connection status are connected."""
        assert self.server_conn.connection_status.is_connected
        assert self.client_conn_1.connection_status.is_connected
        assert self.client_conn_2.connection_status.is_connected

    def test_communication_client_server(self):
        """Test that envelopes can be sent from a client to a server."""
        msg = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
        msg_bytes = DefaultSerializer().encode(msg)
        expected_envelope = Envelope(to=self.server_pbk, sender=self.client_pbk_1, protocol_id=DefaultMessage.protocol_id, message=msg_bytes)
        self.client_1_mailbox.outbox.put(expected_envelope)
        actual_envelope = self.server_mailbox.inbox.get(block=True, timeout=5.0)

        assert expected_envelope == actual_envelope

    def test_communication_server_client(self):
        """Test that envelopes can be sent from a server to a client."""
        msg = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
        msg_bytes = DefaultSerializer().encode(msg)

        expected_envelope = Envelope(to=self.client_pbk_1, sender=self.server_pbk, protocol_id=DefaultMessage.protocol_id, message=msg_bytes)
        self.server_mailbox.outbox.put(expected_envelope)
        actual_envelope = self.client_1_mailbox.inbox.get(block=True, timeout=5.0)

        assert expected_envelope == actual_envelope

        expected_envelope = Envelope(to=self.client_pbk_2, sender=self.server_pbk, protocol_id=DefaultMessage.protocol_id, message=msg_bytes)
        self.server_mailbox.outbox.put(expected_envelope)
        actual_envelope = self.client_2_mailbox.inbox.get(block=True, timeout=5.0)

        assert expected_envelope == actual_envelope

    @classmethod
    def teardown_class(cls):
        """Tear down the test class."""
        cls.server_mailbox.disconnect()
        cls.client_1_mailbox.disconnect()
        cls.client_2_mailbox.disconnect()


class TestTCPClientConnection:
    """Test TCP Client code."""

    @pytest.mark.asyncio
    async def test_receive_cancelled(self):
        """Test that cancelling a receive task works correctly."""
        tcp_server = TCPServerConnection("public_key_server", "127.0.0.1", 8082)
        tcp_client = TCPClientConnection("public_key_client", "127.0.0.1", 8082)

        await tcp_server.connect()
        await tcp_client.connect()

        with unittest.mock.patch.object(aea.connections.tcp.tcp_client.logger, "debug") as mock_logger_debug:
            task = asyncio.ensure_future(tcp_client.recv())
            await asyncio.sleep(0.1)
            task.cancel()
            await asyncio.sleep(0.1)
            mock_logger_debug.assert_called_with("[{}] Read cancelled.".format("public_key_client"))
            assert task.result() is None

        await tcp_client.disconnect()
        await tcp_server.disconnect()

    @pytest.mark.asyncio
    async def test_receive_raises_struct_error(self):
        """Test the case when a receive raises a struct error."""
        tcp_server = TCPServerConnection("public_key_server", "127.0.0.1", 8082)
        tcp_client = TCPClientConnection("public_key_client", "127.0.0.1", 8082)

        await tcp_server.connect()
        await tcp_client.connect()

        with unittest.mock.patch.object(aea.connections.tcp.tcp_client.logger, "debug") as mock_logger_debug:
            with unittest.mock.patch.object(tcp_client, "_recv", side_effect=struct.error):
                task = asyncio.ensure_future(tcp_client.recv())
                await asyncio.sleep(0.1)
                mock_logger_debug.assert_called_with("Struct error: ")
                assert task.result() is None

        await tcp_client.disconnect()
        await tcp_server.disconnect()

    @pytest.mark.asyncio
    async def test_receive_raises_exception(self):
        """Test the case when a receive raises a generic exception."""
        tcp_server = TCPServerConnection("public_key_server", "127.0.0.1", 8082)
        tcp_client = TCPClientConnection("public_key_client", "127.0.0.1", 8082)

        await tcp_server.connect()
        await tcp_client.connect()

        with pytest.raises(Exception, match="generic exception"):
            with unittest.mock.patch.object(tcp_client, "_recv", side_effect=Exception("generic exception")):
                task = asyncio.ensure_future(tcp_client.recv())
                await asyncio.sleep(0.1)
                assert task.result() is None

        await tcp_client.disconnect()
        await tcp_server.disconnect()

    @pytest.mark.asyncio
    async def test_from_config(self):
        """Test the creation of the connection from a configuration."""
        TCPClientConnection.from_config("public_key", ConnectionConfig(host="127.0.0.1", port=8081))


class TestTCPServerConnection:
    """Test TCP Server code."""

    @pytest.mark.asyncio
    async def test_receive_raises_exception(self):
        """Test the case when a receive raises a generic exception."""
        tcp_server = TCPServerConnection("public_key_server", "127.0.0.1", 8082)
        tcp_client = TCPClientConnection("public_key_client", "127.0.0.1", 8082)

        await tcp_server.connect()
        await tcp_client.connect()
        await asyncio.sleep(0.1)
        with unittest.mock.patch.object(aea.connections.tcp.tcp_server.logger, "error") as mock_logger_error:
            with unittest.mock.patch("asyncio.wait", side_effect=Exception("generic exception")):
                result = await tcp_server.recv()
                assert result is None
                mock_logger_error.assert_called_with("Error in the receiving loop: generic exception")

        await tcp_client.disconnect()
        await tcp_server.disconnect()

    @pytest.mark.asyncio
    async def test_from_config(self):
        """Test the creation of the connection from a configuration."""
        TCPServerConnection.from_config("public_key", ConnectionConfig(host="127.0.0.1", port=8081))
