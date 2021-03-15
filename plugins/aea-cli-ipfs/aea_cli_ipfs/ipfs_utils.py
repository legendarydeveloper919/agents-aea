# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2020 Fetch.AI Limited
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
"""Ipfs utils for `ipfs cli command`."""
import os
import shutil
import signal
import subprocess  # nosec
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import ipfshttpclient


class IPFSDaemon:
    """
    Set up the IPFS daemon.

    :raises Exception: if IPFS is not installed.
    """

    def __init__(self, timeout: float = 15.0):
        """Initialise IPFS daemon."""
        # check we have ipfs
        self.timeout = timeout
        res = shutil.which("ipfs")
        if res is None:
            raise Exception("Please install IPFS first!")
        process = subprocess.Popen(  # nosec
            ["ipfs", "--version"], stdout=subprocess.PIPE, env=os.environ.copy(),
        )
        output, _ = process.communicate()
        if b"0.6.0" not in output:
            raise Exception(
                "Please ensure you have version 0.6.0 of IPFS daemon installed."
            )
        self.process = None  # type: Optional[subprocess.Popen]

    def __enter__(self) -> None:
        """Run the ipfs daemon."""
        self.process = subprocess.Popen(  # nosec
            ["ipfs", "daemon"], stdout=subprocess.PIPE, env=os.environ.copy(),
        )
        print("Waiting for {} seconds the IPFS daemon to be up.".format(self.timeout))
        time.sleep(self.timeout)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        """Terminate the ipfs daemon."""
        if self.process is None:
            return
        self.process.send_signal(signal.SIGTERM)
        self.process.wait(timeout=30)
        poll = self.process.poll()
        if poll is None:
            self.process.terminate()
            self.process.wait(2)


class RemoveError(Exception):
    """Exception on remove."""


class PublishError(Exception):
    """Exception on publish."""


class NodeError(Exception):
    """Exception for node connection check."""


class IPFSTool:
    """IPFS tool to add, publish, remove, download directories."""

    def __init__(self, client_options: Optional[Dict] = None):
        """
        Init tool.

        :param client_options: dict, options for ipfshttpclient instance.
        """
        self.client = ipfshttpclient.Client(**(client_options or {}))

    def add(self, dir_path: str) -> Tuple[str, str, List]:
        """
        Add directory to ipfs.

        It wraps into directory.

        :param dir_path: str, path to dir to publush

        :return: dir name published, hash, list of items processed
        """
        response = self.client.add(
            dir_path, pin=True, recursive=True, wrap_with_directory=True
        )
        return response[-2]["Name"], response[-1]["Hash"], response[:-1]

    def remove(self, hash_id: str) -> Dict:
        """
        Remove dir added by it's hash.

        :param hash_id: str. hash of dir to remove

        :return: dict with unlinked items.
        """
        try:
            return self.client.pin.rm(hash_id, recursive=True)
        except ipfshttpclient.exceptions.ErrorResponse as e:
            raise RemoveError(f"Error on {hash_id} remove: {str(e)}") from e

    def download(self, hash_id: str, target_dir: str, fix_path: bool = True) -> None:
        """
        Download dir by it's hash.

        :param hash_id: str. hash od fir to download
        :param target_dir: str. directory to place downlaoded
        :param fix_path: boo. default True. on download dont wrap result in to hash_id dirrectory.

        :return: None
        """
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)
        self.client.get(hash_id, target_dir)

        downloaded_path = str(Path(target_dir) / hash_id)

        if fix_path:
            # self.client.get creates result with hash name  and content, but we want content in the target dir
            for each_file in Path(downloaded_path).iterdir():  # grabs all files
                shutil.move(str(each_file), target_dir)
        os.rmdir(downloaded_path)

    def publish(self, hash_id: str) -> Dict:
        """
        Publish directory by it's hash id.

        :param hash_id: hash of the directory to publish.

        :return: dict of names it was publish for.
        """
        try:
            return self.client.name.publish(hash_id)
        except ipfshttpclient.exceptions.TimeoutError:
            raise PublishError(
                "can not publish within timeout, check internet connection!"
            )

    def chec_ipfs_node_running(self) -> None:
        """Check ipfs node running."""
        try:
            self.client.id()
        except ipfshttpclient.exceptions.CommunicationError as e:
            raise NodeError(f"Can not connect to node. Is node running?:\n{e}") from e
