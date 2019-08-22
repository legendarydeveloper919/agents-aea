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

"""This module contains the tests of the messages module."""

from aea.mail.base import Envelope
from aea.protocols.default.message import DefaultMessage
from aea.protocols.default.serialization import DefaultSerializer


def test_simple_bytes_serialization():
    """Test that the serialization for the 'simple' protocol works for the BYTES message."""
    msg = DefaultMessage(type=DefaultMessage.Type.BYTES, content=b"hello")
    msg_bytes = DefaultSerializer().encode(msg)
    envelope = Envelope(to="receiver", sender="sender", protocol_id="simple", message=msg_bytes)
    envelope_bytes = envelope.encode()

    actual_envelope = Envelope.decode(envelope_bytes)
    expected_envelope = envelope
    assert expected_envelope == actual_envelope

    actual_msg = DefaultSerializer().decode(actual_envelope.message)
    expected_msg = msg
    assert expected_msg == actual_msg


def test_simple_error_serialization():
    """Test that the serialization for the 'simple' protocol works for the ERROR message."""
    msg = DefaultMessage(type=DefaultMessage.Type.ERROR, error_code=-1, error_msg="An error")
    msg_bytes = DefaultSerializer().encode(msg)
    envelope = Envelope(to="receiver", sender="sender", protocol_id="simple", message=msg_bytes)
    envelope_bytes = envelope.encode()

    actual_envelope = Envelope.decode(envelope_bytes)
    expected_envelope = envelope
    assert expected_envelope == actual_envelope

    actual_msg = DefaultSerializer().decode(actual_envelope.message)
    expected_msg = msg
    assert expected_msg == actual_msg
