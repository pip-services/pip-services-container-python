# -*- coding: utf-8 -*-
"""
    test.DummyController
    ~~~~~~~~~~~~~~~~~~~~
    
    Dummy controller implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.refer import IReferenceable
from pip_services_commons.config import IReconfigurable
from pip_services_commons.run import IOpenable
from pip_services_commons.run import IClosable
from pip_services_commons.run import INotifiable
from pip_services_commons.run import FixedRateTimer
from pip_services_commons.log import CompositeLogger

class DummyController(object, IReferenceable, IReconfigurable, IOpenable, IClosable, INotifiable):
    _timer = None
    _logger = None
    _message = None
    _counter = None

    def __init__(self):
        self._message = "Hello World!"
        self._logger = CompositeLogger()
        self._timer = FixedRateTimer(self, 1000, 1000)
        self._counter = 0

    def configure(self, config):
        self._message = config.get_as_string_with_default("message", self._message)

    def set_references(self, references):
        self._logger.set_references(references)

    def open(self, correlation_id):
        self._timer.start()
        self._logger.trace(correlation_id, "Dummy controller opened")

    def close(self, correlation_id):
        self._timer.stop()
        self._logger.trace(correlation_id, "Dummy controller closed")

    def notify(self, correlation_id):
        self._logger.info(correlation_id, str(self._counter) + " - " + self._message)
        self._counter += 1
