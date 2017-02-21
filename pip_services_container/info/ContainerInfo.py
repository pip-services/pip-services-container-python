# -*- coding: utf-8 -*-
"""
    pip_services_container.info.ContainerInfo
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Container info implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import datetime

from pip_services_commons.data import StringValueMap
from pip_services_commons.data import IdGenerator
from pip_services_commons.refer import Descriptor
from pip_services_commons.refer import IDescriptable

ContainerInfoDescriptor = Descriptor(
    "pip-services-container", "container-info", "default", "1.0"
)

class ContainerInfo(object, IDescriptable):
    name = None
    description = None
    container_id = None
    start_time = None
    properties = None

    def __init__(self):
        self.name = "unknown"
        self.start_time = datetime.datetime.utcnow()
        self.container_id = IdGenerator.next_long()

    def get_descriptor(self):
        return ContainerInfoDescriptor

    @staticmethod
    def from_config(config):
        result = ContainerInfo()

        info = config.get_section("info")
        result.name = info.get_as_nullable_string("name")
        result.description = info.get_as_nullable_string("description")
        result.properties = info.get_section("properties")

        return result

