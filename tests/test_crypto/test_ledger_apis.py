
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

"""This module contains the tests for the crypto/helpers module."""
import logging
import subprocess

import os

import pytest

from aea.crypto.ethereum import ETHEREUM, EthereumCrypto
from aea.crypto.fetchai import FETCHAI, FetchAICrypto
from aea.crypto.ledger_apis import LedgerApis, DEFAULT_FETCHAI_CONFIG
from tests.conftest import CUR_PATH

logger = logging.getLogger(__name__)

DEFAULT_ETHEREUM_CONFIG = ("https://ropsten.infura.io/v3/f00f7b3ba0e848ddbdc8941c527447fe", 3)
fet_address = "B3t9pv4rYccWqCjeuoXsDoeXLiKxVAQh6Q3CLAiNZZQ2mtqF1"
eth_address = "0x21795D753752ccC1AC728002D23Ba33cbF13b8b0"

class TestLedgerApis:
    """Test the ledger_apis module."""

    def test_initialisation(self):
        """Test the initialisation of the ledger APIs."""
        ledger_apis = LedgerApis({ETHEREUM: DEFAULT_ETHEREUM_CONFIG})
        assert ledger_apis.configs.get(ETHEREUM) == DEFAULT_ETHEREUM_CONFIG

        unknown_config = ("UknownPath", 8080)
        with pytest.raises(ValueError):
            ledger_apis = LedgerApis({"UNKNOWN": unknown_config})

    def test_token_balance(self):
        """Test the token_balance for the different tokens."""
        ledger_apis = LedgerApis({ETHEREUM: DEFAULT_ETHEREUM_CONFIG,
                                  FETCHAI: DEFAULT_FETCHAI_CONFIG})

        balance = ledger_apis.token_balance(FETCHAI, eth_address)
        assert balance == 0
        balance = ledger_apis.token_balance(ETHEREUM, eth_address)
        assert balance != 0, "The specific address has some eth"
        balance = ledger_apis.token_balance(ETHEREUM, fet_address)
        assert balance == 0, "Should trigger the Exception and the balance will be 0"
        with pytest.raises(AssertionError):
            balance = ledger_apis.token_balance("UNKNOWN", fet_address)
            assert balance == 0, "Unknown identifier so it will return 0"

    def test_transfer(self):
        """Test the transfer function for the supported tokens."""
        private_key_path = os.path.join(CUR_PATH, "data", "eth_private_key.txt")
        eth_obj = EthereumCrypto(private_key_path=private_key_path)
        private_key_path = os.path.join(CUR_PATH, 'data', "fet_private_key.txt")
        fet_obj = FetchAICrypto(private_key_path=private_key_path)
        ledger_apis = LedgerApis({ETHEREUM: DEFAULT_ETHEREUM_CONFIG,
                                  FETCHAI: DEFAULT_FETCHAI_CONFIG})
        tx_digest =ledger_apis.transfer(FETCHAI, fet_obj, fet_address, amount=10, tx_fee=10)
        assert tx_digest is not None
        assert ledger_apis.is_tx_settled(identifier=FETCHAI, tx_digest=tx_digest)
        tx_digest = "unknown_hash"
        assert not ledger_apis.is_tx_settled(identifier=FETCHAI, tx_digest=tx_digest)

        tx_digest = ledger_apis.transfer(ETHEREUM, eth_obj, eth_address, amount=10, tx_fee=200000)
        assert tx_digest is not None
        assert ledger_apis.is_tx_settled(identifier=ETHEREUM, tx_digest=tx_digest)
        tx_digest = "unknown_hash"
        assert not ledger_apis.is_tx_settled(identifier=ETHEREUM, tx_digest=tx_digest)
        with pytest.raises(ValueError):
            tx_digest = ledger_apis.transfer(ETHEREUM, eth_obj, eth_address, amount=50, tx_fee=2)


