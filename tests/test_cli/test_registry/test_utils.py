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
"""This test module contains the tests for CLI Registry utils."""
import os

from builtins import FileNotFoundError
from unittest import TestCase, mock
from click import ClickException
from yaml import YAMLError
from requests.exceptions import ConnectionError

from aea.cli.common import AEAConfigException
from aea.cli.registry.utils import (
    fetch_package, request_api, download_file, extract, _init_config_folder,
    write_cli_config, read_cli_config
)
from aea.cli.registry.settings import REGISTRY_API_URL
from aea.configurations.base import PublicId


@mock.patch(
    'aea.cli.registry.utils.request_api',
    return_value={'file': 'url'}
)
@mock.patch(
    'aea.cli.registry.utils.download_file',
    return_value='filepath'
)
@mock.patch('aea.cli.registry.utils.extract')
class TestFetchPackage:
    """Test case for fetch_package method."""

    def test_fetch_package_positive(
        self,
        extract_mock,
        download_file_mock,
        request_api_mock
    ):
        """Test for fetch_package method positive result."""
        obj_type = 'connection'
        public_id = PublicId.from_string('author/name:0.1.0')
        cwd = 'cwd'

        fetch_package(obj_type, public_id, cwd)
        request_api_mock.assert_called_with(
            'GET', '/connections/author/name/0.1.0'
        )
        download_file_mock.assert_called_once_with('url', 'cwd')
        extract_mock.assert_called_once_with('filepath', 'cwd/connections')


def _raise_connection_error(*args):
    raise ConnectionError()


def _raise_config_exception(*args):
    raise AEAConfigException()


@mock.patch('aea.cli.registry.utils.requests.request')
class RequestAPITestCase(TestCase):
    """Test case for request_api method."""

    def test_request_api_positive(self, request_mock):
        """Test for fetch_package method positive result."""
        expected_result = {'correct': 'json'}

        resp_mock = mock.Mock()
        resp_mock.json = lambda: expected_result
        resp_mock.status_code = 200
        request_mock.return_value = resp_mock

        result = request_api('GET', '/path')
        request_mock.assert_called_once_with(
            method='GET',
            params=None,
            data=None,
            files=None,
            headers={},
            url=REGISTRY_API_URL + '/path'
        )
        self.assertEqual(result, expected_result)

    def test_request_api_404(self, request_mock):
        """Test for fetch_package method 404 sever response."""
        resp_mock = mock.Mock()
        resp_mock.status_code = 404
        request_mock.return_value = resp_mock
        with self.assertRaises(ClickException):
            request_api('GET', '/path')

    def test_request_api_403(self, request_mock):
        """Test for fetch_package method not authorized sever response."""
        resp_mock = mock.Mock()
        resp_mock.status_code = 403
        request_mock.return_value = resp_mock
        with self.assertRaises(ClickException):
            request_api('GET', '/path')

    def test_request_api_409(self, request_mock):
        """Test for fetch_package method conflict sever response."""
        resp_mock = mock.Mock()
        resp_mock.status_code = 409
        resp_mock.json = lambda: {'detail': 'some'}
        request_mock.return_value = resp_mock
        with self.assertRaises(ClickException):
            request_api('GET', '/path')

    def test_request_api_unexpected_response(self, request_mock):
        """Test for fetch_package method unexpected sever response."""
        resp_mock = mock.Mock()
        resp_mock.status_code = 500
        request_mock.return_value = resp_mock
        with self.assertRaises(ClickException):
            request_api('GET', '/path')

    @mock.patch(
        'aea.cli.registry.utils.requests.request', _raise_connection_error
    )
    def test_request_api_server_not_responding(self, request_mock):
        """Test for fetch_package method no server response."""
        with self.assertRaises(ClickException):
            request_api('GET', '/path')

    @mock.patch(
        'aea.cli.registry.utils.read_cli_config', _raise_config_exception
    )
    def test_request_api_no_auth_data(self, request_mock):
        """Test for fetch_package method no server response."""
        with self.assertRaises(ClickException):
            request_api('GET', '/path')


@mock.patch('aea.cli.registry.utils.requests.get')
class DownloadFileTestCase(TestCase):
    """Test case for download_file method."""

    @mock.patch('builtins.open', mock.mock_open())
    def test_download_file_positive(self, get_mock):
        """Test for download_file method positive result."""
        filename = 'filename.tar.gz'
        url = 'url/{}'.format(filename)
        cwd = 'cwd'
        filepath = os.path.join(cwd, filename)

        resp_mock = mock.Mock()
        raw_mock = mock.Mock()
        raw_mock.read = lambda: 'file content'

        resp_mock.raw = raw_mock
        resp_mock.status_code = 200
        get_mock.return_value = resp_mock

        result = download_file(url, cwd)
        expected_result = filepath
        self.assertEqual(result, expected_result)
        get_mock.assert_called_once_with(url, stream=True)

    def test_download_file_wrong_response(self, get_mock):
        """Test for download_file method wrong response from file server."""
        resp_mock = mock.Mock()
        resp_mock.status_code = 404
        get_mock.return_value = resp_mock

        with self.assertRaises(ClickException):
            download_file('url', 'cwd')


class ExtractTestCase(TestCase):
    """Test case for extract method."""

    @mock.patch('aea.cli.registry.utils.os.remove')
    @mock.patch('aea.cli.registry.utils.tarfile.open')
    def test_extract_positive(self, tarfile_open_mock, os_remove_mock):
        """Test for extract method positive result."""
        source = 'file.tar.gz'
        target = 'target-folder'

        tar_mock = mock.Mock()
        tar_mock.extractall = lambda path: None
        tar_mock.close = lambda: None
        tarfile_open_mock.return_value = tar_mock

        extract(source, target)
        tarfile_open_mock.assert_called_once_with(source, 'r:gz')
        os_remove_mock.assert_called_once_with(source)

    def test_extract_wrong_file_type(self):
        """Test for extract method wrong file type."""
        source = 'file.wrong'
        target = 'target-folder'
        with self.assertRaises(Exception):
            extract(source, target)


@mock.patch('aea.cli.registry.utils.os.path.dirname', return_value='dir-name')
@mock.patch('aea.cli.registry.utils.os.path.exists', return_value=False)
@mock.patch('aea.cli.registry.utils.os.makedirs')
class InitConfigFolderTestCase(TestCase):
    """Test case for _init_config_folder method."""

    def test_init_config_folder_positive(
        self, makedirs_mock, exists_mock, dirname_mock
    ):
        """Test for _init_config_folder method positive result."""
        _init_config_folder()
        dirname_mock.assert_called_once()
        exists_mock.assert_called_once_with('dir-name')
        makedirs_mock.assert_called_once_with('dir-name')


@mock.patch('aea.cli.registry.utils._init_config_folder')
@mock.patch('aea.cli.registry.utils.yaml.dump')
@mock.patch('builtins.open', mock.mock_open())
class WriteCLIConfigTestCase(TestCase):
    """Test case for write_cli_config method."""

    def test_write_cli_config_positive(self, dump_mock, icf_mock):
        """Test for write_cli_config method positive result."""
        write_cli_config({'some': 'config'})
        icf_mock.assert_called_once()
        dump_mock.assert_called_once()


def _raise_yamlerror(*args):
    raise YAMLError()


def _raise_file_not_found_error(*args):
    raise FileNotFoundError()


@mock.patch('builtins.open', mock.mock_open())
class ReadCLIConfigTestCase(TestCase):
    """Test case for read_cli_config method."""

    @mock.patch(
        'aea.cli.registry.utils.yaml.safe_load',
        return_value={'correct': 'output'}
    )
    def test_read_cli_config_positive(self, safe_load_mock):
        """Test for read_cli_config method positive result."""
        result = read_cli_config()
        expected_result = {'correct': 'output'}
        self.assertEqual(result, expected_result)
        safe_load_mock.assert_called_once()

    @mock.patch(
        'aea.cli.registry.utils.yaml.safe_load',
        _raise_yamlerror
    )
    def test_read_cli_config_bad_yaml(self):
        """Test for read_cli_config method bad yaml behavior."""
        with self.assertRaises(ClickException):
            read_cli_config()

    @mock.patch(
        'aea.cli.registry.utils.yaml.safe_load',
        _raise_file_not_found_error
    )
    def test_read_cli_config_file_not_found(self):
        """Test for read_cli_config method bad yaml behavior."""
        with self.assertRaises(AEAConfigException):
            read_cli_config()
