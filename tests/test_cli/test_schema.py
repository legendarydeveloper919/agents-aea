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

"""This test module contains the tests for the JSON schemas of the configuration files."""
import json
import os
import pprint

import pytest
import yaml
from jsonschema import validate, Draft7Validator  # type: ignore

from aea.configurations.base import DEFAULT_PROTOCOL_CONFIG_FILE, DEFAULT_CONNECTION_CONFIG_FILE, \
    DEFAULT_SKILL_CONFIG_FILE
from ..conftest import CUR_PATH, ROOT_DIR, AGENT_CONFIGURATION_SCHEMA, SKILL_CONFIGURATION_SCHEMA, \
    CONNECTION_CONFIGURATION_SCHEMA, PROTOCOL_CONFIGURATION_SCHEMA


def test_agent_configuration_schema_is_valid_wrt_draft_07():
    """Test that the JSON schema for the agent configuration file is compliant with the specification Draft 07."""
    agent_config_schema = json.load(open(os.path.join(ROOT_DIR, "aea", "configurations", "schemas", "aea-config_schema.json")))
    Draft7Validator.check_schema(agent_config_schema)


def test_skill_configuration_schema_is_valid_wrt_draft_07():
    """Test that the JSON schema for the skill configuration file is compliant with the specification Draft 07."""
    skill_config_schema = json.load(open(os.path.join(ROOT_DIR, "aea", "configurations", "schemas", "skill-config_schema.json")))
    Draft7Validator.check_schema(skill_config_schema)


def test_connection_configuration_schema_is_valid_wrt_draft_07():
    """Test that the JSON schema for the connection configuration file is compliant with the specification Draft 07."""
    connection_config_schema = json.load(open(os.path.join(ROOT_DIR, "aea", "configurations", "schemas", "connection-config_schema.json")))
    Draft7Validator.check_schema(connection_config_schema)


def test_validate_agent_config():
    """Test that the validation of the agent configuration file works correctly."""
    agent_config_schema = json.load(open(AGENT_CONFIGURATION_SCHEMA))
    agent_config_file = yaml.safe_load(open(os.path.join(CUR_PATH, "data", "aea-config.example.yaml")))
    pprint.pprint(agent_config_file)
    validate(instance=agent_config_file, schema=agent_config_schema)


def test_validate_skill_config():
    """Test that the validation of the skill configuration file works correctly."""
    skill_config_schema = json.load(open(SKILL_CONFIGURATION_SCHEMA))
    skill_config_file = yaml.safe_load(open(os.path.join(CUR_PATH, "data", "dummy_skill", "skill.yaml")))
    pprint.pprint(skill_config_file)
    validate(instance=skill_config_file, schema=skill_config_schema)


def test_validate_connection_config():
    """Test that the validation of the connection configuration file works correctly."""
    connection_config_schema = json.load(open(CONNECTION_CONFIGURATION_SCHEMA))
    connection_config_file = yaml.safe_load(open(os.path.join(CUR_PATH, "data", "dummy_connection", "connection.yaml")))
    pprint.pprint(connection_config_file)
    validate(instance=connection_config_file, schema=connection_config_schema)


class TestProtocolsSchema:
    """Test that the protocol configuration files provided by the framework are compliant to the schema."""

    @classmethod
    def setup_class(cls):
        """Set up the test class."""
        cls.protocol_config_schema = json.load(open(PROTOCOL_CONFIGURATION_SCHEMA))

    @pytest.mark.parametrize("protocol_path",
                             [
                                 os.path.join(ROOT_DIR, "aea", "protocols", "default"),
                                 os.path.join(ROOT_DIR, "aea", "protocols", "fipa"),
                                 os.path.join(ROOT_DIR, "aea", "protocols", "oef"),
                                 os.path.join(ROOT_DIR, "aea", "protocols", "scaffold"),
                                 os.path.join(ROOT_DIR, "packages", "protocols", "gym"),
                                 os.path.join(ROOT_DIR, "packages", "protocols", "tac"),
                             ])
    def test_validate_protocol_config(self, protocol_path):
        """Test that the validation of the protocol configuration file in aea/protocols works correctly."""
        protocol_config_file = yaml.safe_load(open(os.path.join(protocol_path, DEFAULT_PROTOCOL_CONFIG_FILE)))
        validate(instance=protocol_config_file, schema=self.protocol_config_schema)


class TestConnectionsSchema:
    """Test that the connection configuration files provided by the framework are compliant to the schema."""

    @classmethod
    def setup_class(cls):
        """Set up the test class."""
        cls.connection_config_schema = json.load(open(CONNECTION_CONFIGURATION_SCHEMA))

    @pytest.mark.parametrize("connection_path",
                             [
                                 os.path.join(ROOT_DIR, "aea", "connections", "local"),
                                 os.path.join(ROOT_DIR, "aea", "connections", "oef"),
                                 os.path.join(ROOT_DIR, "aea", "connections", "scaffold"),
                                 os.path.join(ROOT_DIR, "packages", "connections", "gym"),
                             ])
    def test_validate_protocol_config(self, connection_path):
        """Test that the validation of the protocol configuration file in aea/protocols works correctly."""
        connection_config_file = yaml.safe_load(open(os.path.join(connection_path, DEFAULT_CONNECTION_CONFIG_FILE)))
        validate(instance=connection_config_file, schema=self.connection_config_schema)


class TestSkillsSchema:
    """Test that the skill configuration files provided by the framework are compliant to the schema."""

    @classmethod
    def setup_class(cls):
        """Set up the test class."""
        cls.skill_config_schema = json.load(open(SKILL_CONFIGURATION_SCHEMA))

    @pytest.mark.parametrize("skill_path",
                             [
                                 os.path.join(ROOT_DIR, "aea", "skills", "error"),
                                 os.path.join(ROOT_DIR, "aea", "skills", "scaffold"),
                                 os.path.join(ROOT_DIR, "packages", "skills", "echo"),
                                 os.path.join(ROOT_DIR, "packages", "skills", "gym"),
                             ])
    def test_validate_protocol_config(self, skill_path):
        """Test that the validation of the protocol configuration file in aea/protocols works correctly."""
        skill_config_file = yaml.safe_load(open(os.path.join(skill_path, DEFAULT_SKILL_CONFIG_FILE)))
        validate(instance=skill_config_file, schema=self.skill_config_schema)
