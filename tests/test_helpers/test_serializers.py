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
"""This module contains the tests for the helpers/serializers module."""
from aea.helpers.serializers import DictProtobufStructSerializer


def test_encode_decode_i():
    """Test encode decode logic."""
    case = {
        "bool_true": True,
        "bool_False": False,
        "none": None,
        "float": 0.12,
        "int": 100,
        "str": "some string",
        "bytes": b"some bytes string",
        "empty dict": {},
        "list_of_bytes": [b"1234", b"234234"],
        "list_of_ints": [1, 2, 3],
        "list_of_str": ["1234", "234234"],
        "list_of_floats": [1.1, 2.2, 3.0],
        "nested_dict": {"a": b"test", "b": 10, "c": [b"1", b"2"]},
    }
    encoded = DictProtobufStructSerializer.encode(case)
    assert isinstance(encoded, bytes)
    decoded = DictProtobufStructSerializer.decode(encoded)
    assert case == decoded


def test_encode_dict_is_deterministic():
    """Check DictProtobufStructSerializer.encode result is the same for the same input data."""
    data = dict(c=3, b=2, a=1)
    assert DictProtobufStructSerializer.encode(
        data
    ) == DictProtobufStructSerializer.encode(data)
