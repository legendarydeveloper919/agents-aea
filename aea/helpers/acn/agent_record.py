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

"""This module contains types and helpers for acn Proof-of-Representation."""

import base64
from hashlib import sha256
from typing import List

from ecdsa import SECP256k1, VerifyingKey

from aea.crypto.fetchai import FetchAIHelper

def recover_verify_keys_from_message(message: bytes, signature: str) -> List[str]:
    """ get the public key used to produce the `signature` of the `message`"""
    signature_b64 = base64.b64decode(signature)
    verifying_keys = VerifyingKey.from_public_key_recovery(
        signature_b64, message, SECP256k1, hashfunc=sha256,
    )
    public_keys = [
        verifying_key.to_string("compressed").hex()
        for verifying_key in verifying_keys
    ]
    return public_keys

class AgentRecord:
    """Agent Proof-of-Representation to peer"""

    def __init__(
        self,
        address: str,
        public_key: str,
        peer_public_key: str,
        signature: str,
        service_id: str,
    ):
        """Initialize the AgentRecord"""
        self._service_id = service_id
        self._address = address
        self._public_key = public_key
        self._peer_public_key = peer_public_key
        self._signature = signature

    @property
    def address(self) -> str:
        """Get agent address"""
        return self._address

    @property
    def public_key(self) -> str:
        """Get agent public key"""
        return self._public_key

    @property
    def peer_public_key(self) -> str:
        """Get agent's representative peer public key"""
        return self._peer_public_key

    @property
    def signature(self) -> str:
        """Get record signature"""
        return self._signature

    @property
    def service_id(self) -> str:
        """Get record service id"""
        return self._service_id

    def __str__(self):
        """Get string representation."""
        return f"(address={self.address}, public_key={self.public_key}, peer_public_key={self.peer_public_key}, signature={self.signature})"

    def is_valid_for(self, address: str, peer_public_key: str) -> bool:
        """
        Check if the agent record is valid for `address` and `peer_public_key`

        :param address: the expected agent address concerned by the record
        :param peer_public_key: the expected representative peer public key
        :return: True if record is valid
        """

        if self._address != address:
            print("Wrong address")
            return False
        if self._peer_public_key != peer_public_key:
            print("Wrong peer public key")
            return False
        if self._address != FetchAIHelper.get_address_from_public_key(self._public_key):
            print(f"Wrong address '{self._address}' and public key '{FetchAIHelper.get_address_from_public_key(self._public_key)}'")
            return False
        if self._address not in FetchAIHelper.recover_message(
            self._peer_public_key.encode("utf-8"), self._signature
        ):
            print("Wrong signature")
            return False
        return True
