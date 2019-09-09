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

"""This contains the rl agent class."""

from typing import Any, Dict
import random
import numpy as np

from env import BanditNArmedRandom
from bandit_proxy_env import BanditProxyEnv
from proxy_env import ProxyEnv


class PriceBandit(object):
    """A class for a multi-armed bandit model of price."""

    def __init__(self, price: float, beta_a: float = 1.0, beta_b: float = 1.0):
        """
        Instantiate a price bandit object.

        :param price: the price this bandit is modelling
        :param beta_a: the a parameter of the beta distribution
        :param beta_b: the b parameter of the beta distribution
        """
        self.price = price
        # default params imply a uniform random prior
        self.beta_a = beta_a
        self.beta_b = beta_b

    def sample(self) -> int:
        """
        Sample from the bandit.

        :return: the sampled value
        """
        return round(np.random.beta(self.beta_a, self.beta_b))

    def update(self, outcome: bool) -> None:
        """
        Update the bandit.

        :param outcome: the outcome used for updating
        :return: None
        """
        outcome_int = 1 if outcome else 0  # explicit type conversion
        self.beta_a += outcome_int
        self.beta_b += 1 - outcome_int


class GoodPriceModel(object):
    """A class for a price model of a good."""

    def __init__(self, bound: int = 100):
        """Instantiate a good price model."""
        self.price_bandits = dict(
            (price, PriceBandit(price))
            for price in range(bound + 1))

    def update(self, outcome: bool, price: int) -> None:
        """
        Update the respective bandit.

        :param price: the price to be updated
        :param outcome: the negotiation outcome
        :return: None
        """
        bandit = self.price_bandits[price]
        bandit.update(outcome)

    def get_price_expectation(self) -> int:
        """
        Get best price.

        :return: the winning price
        """
        maxsample = -1
        winning_price = 0
        for price, bandit in self.price_bandits.items():
            sample = bandit.sample()
            if sample > maxsample:
                maxsample = sample
                winning_price = price
        return winning_price


class RLAgent:

    def __init__(self, nb_goods: int):
        self.good_price_models = dict(
            (good_id, GoodPriceModel()) for good_id in range(nb_goods))  # type: Dict[int, GoodPriceModel]

    def _pick_an_action(self) -> Any:
        """
        Pick an action.

        :return: None
        """
        # Get the good
        good_id = self._get_random_next_good()

        # Pick the best price based on own model.
        good_price_model = self.good_price_models[good_id]
        price = good_price_model.get_price_expectation()

        action = [good_id, price]

        return action

    def _update_model(self, obs, reward, done, info, action) -> None:
        """
        Update model.

        :return: None
        """
        good_id, price = action

        # Update the price model:
        good_price_model = self.good_price_models[good_id]
        good_price_model.update(reward, price)

    def _get_random_next_good(self) -> int:
        """Get the next good for trading (randomly)."""
        return random.choice(list(self.good_price_models.keys()))

    def fit(self, proxy_env: ProxyEnv, nb_steps: int):
        action_counter = 0

        print("Connecting to proxy env ...")
        proxy_env.connect()

        while action_counter < nb_steps:
            action = self._pick_an_action()
            obs, reward, done, info = proxy_env.step(action)
            self._update_model(obs, reward, done, info, action)
            action_counter += 1
            if action_counter % 10 == 0:
                print("Action: step_id='{}' action='{}'".format(action_counter, action))

        proxy_env.disconnect()
        print("Disconnected from proxy env!")


if __name__ == "__main__":
    NB_GOODS = 10
    NB_PRICES_PER_GOOD = 100

    gym_env = BanditNArmedRandom(nb_bandits=NB_GOODS, nb_prices_per_bandit=NB_PRICES_PER_GOOD)
    proxy_env = BanditProxyEnv(gym_env)

    """Launch the agent."""
    rl_agent = RLAgent(nb_goods=NB_GOODS)
    rl_agent.fit(proxy_env, nb_steps=1000)
