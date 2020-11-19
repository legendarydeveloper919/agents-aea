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
"""This module contains sqlite storage backend implementation."""
import asyncio
import json
import sqlite3
import threading
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

from aea.helpers.storage.backends.base import AbstractStorageBackend


class SqliteStorageBackend(AbstractStorageBackend):
    """Sqlite storage backend."""

    def __init__(self, uri: str) -> None:
        """Init backend."""
        super().__init__(uri)
        parsed = urlparse(uri)
        self._fname = parsed.netloc or parsed.path
        self._connection: Optional[sqlite3.Connection] = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._lock = threading.Lock()

    def _execute_sql_sync(self, query: str, args: Optional[List] = None) -> List[Tuple]:
        """
        Execute sql command and return results.

        :param query: sql query string
        :param args: optional argumets to set into sql query.

        :return: List of tuples with sql records
        """
        if not self._connection:  # pragma: nocover
            raise ValueError("Not connected")
        with self._lock:
            return self._connection.execute(query, args or []).fetchall()

    async def _executute_sql(self, query: str, args: Optional[List] = None):
        """
        Execute sql command and return results in async executor.

        :param query: sql query string
        :param args: optional argumets to set into sql query.

        :return: List of tuples with sql records
        """
        if not self._loop:  # pragma: nocover
            raise ValueError("Not connected")
        return await self._loop.run_in_executor(
            None, self._execute_sql_sync, query, args
        )

    async def connect(self) -> None:
        """Connect to backend."""
        self._loop = asyncio.get_event_loop()
        self._connection = await self._loop.run_in_executor(
            None, sqlite3.connect, self._fname
        )

    async def disconnect(self) -> None:
        """Disconnect the backend."""
        if not self._loop or not self._connection:  # pragma: nocover
            raise ValueError("Not connected")
        await self._loop.run_in_executor(None, self._connection.close)
        self._connection = None
        self._loop = None

    async def ensure_collection(self, collection_name: str) -> None:
        """
        Create collection if not exits.

        :param collection_name: str.
        :return: None
        """
        self._check_collection_name(collection_name)
        sql = f"""CREATE TABLE IF NOT EXISTS {collection_name} (
            object_id TEXT PRIMARY KEY,
            object_body JSON1 NOT NULL)
        """
        await self._executute_sql(sql)

    async def put(
        self, collection_name: str, object_id: str, object_body: Dict
    ) -> None:
        """
        Put object into collection.

        :param collection_name: str.
        :param object_id: str object id
        :param object_body: python dict, json compatible.
        :return: None
        """
        self._check_collection_name(collection_name)
        sql = f"""INSERT INTO {collection_name} (object_id, object_body)
            VALUES (?, ?);
        """
        await self._executute_sql(sql, [object_id, json.dumps(object_body)])

    async def get(self, collection_name: str, object_id: str) -> Optional[Dict]:
        """
        Get object from the collection.

        :param collection_name: str.
        :param object_id: str object id

        :return: dict if object exists in collection otherwise None
        """
        self._check_collection_name(collection_name)
        sql = f"""SELECT object_body FROM {collection_name} WHERE object_id = ? LIMIT 1;"""
        result = await self._executute_sql(sql, [object_id])
        if result:
            return json.loads(result[0][0])
        return None

    async def remove(self, collection_name: str, object_id: str) -> None:
        """
        Remove object from the collection.

        :param collection_name: str.
        :param object_id: str object id

        :return: None
        """
        self._check_collection_name(collection_name)
        sql = f"""DELETE FROM {collection_name} WHERE object_id = ?;"""
        await self._executute_sql(sql, [object_id])

    async def find(self, collection_name: str, field: str, equals: Any) -> List[Dict]:
        """
        Get objects from the collection by filtering by field value.

        :param collection_name: str.
        :param field: field name to search: example "parent.field"
        :param equals: value field should be equal to

        :return: None
        """
        self._check_collection_name(collection_name)
        sql = f"""SELECT object_body FROM {collection_name} WHERE json_extract(object_body, ?) = ?;"""
        if not field.startswith("$."):
            field = f"$.{field}"
        return [
            json.loads(i[0]) for i in await self._executute_sql(sql, [field, equals])
        ]
