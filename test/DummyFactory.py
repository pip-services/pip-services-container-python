# -*- coding: utf-8 -*-
"""
    test.DummyFactory
    ~~~~~~~~~~~~~~~~~
    
    Dummy factory implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .DummyController import DummyController

from pip_services_commons.refer import Descriptor
from pip_services_commons.refer import IDescriptable
from pip_services_commons.build import IFactory

DummyFactoryDescriptor = Descriptor(
    "pip-services-dummies", "factory", "default", "1.0"
)
DummyControllerDescriptor = Descriptor(
    "pip-services-dummies", "controller", "default", "1.0"
)

class DummyFactory(object, IFactory, IDescriptable):

    def get_descriptor(self):
        return DummyFactoryDescriptor

    def can_create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(DummyControllerDescriptor):
                return True
        return False

    def create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(DummyControllerDescriptor):
                return DummyController()
        return None
