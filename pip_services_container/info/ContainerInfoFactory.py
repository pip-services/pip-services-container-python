# -*- coding: utf-8 -*-
"""
    pip_services_container.info.ContainerInfoFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Container info factory implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .ContainerInfo import ContainerInfo
from .ContainerInfo import ContainerInfoDescriptor

from pip_services_commons.refer import Descriptor
from pip_services_commons.refer import IDescriptable
from pip_services_commons.build import IFactory

ContainerInfoFactoryDescriptor = Descriptor(
    "pip-services-container", "factory", "container-info", "1.0"
)

class ContainerInfoFactory(IFactory, IDescriptable):

    def get_descriptor(self):
        return ContainerInfoFactoryDescriptor

    def can_create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(ContainerInfoDescriptor):
                return True
        return False

    def create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(ContainerInfoDescriptor):
                return ContainerInfo()

        return None
