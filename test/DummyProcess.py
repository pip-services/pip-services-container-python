# -*- coding: utf-8 -*-
"""
    test.DummyProcess
    ~~~~~~~~~~~~~~~~~
    
    Dummy process implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import os
import traceback

from pip_services_container.ProcessContainer import ProcessContainer
from pip_services_commons.log import ConsoleLogger
from .DummyFactory import DummyFactory

class DummyProcess(ProcessContainer):

    def _init_references(self, references):
        super(DummyProcess, self)._init_references(references)
        
        # Factory to statically resolve dummy components
        references.put(DummyFactory())

    def launch(self):
        self.run_with_config_from_args('dummy', "./config/dummy.yaml")


if __name__ == '__main__':
    runner = DummyProcess()
    try:
        runner.launch()
    except Exception as ex:
        ConsoleLogger().fatal("dummy", ex, "Error: ")
        #print(traceback.format_exc(ex))
        #sys.stderr.write(str(e) + '\n')