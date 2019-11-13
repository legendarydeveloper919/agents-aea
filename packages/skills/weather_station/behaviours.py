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

"""This package contains a scaffold of a behaviour."""

import datetime
import logging
from typing import cast, Optional, TYPE_CHECKING

from aea.skills.base import Behaviour
from aea.protocols.oef.message import OEFMessage
from aea.protocols.oef.models import Description
from aea.protocols.oef.serialization import OEFSerializer, DEFAULT_OEF

if TYPE_CHECKING:
    from packages.skills.weather_station.strategy import Strategy
else:
    from weather_station_skill.strategy import Strategy

logger = logging.getLogger("aea.weather_station_skill")

SERVICE_ID = ''


class ServiceRegistrationBehaviour(Behaviour):
    """This class implements a behaviour."""

    def __init__(self, **kwargs):
        """Initialise the behaviour."""
        self._services_interval = kwargs.pop('services_interval', 30)  # type: int
        super().__init__(**kwargs)
        self._last_update_time = datetime.datetime.now()  # type: datetime.datetime
        self._registered_service_description = None  # type: Optional[Description]

    def setup(self) -> None:
        """
        Implement the setup.

        :return: None
        """
        self._register_service()

    def act(self) -> None:
        """
        Implement the act.

        :return: None
        """
        if self._is_time_to_update_services():
            self._unregister_service()
            self._register_service()

    def teardown(self) -> None:
        """
        Implement the task teardown.

        :return: None
        """
        self._unregister_service()

    def _register_service(self) -> None:
        """
        Register to the OEF Service Directory.

        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        desc = strategy.get_service_description()
        self._registered_service_description = desc
        oef_msg_id = strategy.get_next_oef_msg_id()
        msg = OEFMessage(oef_type=OEFMessage.Type.REGISTER_SERVICE,
                         id=oef_msg_id,
                         service_description=desc,
                         service_id=SERVICE_ID)
        self.context.outbox.put_message(to=DEFAULT_OEF,
                                        sender=self.context.agent_public_key,
                                        protocol_id=OEFMessage.protocol_id,
                                        message=OEFSerializer().encode(msg))
        logger.info("[{}]: updating weather station services on OEF.".format(self.context.agent_name))

    def _unregister_service(self) -> None:
        """
        Unregister service from OEF Service Directory.

        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        oef_msg_id = strategy.get_next_oef_msg_id()
        msg = OEFMessage(oef_type=OEFMessage.Type.UNREGISTER_SERVICE,
                         id=oef_msg_id,
                         service_description=self._registered_service_description,
                         service_id=SERVICE_ID)
        self.context.outbox.put_message(to=DEFAULT_OEF,
                                        sender=self.context.agent_public_key,
                                        protocol_id=OEFMessage.protocol_id,
                                        message=OEFSerializer().encode(msg))
        logger.info("[{}]: unregistering weather station services from OEF.".format(self.context.agent_name))
        self._registered_service_description = None

    def _is_time_to_update_services(self) -> bool:
        """
        Check if the agent should update the service directory.

        :return: bool indicating the action
        """
        now = datetime.datetime.now()
        diff = now - self._last_update_time
        result = diff.total_seconds() > self._services_interval
        if result:
            self._last_update_time = now
        return result
