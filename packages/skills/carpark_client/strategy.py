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

"""This module contains the strategy class."""

import datetime
import time
from typing import cast

from aea.protocols.oef.models import Description, Query, Constraint, ConstraintType
from aea.skills.base import SharedClass

DEFAULT_COUNTRY = 'UK'
SEARCH_TERM = 'country'
DEFAULT_SEARCH_INTERVAL = 5.0
DEFAULT_MAX_PRICE = 4000
DEFAULT_MAX_DETECTION_AGE = 60 * 60   # 1 hour


class Strategy(SharedClass):
    """This class defines a strategy for the agent."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize the strategy of the agent.

        :return: None
        """
        self._country = kwargs.pop('country') if 'country' in kwargs.keys() else DEFAULT_COUNTRY
        self._search_interval = cast(float, kwargs.pop('search_interval')) if 'search_interval' in kwargs.keys() else DEFAULT_SEARCH_INTERVAL
        self._max_price = kwargs.pop('max_price') if 'max_price' in kwargs.keys() else DEFAULT_MAX_PRICE
        self._max_detection_age = kwargs.pop('max_detection_age') if 'max_detection_age' in kwargs.keys() else DEFAULT_MAX_DETECTION_AGE
        super().__init__(**kwargs)
        self.is_searching = True
        self.last_search_time = datetime.datetime.now() - datetime.timedelta(seconds=self._search_interval)
        print ("self._max_price  = {}".format(self._max_price ))

    def get_service_query(self) -> Query:
        """
        Get the service query of the agent.

        :return: the query
        """
        query = Query([Constraint('longitude', ConstraintType("!=", 0.0))], model=None)
        return query

    def pause_search(self):
        """Stop searching temporarily"""
        self.is_searching = False

    def unpause_search(self):
        """Restart searching after pausing"""
        self.last_search_time = datetime.datetime.now()
        self.is_searching = True

    def is_time_to_search(self) -> bool:
        """
        Check whether it is time to search.

        :return: whether it is time to search
        """
        now = datetime.datetime.now()
        diff = now - self.last_search_time
       # print("is_time_to_search: diff = {}".format(diff))
        result = diff.total_seconds() > self._search_interval
        return result

    def is_acceptable_proposal(self, proposal: Description) -> bool:
        """
        Check whether it is an acceptable proposal.

        :return: whether it is acceptable
        """
        result = proposal.values["price"] < self._max_price and \
            proposal.values["last_detection_time"] > int(time.time()) - self._max_detection_age
        print("is_acceptable_proposal price = {} - self._max_price = {}".format(proposal.values["price"], self._max_price))

        return result
