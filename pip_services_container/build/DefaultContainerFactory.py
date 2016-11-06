# -*- coding: utf-8 -*-
"""
    pip_services_container.build.DefaultContainerFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default container factory implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.refer import Descriptor
from pip_services_commons.refer import IDescriptable
from pip_services_commons.build import CompositeFactory
from pip_services_commons.log import DefaultLoggerFactory
from pip_services_commons.count import DefaultCountersFactory
from pip_services_commons.cache import DefaultCacheFactory

DefaultContainerFactoryDescriptor = Descriptor(
    "pip-services-container", "factory", "container", "1.0"
)

class DefaultContainerFactory(CompositeFactory, IDescriptable):

    def __init__(self):
        #self.add(ContainerInfoFactory())
        self.add(DefaultLoggerFactory())
        self.add(DefaultCountersFactory())
        self.add(DefaultCacheFactory())

    def get_descriptor(self):
        return DefaultContainerFactoryDescriptor
