# -*- coding: utf-8 -*-
"""
    test.DummyFactory
    ~~~~~~~~~~~~~~~~~
    
    Dummy factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .DummyController import DummyController

from pip_services_commons.refer import Descriptor
from pip_services_commons.build import Factory

DummyFactoryDescriptor = Descriptor(
    "pip-services-dummies", "factory", "default", "default", "1.0"
)

DummyControllerDescriptor = Descriptor(
    "pip-services-dummies", "controller", "default", "default", "1.0"
)

class DummyFactory(Factory):

    def __init__(self):
        self.register_as_type(DummyControllerDescriptor, DummyController)

