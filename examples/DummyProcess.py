# -*- coding: utf-8 -*-
"""
    test.DummyProcess
    ~~~~~~~~~~~~~~~~~
    
    Dummy process implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import traceback

from pip_services_container.ProcessContainer import ProcessContainer
from .DummyFactory import DummyFactoryDescriptor
from .DummyFactory import DummyFactory

class DummyProcess(ProcessContainer):

    def _init_references(self, references):
        super(DummyProcess, self)._init_references(references)
        
        # Factory to statically resolve dummy components
        references.put(DummyFactoryDescriptor, DummyFactory())

    def run_with_args(self):
        self.run_with_config_from_args_or_file('dummy', "./config/dummy.yaml")
