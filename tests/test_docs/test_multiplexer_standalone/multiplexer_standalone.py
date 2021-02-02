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

"""This module contains the full script from the multiplexer-standalone.md file."""

import os
import time
from copy import copy
from threading import Thread
from typing import Optional

from aea.configurations.base import ConnectionConfig
from aea.helpers.file_io import write_with_lock
from aea.identity.base import Identity
from aea.mail.base import Envelope
from aea.multiplexer import Multiplexer

from packages.fetchai.connections.stub.connection import StubConnection
from packages.fetchai.protocols.default.message import DefaultMessage


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def run():
    """Run demo."""

    # Ensure the input and output files do not exist initially
    if os.path.isfile(INPUT_FILE):
        os.remove(INPUT_FILE)
    if os.path.isfile(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    # create the connection and multiplexer objects
    configuration = ConnectionConfig(
        input_file=INPUT_FILE,
        output_file=OUTPUT_FILE,
        connection_id=StubConnection.connection_id,
    )
    stub_connection = StubConnection(
        configuration=configuration, identity=Identity("some_agent", "some_address")
    )
    multiplexer = Multiplexer([stub_connection], protocols=[DefaultMessage])
    try:
        # Set the multiplexer running in a different thread
        t = Thread(target=multiplexer.connect)
        t.start()

        # Wait for everything to start up
        time.sleep(3)

        # Create a message inside an envelope and get the stub connection to pass it into the multiplexer
        message_text = (
            "multiplexer,some_agent,fetchai/default:0.1.0,\x08\x01*\x07\n\x05hello,"
        )
        with open(INPUT_FILE, "w") as f:
            write_with_lock(f, message_text)

        # Wait for the envelope to get processed
        time.sleep(2)

        # get the envelope
        envelope = multiplexer.get()  # type: Optional[Envelope]
        assert envelope is not None

        # Inspect its contents
        print(
            "Envelope received by Multiplexer: sender={}, to={}, protocol_specification_id={}, message={}".format(
                envelope.sender,
                envelope.to,
                envelope.protocol_specification_id,
                envelope.message,
            )
        )

        # Create a mirrored response envelope
        response_envelope = copy(envelope)
        response_envelope.to = envelope.sender
        response_envelope.sender = envelope.to

        # Send the envelope back
        multiplexer.put(response_envelope)

        # Read the output envelope generated by the multiplexer
        with open(OUTPUT_FILE, "r") as f:
            print("Envelope received from Multiplexer: " + f.readline())
    finally:
        # Shut down the multiplexer
        multiplexer.disconnect()
        t.join()


if __name__ == "__main__":
    run()
