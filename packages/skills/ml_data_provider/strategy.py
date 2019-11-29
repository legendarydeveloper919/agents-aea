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
from typing import Tuple

import numpy as np
from tensorflow import keras

from aea.protocols.oef.models import Attribute, DataModel, Description, Query
from aea.skills.base import SharedClass

DEFAULT_PRICE_PER_DATA_BATCH = 1
DEFAULT_BATCH_SIZE = 32
DEFAULT_SELLER_TX_FEE = 0
DEFAULT_BUYER_TX_FEE = 0
DEFAULT_CURRENCY_PBK = 'FET'
DEFAULT_LEDGER_ID = 'fetchai'


class Strategy(SharedClass):
    """This class defines a strategy for the agent."""

    def __init__(self, **kwargs) -> None:
        """Initialize the strategy of the agent."""
        self.price_per_data_batch = kwargs.pop('price_per_data_batch', DEFAULT_PRICE_PER_DATA_BATCH)
        self.batch_size = kwargs.pop('batch_size', DEFAULT_BATCH_SIZE)
        self.seller_tx_fee = kwargs.pop('seller_tx_fee', DEFAULT_SELLER_TX_FEE)
        self.buyer_tx_fee = kwargs.pop('buyer_tx_fee', DEFAULT_BUYER_TX_FEE)
        self.currency_pbk = kwargs.pop('currency_pbk', DEFAULT_CURRENCY_PBK)
        self.ledger_id = kwargs.pop('ledger_id', DEFAULT_LEDGER_ID)
        super().__init__(**kwargs)
        self._oef_msg_id = 0

        # loading ML dataset
        # TODO this should be parametrized
        (self.train_x, self.train_y), (self.test_x, self.test_y) = keras.datasets.fashion_mnist.load_data()

    def get_next_oef_msg_id(self) -> int:
        """
        Get the next oef msg id.

        :return: the next oef msg id
        """
        self._oef_msg_id += 1
        return self._oef_msg_id

    def get_service_description(self) -> Description:
        """
        Get the service description.

        :return: a description of the offered services
        """
        dm = DataModel("ml_datamodel", [Attribute("ml_data", str, True)])
        desc = Description({'ml_data': 'Fashion MNIST'}, data_model=dm)
        return desc

    def _sample(self, n: int):
        """Sample N rows from data."""
        idx = np.arange(self.train_x.shape[0])
        mask = np.zeros_like(idx, dtype=bool)

        selected = np.random.choice(idx, n, replace=False)
        mask[selected] = True

        x_sample = self.train_x[mask]
        y_sample = self.train_y[mask]
        return x_sample, y_sample

    def generate_proposal_and_data(self, query: Query) -> Tuple[Description, Tuple[np.ndarray, np.ndarray]]:
        """
        Generate a proposal matching the query.

        :param query: the query
        :return: a tuple of proposal and the weather data
        """
        batch = self._sample(self.batch_size)
        proposal = Description({"rows": self.batch_size,
                                "price": self.price_per_data_batch,
                                "seller_tx_fee": self.seller_tx_fee,
                                "currency_pbk": self.currency_pbk,
                                "ledger_id": self.ledger_id})
        return proposal, batch
