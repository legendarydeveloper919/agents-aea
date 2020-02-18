import os
import time
from threading import Thread

import yaml

from aea import AEA_DIR
from aea.aea import AEA
from aea.configurations.base import ProtocolConfig, PublicId
from aea.connections.stub.connection import StubConnection
from aea.crypto.fetchai import FETCHAI
from aea.crypto.helpers import FETCHAI_PRIVATE_KEY_FILE, _create_fetchai_private_key
from aea.crypto.ledger_apis import LedgerApis
from aea.crypto.wallet import Wallet
from aea.identity.base import Identity
from aea.protocols.base import Protocol
from aea.protocols.default.serialization import DefaultSerializer
from aea.registries.base import Resources
from aea.skills.base import Skill

ROOT_DIR = "./"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def run():
    # Create a private key
    _create_fetchai_private_key()

    # Ensure the input and output files do not exist initially
    if os.path.isfile(INPUT_FILE):
        os.remove(INPUT_FILE)
    if os.path.isfile(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    # Set up the Wallet, stub connection, ledger and (empty) resources
    wallet = Wallet({FETCHAI: FETCHAI_PRIVATE_KEY_FILE})
    stub_connection = StubConnection(
        input_file_path=INPUT_FILE, output_file_path=OUTPUT_FILE
    )
    ledger_apis = LedgerApis({"fetchai": {"network": "testnet"}}, "fetchai")
    resources = Resources()
    # Create an identity
    identity = Identity(
        name="my_aea",
        address=wallet.addresses.get(FETCHAI),
        default_address_key=FETCHAI,
    )

    # Create our AEA
    my_aea = AEA(identity, [stub_connection], wallet, ledger_apis, resources)

    # Add the default protocol (which is part of the AEA distribution)
    default_protocol_configuration = ProtocolConfig.from_json(
        yaml.safe_load(
            open(os.path.join(AEA_DIR, "protocols", "default", "protocol.yaml"))
        )
    )
    default_protocol = Protocol(
        PublicId.from_str("fetchai/default:0.1.0"),
        DefaultSerializer(),
        default_protocol_configuration,
    )
    resources.protocol_registry.register(
        PublicId.from_str("fetchai/default:0.1.0"), default_protocol
    )

    # Add the error skill (from the local packages dir) and the echo skill (which is part of the AEA distribution)
    echo_skill = Skill.from_dir(
        os.path.join(ROOT_DIR, "packages", "fetchai", "skills", "echo"), my_aea.context,
    )
    resources.add_skill(echo_skill)
    error_skill = Skill.from_dir(
        os.path.join(AEA_DIR, "skills", "error"), my_aea.context
    )
    resources.add_skill(error_skill)

    # Set the AEA running in a different thread
    t = Thread(target=my_aea.start)
    t.start()

    # Wait for everything to start up
    time.sleep(4)

    # Create a message inside an envelope and get the stub connection to pass it on to the echo skill
    message_text = 'my_aea,other_agent,fetchai/default:0.1.0,{"type": "bytes", "content": "aGVsbG8="}'
    with open(INPUT_FILE, "w") as f:
        f.write(message_text)
        print("input message: " + message_text)

    # Wait for the envelope to get processed
    time.sleep(4)

    # Read the output envelope generated by the echo skill
    with open(OUTPUT_FILE, "r") as f:
        print("output message: " + f.readline())

    # Shut down the AEA
    my_aea.stop()
    t.join()
    t = None


if __name__ == "__main__":
    run()
