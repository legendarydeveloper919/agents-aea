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

"""This test module contains the tests for the `aea scaffold skill` sub-command."""

import filecmp
import json
import os
import shutil
import tempfile
import unittest.mock
from pathlib import Path

import jsonschema
from jsonschema import Draft4Validator, ValidationError

import yaml

import aea.cli.common
import aea.configurations.base
from aea import AEA_DIR
from aea.cli import cli
from aea.configurations.base import DEFAULT_SKILL_CONFIG_FILE

from ...common.click_testing import CliRunner
from ...conftest import CLI_LOG_OPTION, CONFIGURATION_SCHEMA_DIR, SKILL_CONFIGURATION_SCHEMA


class TestScaffoldSkill:
    """Test that the command 'aea scaffold skill' works correctly in correct preconditions."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.resource_name = "myresource"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        cls.schema = json.load(open(SKILL_CONFIGURATION_SCHEMA))
        cls.resolver = jsonschema.RefResolver("file://{}/".format(Path(CONFIGURATION_SCHEMA_DIR).absolute()), cls.schema)
        cls.validator = Draft4Validator(cls.schema, resolver=cls.resolver)

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name], standalone_mode=False)
        assert result.exit_code == 0
        os.chdir(cls.agent_name)
        # scaffold skill
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "scaffold", "skill", cls.resource_name], standalone_mode=False)

    def test_exit_code_equal_to_0(self):
        """Test that the exit code is equal to 0."""
        assert self.result.exit_code == 0

    def test_resource_folder_contains_module_handlers(self):
        """Test that the resource folder contains scaffold handlers.py module."""
        p = Path(self.t, self.agent_name, "skills", self.resource_name, "handlers.py")
        original = Path(AEA_DIR, "skills", "scaffold", "handlers.py")
        assert filecmp.cmp(p, original)

    def test_resource_folder_contains_module_behaviours(self):
        """Test that the resource folder contains scaffold behaviours.py module."""
        p = Path(self.t, self.agent_name, "skills", self.resource_name, "behaviours.py")
        original = Path(AEA_DIR, "skills", "scaffold", "behaviours.py")
        assert filecmp.cmp(p, original)

    def test_resource_folder_contains_module_tasks(self):
        """Test that the resource folder contains scaffold tasks.py module."""
        p = Path(self.t, self.agent_name, "skills", self.resource_name, "tasks.py")
        original = Path(AEA_DIR, "skills", "scaffold", "tasks.py")
        assert filecmp.cmp(p, original)

    def test_resource_folder_contains_module_shared_class(self):
        """Test that the resource folder contains scaffold my_shared_class.py.py module."""
        p = Path(self.t, self.agent_name, "skills", self.resource_name, "my_shared_class.py")
        original = Path(AEA_DIR, "skills", "scaffold", "my_shared_class.py")
        assert filecmp.cmp(p, original)

    def test_resource_folder_contains_configuration_file(self):
        """Test that the resource folder contains a good configuration file."""
        p = Path(self.t, self.agent_name, "skills", self.resource_name, DEFAULT_SKILL_CONFIG_FILE)
        config_file = yaml.safe_load(open(p))
        self.validator.validate(instance=config_file)

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestScaffoldSkillFailsWhenDirectoryAlreadyExists:
    """Test that the command 'aea scaffold skill' fails when a folder with 'scaffold' name already."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.resource_name = "myresource"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name], standalone_mode=False)
        assert result.exit_code == 0
        os.chdir(cls.agent_name)
        # create a dummy 'myresource' folder
        Path(cls.t, cls.agent_name, "skills", cls.resource_name).mkdir(exist_ok=False, parents=True)
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "scaffold", "skill", cls.resource_name], standalone_mode=False)

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_error_message_skill_already_existing(self):
        """Test that the log error message is fixed.

        The expected message is: 'A skill with name '{skill_name}' already exists. Aborting...'
        """
        s = "A skill with this name already exists. Please choose a different name and try again."
        self.mocked_logger_error.assert_called_once_with(s)

    def test_resource_directory_exists(self):
        """Test that the resource directory still exists.

        This means that after every failure, we make sure we restore the previous state.
        """
        assert Path(self.t, self.agent_name, "skills", self.resource_name).exists()

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestScaffoldSkillFailsWhenSkillAlreadyExists:
    """Test that the command 'aea add skill' fails when the skill already exists."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.resource_name = "myresource"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name], standalone_mode=False)
        assert result.exit_code == 0
        os.chdir(cls.agent_name)
        # add skill first time
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "scaffold", "skill", cls.resource_name], standalone_mode=False)
        assert result.exit_code == 0
        # scaffold skill with the same skill name
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "scaffold", "skill", cls.resource_name], standalone_mode=False)

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_error_message_skill_already_existing(self):
        """Test that the log error message is fixed.

        The expected message is: 'A skill with name '{skill_name}' already exists. Aborting...'
        """
        s = "A skill with name '{}' already exists. Aborting...".format(self.resource_name)
        self.mocked_logger_error.assert_called_once_with(s)

    def test_resource_directory_exists(self):
        """Test that the resource directory still exists.

        This means that after every failure, we make sure we restore the previous state.
        """
        assert Path(self.t, self.agent_name, "skills", self.resource_name).exists()

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestScaffoldSkillFailsWhenConfigFileIsNotCompliant:
    """Test that the command 'aea scaffold skill' fails when the configuration file is not compliant with the schema."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.resource_name = "myresource"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        cls.patch = unittest.mock.patch.object(aea.cli.common.logger, 'error')
        cls.mocked_logger_error = cls.patch.__enter__()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name], standalone_mode=False)
        assert result.exit_code == 0

        # change the dumping of yaml module to raise an exception.
        cls.patch = unittest.mock.patch("yaml.safe_dump", side_effect=ValidationError("test error message"))
        cls.patch.__enter__()

        os.chdir(cls.agent_name)
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "scaffold", "skill", cls.resource_name], standalone_mode=False)

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_configuration_file_not_valid(self):
        """Test that the log error message is fixed.

        The expected message is: 'Cannot find skill: '{skill_name}'
        """
        self.mocked_logger_error.assert_called_once_with("Error when validating the skill configuration file.")

    def test_resource_directory_does_not_exists(self):
        """Test that the resource directory does not exist.

        This means that after every failure, we make sure we restore the previous state.
        """
        assert not Path(self.t, self.agent_name, "skills", self.resource_name).exists()

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        cls.patch.__exit__()
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestScaffoldSkillFailsWhenExceptionOccurs:
    """Test that the command 'aea scaffold skill' fails when the configuration file is not compliant with the schema."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.runner = CliRunner()
        cls.agent_name = "myagent"
        cls.resource_name = "myresource"
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()

        os.chdir(cls.t)
        result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "create", cls.agent_name], standalone_mode=False)
        assert result.exit_code == 0

        cls.patch = unittest.mock.patch("shutil.copytree", side_effect=Exception("unknwon exception"))
        cls.patch.__enter__()

        os.chdir(cls.agent_name)
        cls.result = cls.runner.invoke(cli, [*CLI_LOG_OPTION, "scaffold", "skill", cls.resource_name], standalone_mode=False)

    def test_exit_code_equal_to_1(self):
        """Test that the exit code is equal to 1 (i.e. catchall for general errors)."""
        assert self.result.exit_code == 1

    def test_resource_directory_does_not_exists(self):
        """Test that the resource directory does not exist.

        This means that after every failure, we make sure we restore the previous state.
        """
        assert not Path(self.t, self.agent_name, "skills", self.resource_name).exists()

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        cls.patch.__exit__()
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass
