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

"""This test module contains the tests for the `aea add protocol` sub-command."""
import os
import shutil
import tempfile
import unittest.mock
from pathlib import Path

from click.testing import CliRunner
from jsonschema import ValidationError

import aea
import aea.cli.common
import aea.configurations.base
from aea.cli import cli
from tests.conftest import CLI_LOG_OPTION


class TestAddProtocolFailsWhenProtocolAlreadyExists:
    """Test that the command 'aea add protocol' fails when the protocol already exists."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.protocol_name = "oef"
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name])
        assert result.exit_code == 0
        os.chdir(cls.agent_name)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "add", "protocol", cls.protocol_name])
        assert result.exit_code == 0
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "add", "protocol", cls.protocol_name])

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_error_message_protocol_already_existing(self):
        """Test that the log error message is fixed.

        The expected message is: 'A protocol with name '{protocol_name}' already exists. Aborting...'
        """
        s = "A protocol with name '{}' already exists. Aborting...".format(self.protocol_name)
        self.mocked_logger_error.assert_called_once_with(s)

    @classmethod
    def teardown_class(cls):
        """Teardowm the test."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestAddProtocolFailsWhenProtocolNotInRegistry:
    """Test that the command 'aea add protocol' fails when the protocol is not in the registry."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.protocol_name = "unknown_protocol"
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name])
        assert result.exit_code == 0
        os.chdir(cls.agent_name)
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "add", "protocol", cls.protocol_name])

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_error_message_protocol_already_existing(self):
        """Test that the log error message is fixed.

        The expected message is: 'Cannot find protocol: '{protocol_name}''
        """
        s = "Cannot find protocol: '{}'.".format(self.protocol_name)
        self.mocked_logger_error.assert_called_once_with(s)

    @classmethod
    def teardown_class(cls):
        """Teardowm the test."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestAddProtocolFailsWhenConfigFileIsNotCompliant:
    """Test that the command 'aea add protocol' fails when the configuration file is not compliant with the schema."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.protocol_name = "oef"
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name])
        assert result.exit_code == 0

        # change the serialization of the ProtocolConfig class so to make the parsing to fail.
        cls.patch = unittest.mock.patch.object(aea.configurations.base.ProtocolConfig, "from_json",
                                               side_effect=ValidationError("test error message"))
        cls.patch.__enter__()

        os.chdir(cls.agent_name)
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "add", "protocol", cls.protocol_name])

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_configuration_file_not_valid(self):
        """Test that the log error message is fixed.

        The expected message is: 'Protocol configuration file not valid: ...'
        """
        self.mocked_logger_error.assert_called_once_with("Protocol configuration file not valid: test error message")

    @classmethod
    def teardown_class(cls):
        """Teardowm the test."""
        cls.patch.__exit__()
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestAddProtocolFailsWhenDirectoryAlreadyExists:
    """Test that the command 'aea add protocol' fails when the destination directory already exists."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.protocol_name = "oef"
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name])
        assert result.exit_code == 0

        os.chdir(cls.agent_name)
        Path("protocols", cls.protocol_name).mkdir(parents=True, exist_ok=True)
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "add", "protocol", cls.protocol_name])

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_file_exists_error(self):
        """Test that the log error message is fixed.

        The expected message is: 'Cannot find protocol: '{protocol_name}''
        """
        s = "[Errno 17] File exists: './protocols/{}'".format(self.protocol_name)
        self.mocked_logger_error.assert_called_once_with(s)

    @classmethod
    def teardown_class(cls):
        """Teardowm the test."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass
