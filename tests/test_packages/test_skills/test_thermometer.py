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
"""This test module contains the integration test for the thermometer skills."""
import pytest

from aea.test_tools.test_cases import AEATestCaseMany

from tests.conftest import (
    COSMOS,
    COSMOS_PRIVATE_KEY_FILE,
    FUNDED_COSMOS_PRIVATE_KEY_1,
    MAX_FLAKY_RERUNS,
    NON_FUNDED_COSMOS_PRIVATE_KEY_1,
    NON_GENESIS_CONFIG,
    wait_for_localhost_ports_to_close,
)


class TestThermometerSkill(AEATestCaseMany):
    """Test that thermometer skills work."""

    @pytest.mark.flaky(reruns=MAX_FLAKY_RERUNS)  # cause possible network issues
    def test_thermometer(self):
        """Run the thermometer skills sequence."""

        thermometer_aea_name = "my_thermometer"
        thermometer_client_aea_name = "my_thermometer_client"
        self.create_agents(thermometer_aea_name, thermometer_client_aea_name)

        default_routing = {
            "fetchai/ledger_api:0.1.0": "fetchai/ledger:0.2.0",
            "fetchai/oef_search:0.3.0": "fetchai/soef:0.5.0",
        }

        # add packages for agent one and run it
        self.set_agent_context(thermometer_aea_name)
        self.add_item("connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/soef:0.5.0")
        self.set_config("agent.default_connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/ledger:0.2.0")
        self.add_item("skill", "fetchai/thermometer:0.7.0")
        setting_path = (
            "vendor.fetchai.skills.thermometer.models.strategy.args.is_ledger_tx"
        )
        self.set_config(setting_path, False, "bool")
        setting_path = "agent.default_routing"
        self.force_set_config(setting_path, default_routing)
        self.run_install()

        # add non-funded key
        self.generate_private_key(COSMOS)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE, connection=True)
        self.replace_private_key_in_file(
            NON_FUNDED_COSMOS_PRIVATE_KEY_1, COSMOS_PRIVATE_KEY_FILE
        )

        # add packages for agent two and run it
        self.set_agent_context(thermometer_client_aea_name)
        self.add_item("connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/soef:0.5.0")
        self.set_config("agent.default_connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/ledger:0.2.0")
        self.add_item("skill", "fetchai/thermometer_client:0.6.0")
        setting_path = (
            "vendor.fetchai.skills.thermometer_client.models.strategy.args.is_ledger_tx"
        )
        self.set_config(setting_path, False, "bool")
        setting_path = "agent.default_routing"
        self.force_set_config(setting_path, default_routing)
        self.run_install()

        # add funded key
        self.generate_private_key(COSMOS)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE, connection=True)
        self.replace_private_key_in_file(
            FUNDED_COSMOS_PRIVATE_KEY_1, COSMOS_PRIVATE_KEY_FILE
        )
        setting_path = "vendor.fetchai.connections.p2p_libp2p.config"
        self.force_set_config(setting_path, NON_GENESIS_CONFIG)

        # run AEAs
        self.set_agent_context(thermometer_aea_name)
        thermometer_aea_process = self.run_agent()

        check_strings = (
            "Downloading golang dependencies. This may take a while...",
            "Finished downloading golang dependencies.",
            "Starting libp2p node...",
            "Connecting to libp2p node...",
            "Successfully connected to libp2p node!",
            "My libp2p addresses:",
        )
        missing_strings = self.missing_from_output(
            thermometer_aea_process, check_strings, timeout=240, is_terminating=False
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_aea output.".format(missing_strings)

        self.set_agent_context(thermometer_client_aea_name)
        thermometer_client_aea_process = self.run_agent()

        check_strings = (
            "Downloading golang dependencies. This may take a while...",
            "Finished downloading golang dependencies.",
            "Starting libp2p node...",
            "Connecting to libp2p node...",
            "Successfully connected to libp2p node!",
            "My libp2p addresses:",
        )
        missing_strings = self.missing_from_output(
            thermometer_client_aea_process,
            check_strings,
            timeout=240,
            is_terminating=False,
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_client_aea output.".format(
            missing_strings
        )

        check_strings = (
            "registering agent on SOEF.",
            "registering service on SOEF.",
            "received CFP from sender=",
            "sending a PROPOSE with proposal=",
            "received ACCEPT from sender=",
            "sending MATCH_ACCEPT_W_INFORM to sender=",
            "received INFORM from sender=",
            "transaction confirmed, sending data=",
        )
        missing_strings = self.missing_from_output(
            thermometer_aea_process, check_strings, is_terminating=False
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_aea output.".format(missing_strings)

        check_strings = (
            "found agents=",
            "sending CFP to agent=",
            "received proposal=",
            "accepting the proposal from sender=",
            "informing counterparty=",
            "received INFORM from sender=",
            "received the following data=",
        )
        missing_strings = self.missing_from_output(
            thermometer_client_aea_process, check_strings, is_terminating=False
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_client_aea output.".format(
            missing_strings
        )

        self.terminate_agents(thermometer_aea_process, thermometer_client_aea_process)
        assert (
            self.is_successfully_terminated()
        ), "Agents weren't successfully terminated."
        wait_for_localhost_ports_to_close([9000, 9001])


class TestThermometerSkillFetchaiLedger(AEATestCaseMany):
    """Test that thermometer skills work."""

    @pytest.mark.flaky(reruns=MAX_FLAKY_RERUNS)  # cause possible network issues
    def test_thermometer(self):
        """Run the thermometer skills sequence."""

        thermometer_aea_name = "my_thermometer"
        thermometer_client_aea_name = "my_thermometer_client"
        self.create_agents(thermometer_aea_name, thermometer_client_aea_name)

        default_routing = {
            "fetchai/ledger_api:0.1.0": "fetchai/ledger:0.2.0",
            "fetchai/oef_search:0.3.0": "fetchai/soef:0.5.0",
        }

        # add packages for agent one and run it
        self.set_agent_context(thermometer_aea_name)
        self.add_item("connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/soef:0.5.0")
        self.set_config("agent.default_connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/ledger:0.2.0")
        self.add_item("skill", "fetchai/thermometer:0.7.0")
        setting_path = "agent.default_routing"
        self.force_set_config(setting_path, default_routing)
        self.run_install()

        diff = self.difference_to_fetched_agent(
            "fetchai/thermometer_aea:0.6.0", thermometer_aea_name
        )
        assert (
            diff == []
        ), "Difference between created and fetched project for files={}".format(diff)

        # add non-funded key
        self.generate_private_key(COSMOS)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE, connection=True)
        self.replace_private_key_in_file(
            NON_FUNDED_COSMOS_PRIVATE_KEY_1, COSMOS_PRIVATE_KEY_FILE
        )

        # add packages for agent two and run it
        self.set_agent_context(thermometer_client_aea_name)
        self.add_item("connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/soef:0.5.0")
        self.set_config("agent.default_connection", "fetchai/p2p_libp2p:0.5.0")
        self.add_item("connection", "fetchai/ledger:0.2.0")
        self.add_item("skill", "fetchai/thermometer_client:0.6.0")
        setting_path = "agent.default_routing"
        self.force_set_config(setting_path, default_routing)
        self.run_install()

        diff = self.difference_to_fetched_agent(
            "fetchai/thermometer_client:0.6.0", thermometer_client_aea_name
        )
        assert (
            diff == []
        ), "Difference between created and fetched project for files={}".format(diff)

        # add funded key
        self.generate_private_key(COSMOS)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE)
        self.add_private_key(COSMOS, COSMOS_PRIVATE_KEY_FILE, connection=True)
        self.replace_private_key_in_file(
            FUNDED_COSMOS_PRIVATE_KEY_1, COSMOS_PRIVATE_KEY_FILE
        )
        setting_path = "vendor.fetchai.connections.p2p_libp2p.config"
        self.force_set_config(setting_path, NON_GENESIS_CONFIG)

        # run AEAs
        self.set_agent_context(thermometer_aea_name)
        thermometer_aea_process = self.run_agent()

        check_strings = (
            "Downloading golang dependencies. This may take a while...",
            "Finished downloading golang dependencies.",
            "Starting libp2p node...",
            "Connecting to libp2p node...",
            "Successfully connected to libp2p node!",
            "My libp2p addresses:",
        )
        missing_strings = self.missing_from_output(
            thermometer_aea_process, check_strings, timeout=240, is_terminating=False
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_aea output.".format(missing_strings)

        self.set_agent_context(thermometer_client_aea_name)
        thermometer_client_aea_process = self.run_agent()

        check_strings = (
            "Downloading golang dependencies. This may take a while...",
            "Finished downloading golang dependencies.",
            "Starting libp2p node...",
            "Connecting to libp2p node...",
            "Successfully connected to libp2p node!",
            "My libp2p addresses:",
        )
        missing_strings = self.missing_from_output(
            thermometer_client_aea_process,
            check_strings,
            timeout=240,
            is_terminating=False,
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_client_aea output.".format(
            missing_strings
        )

        check_strings = (
            "registering agent on SOEF.",
            "registering service on SOEF.",
            "received CFP from sender=",
            "sending a PROPOSE with proposal=",
            "received ACCEPT from sender=",
            "sending MATCH_ACCEPT_W_INFORM to sender=",
            "received INFORM from sender=",
            "checking whether transaction=",
            "transaction confirmed, sending data=",
        )
        missing_strings = self.missing_from_output(
            thermometer_aea_process, check_strings, timeout=240, is_terminating=False
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_aea output.".format(missing_strings)

        check_strings = (
            "found agents=",
            "sending CFP to agent=",
            "received proposal=",
            "accepting the proposal from sender=",
            "received MATCH_ACCEPT_W_INFORM from sender=",
            "requesting transfer transaction from ledger api...",
            "received raw transaction=",
            "proposing the transaction to the decision maker. Waiting for confirmation ...",
            "transaction signing was successful.",
            "sending transaction to ledger.",
            "transaction was successfully submitted. Transaction digest=",
            "informing counterparty=",
            "received INFORM from sender=",
            "received the following data=",
        )
        missing_strings = self.missing_from_output(
            thermometer_client_aea_process, check_strings, is_terminating=False
        )
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in thermometer_client_aea output.".format(
            missing_strings
        )

        self.terminate_agents(thermometer_aea_process, thermometer_client_aea_process)
        assert (
            self.is_successfully_terminated()
        ), "Agents weren't successfully terminated."
        wait_for_localhost_ports_to_close([9000, 9001])
