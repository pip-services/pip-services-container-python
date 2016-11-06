# -*- coding: utf-8 -*-
"""
    test.refer.test_ContainerInfo
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Tests for container information
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import datetime

from pip_services_commons.config import ConfigParams
from pip_services_container.info import ContainerInfo

class TestContainerInfo(object):

    def test_name(self):
        container_info = ContainerInfo()
        assert container_info.name == "unknown"
        
        container_info.name = "new name"
        assert container_info.name == "new name"

    def test_description(self):
        container_info = ContainerInfo()
        assert None == container_info.description
        
        container_info.description = "new description"
        assert container_info.description == "new description"

    def test_container_id(self):
        container_info = ContainerInfo()
        container_info.container_id = "new container id"
        assert container_info.container_id == "new container id"

    def test_start_time(self):
        container_info = ContainerInfo()
        assert container_info.start_time.year == datetime.datetime.utcnow().year
        assert container_info.start_time.month == datetime.datetime.utcnow().month
        
    def test_from_config(self):
        config = ConfigParams.from_tuples(
            "info.name", "new name",
            "info.description", "new description",
            "info.properties.access_key", "key",
            "info.properties.store_key", "store key"
        )
        container_info = ContainerInfo.from_config(config)
        assert container_info.name == "new name"
        assert container_info.description == "new description"
