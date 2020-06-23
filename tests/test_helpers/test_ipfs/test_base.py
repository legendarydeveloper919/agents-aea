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

"""This module contains the tests for the ipfs helper module."""

import os

from aea.helpers.ipfs.base import IPFSHashOnly

from ...conftest import CUR_PATH

FILE_PATH = "__init__.py"


def test_get_hash():
    """Test get hash IPFSHashOnly."""
    ipfs_hash = IPFSHashOnly().get(file_path=os.path.join(CUR_PATH, FILE_PATH))
    assert ipfs_hash == "QmWeMu9JFPUcYdz4rwnWiJuQ6QForNFRsjBiN5PtmkEg4A"
