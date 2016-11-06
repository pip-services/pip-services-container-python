# -*- coding: utf-8 -*-
"""
    pip_services_container.config.ContainerConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Container configuration reader implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.errors import ConfigException

class ContainerConfigReader(object):

    @staticmethod
    def read_from_file(correlation_id, path):
        if path == None:
            raise ConfigException(correlation_id, "NO_PATH", "Missing config file path")
        
        index = path.find('.')
        ext = path[index + 1:].lower() if index > 0 else ''
        
        if ext == "json":
            return read_from_json_file(correlation_id, path)
        elif ext == "yaml":
            return read_from_yaml_file(correlation_id, path)
        
        # By default read as JSON
        return read_from_json_file(correlation_id, path)

    @staticmethod
    def read_from_json_file(correlation_id, path):
        config = JsonConfigReader.read_config(correlation_id, path)
        return ContainerConfig.from_config(config)

    @staticmethod
    def read_from_yaml_file(correlation_id, path):
        config = YamlConfigReader.read_config(correlation_id, path)
        return ContainerConfig.from_config(config)

