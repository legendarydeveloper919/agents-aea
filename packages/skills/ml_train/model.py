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
import json
import threading
from pathlib import Path

from tensorflow import keras

from aea.skills.base import SharedClass

DEFAULT_MODEL_CONFIG_PATH = str(Path("..", "..", "model.config").resolve())


class Model(SharedClass):
    """This class defines a machine learning model."""

    def __init__(self, **kwargs):
        """Initialize the machine learning model."""
        self._model_config_path = kwargs.pop("model_config_path", DEFAULT_MODEL_CONFIG_PATH)
        super().__init__(**kwargs)

        # TODO this at the momment does not work - need to compile the model according to the network configuration
        #      A better alternative is to save/load in HDF5 format, but that might require some system level dependencies
        #      https://keras.io/getting-started/faq/#how-can-i-install-hdf5-or-h5py-to-save-my-models-in-keras
        # self._model = keras.Model.from_config(json.load(open(self._model_config_path)))
        self._model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])
        self._model.compile(optimizer='adam',
                            loss='sparse_categorical_crossentropy',
                            metrics=['accuracy'])
        self._lock = threading.Lock()

    @property
    def tf_model(self) -> keras.Model:
        with self._lock:
            return self._model

    def save(self):
        """Save the model weights."""
        # TODO to implement.