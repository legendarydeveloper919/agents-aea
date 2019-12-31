# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Abstract module wrapping the public and private key cryptography and ledger api."""
from abc import ABC, abstractmethod
from typing import Any, BinaryIO, Union, Optional

AddressLike = Union[str, bytes]


class Crypto(ABC):
    """Base class for a crypto object."""

    identifier = 'base'

    @property
    @abstractmethod
    def entity(self) -> Any:
        """
        Return an entity object.

        :return: an entity object
        """

    @property
    @abstractmethod
    def public_key(self) -> str:
        """
        Return a public key.

        :return: a public key string
        """

    @property
    @abstractmethod
    def address(self) -> str:
        """
        Return the address.

        :return: an address string
        """

    @classmethod
    @abstractmethod
    def get_address_from_public_key(cls, public_key: str) -> str:
        """
        Get the address from the public key.

        :param public_key: the public key
        :return: str
        """

    @classmethod
    @abstractmethod
    def load(cls, fp: BinaryIO) -> 'Crypto':
        """
        Deserialize binary file `fp` (a `.read()`-supporting file-like object containing a private key).

        :param fp: the input file pointer. Must be set in binary mode (mode='rb')
        :return: None
        """

    @abstractmethod
    def dump(self, fp: BinaryIO) -> None:
        """
        Serialize crypto object as binary stream to `fp` (a `.write()`-supporting file-like object).

        :param fp: the output file pointer. Must be set in binary mode (mode='wb')
        :return: None
        """


class LedgerApi(ABC):
    """Interface for ledger APIs."""

    identifier = None  # type: Optional[str]

    @abstractmethod
    def get_balance(self, address: AddressLike) -> int:
        """
        Get the balance of a given account.

        This usually takes the form of a web request to be waited synchronously.

        :param address: the address.
        :return: the balance.
        """

    @abstractmethod
    def send_transaction(self,
                         crypto_object: Crypto,
                         destination_address: AddressLike,
                         amount: int,
                         tx_fee: int
                         ) -> Optional[str]:
        """
        Submit a transaction to the ledger.

        :param crypto_object: the crypto object associated to the payer.
        :param destination_address: the destination address of the payee.
        :param amount: the amount of wealth to be transferred.
        :param tx_fee: the transaction fee.
        :return: the transaction digest, or None.
        """

    # TODO?
    # def get_transaction_receipt(self, tx_digest: str) -> Dict:

    @abstractmethod
    def is_transaction_settled(self, tx_digest: str) -> bool:
        """
        Check whether a transaction is settled or not.

        :param tx_digest: the digest associated to the transaction.
        :return: True if the transaction has been settled, False o/w.
        """
