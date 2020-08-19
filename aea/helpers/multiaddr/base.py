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

import base58

import multihash

from binascii import unhexlify

from aea.crypto.base import Crypto

from .crypto_pb2 import KeyType, PublicKey

# NOTE: Implementation inspired from https://github.com/libp2p/py-libp2p
# NOTE: On inlining...
# See: https://github.com/libp2p/specs/issues/138
# NOTE: enabling to be interoperable w/ the Go implementation

ENABLE_INLINING = True
MAX_INLINE_KEY_LENGTH = 42
IDENTITY_MULTIHASH_CODE = 0x00

KEY_SIZE = 32
ZERO = b"\x00"

if ENABLE_INLINING:

    class IdentityHash:
        _digest: bytes

        def __init__(self) -> None:
            self._digest = bytearray()

        def update(self, input: bytes) -> None:
            self._digest += input

        def digest(self) -> bytes:
            return self._digest

    multihash.FuncReg.register(
        IDENTITY_MULTIHASH_CODE, "identity", hash_new=lambda: IdentityHash()
    )


def _pad_scalar(scalar):
    return (ZERO * (KEY_SIZE - len(scalar))) + scalar


def _pad_hex(hexed):
    # Pad odd-length hex strings.
    return hexed if not len(hexed) & 1 else "0" + hexed


def _hex_to_bytes(hexed):
    return _pad_scalar(unhexlify(_pad_hex(hexed)))


class MultiAddr:
    def __init__(self, host: str, port: int, key: Crypto):
        self._host = host
        self._port = port
        self._key = key
        self._peerid = self._compute_peerid()

    def _compute_peerid(self) -> str:
        key_protobuf = PublicKey(
            key_type=KeyType.Secp256k1, data=_hex_to_bytes(self._key.public_key)  # type: ignore
        )
        key_serialized = key_protobuf.SerializeToString()
        algo = multihash.Func.sha2_256
        if ENABLE_INLINING and len(key_serialized) <= MAX_INLINE_KEY_LENGTH:
            algo = IDENTITY_MULTIHASH_CODE
        key_mh = multihash.digest(key_serialized, algo)
        return base58.b58encode(key_mh.encode()).decode()

    def to_string(self) -> str:
        return "/dns/" + self._host + "/tcp/" + str(self._port) + "/p2p/" + self._peerid

    def __str__(self) -> str:
        return self.to_string()
