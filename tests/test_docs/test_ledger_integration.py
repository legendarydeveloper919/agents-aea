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

"""This module contains the tests for the content of ledger-integration.md file."""
from importlib import import_module
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock

from aea.crypto import FetchAICrypto
from aea.crypto.fetchai import FetchAIFaucetApi

from tests.conftest import ROOT_DIR
from tests.test_docs.helper import BasePythonMarkdownDocs


def _import_module_mock(arg):
    """
    Mock importlib.import_module only if argument is a dummy one: 'some.dotted.path'.

    This choice is tight to the code examples in 'ledger-integration.md'.
    It helps to tests the cases in which the import path is not a fake one.
    """
    if arg.startswith("some.dotted.path"):
        return MagicMock()
    return import_module(arg)


# we mock only if the import is from dumyy import path like "some.dotted.path".
@mock.patch("importlib.import_module", side_effect=_import_module_mock)
class TestLedgerIntegration(BasePythonMarkdownDocs):
    """Test the ledger integration code snippets."""

    DOC_PATH = Path(ROOT_DIR, "docs", "ledger-integration.md")

    def _assert_isinstance(self, locals_key, cls, **locals_):
        """Assert that the member of 'locals' is an instance of a class."""
        assert locals_key in locals_
        obj = locals_[locals_key]
        assert isinstance(obj, cls)

    def _assert(self, *mocks, **locals_):
        """Assert code outputs."""
        self._assert_isinstance("fetchai_crypto", FetchAICrypto, **locals_)
        self._assert_isinstance("fetchai_faucet_api", FetchAIFaucetApi, **locals_)
        self._assert_isinstance("my_ledger_api", MagicMock, **locals_)
        self._assert_isinstance("my_faucet_api", MagicMock, **locals_)
