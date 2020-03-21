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
import aea.aea_builder
from pathlib import Path
from aea.aea_builder import AEABuilder
from aea.configurations.base import ComponentId
from aea.configurations.base import PublicId
from aea.crypto.fetchai import FetchAICrypto
import logging

"""Example of programmatic initialization of an AEA using the builder."""

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    builder = AEABuilder()

    builder.set_name("myagent")
    builder.add_address("fetchai", FetchAICrypto().address)
    builder.add_protocol("./packages/fetchai/protocols/oef")
    builder.add_skill("./packages/fetchai/skills/echo")

    # you can also use the fluent interface
    # builder.add_protocol(...).add_skill(...)

    aea_agent = builder.build()
    aea_agent.start()
