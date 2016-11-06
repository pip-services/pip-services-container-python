# -*- coding: utf-8 -*-
"""
    pip_services_container.refer.ContainerReferenceSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Container references implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import traceback

from pip_services_commons.build import IFactory
from pip_services_commons.config import IConfigurable
from pip_services_commons.build import CreateException
from pip_services_commons.refer import ReferenceSet
from pip_services_commons.refer import IDescriptable
from pip_services_commons.refer import ILocateable
from pip_services_commons.refer import ReferenceException
from pip_services_commons.refer import IReferenceable
from pip_services_commons.reflect import TypeReflector

class ContainerReferenceSet(ReferenceSet):
    
    def __init__(self):
        super(ContainerReferenceSet, self).__init__()

    def _find_factory(self, locator):
        for reference in self._references:
            ref_obj = reference.get_reference()
            if isinstance(ref_obj, IFactory):
                if ref_obj.can_create(locator):
                    return ref_obj
        return None

    def _create_statically(self, locator):
        # Find factory
        factory = self._find_factory(locator)
        if factory == None:
            return None
        
        try:
            # Create component
            component = factory.create(locator)
            if component == None:
                return None
            
            # Replace locator
            if isinstance(component, IDescriptable):
                locator = component.get_descriptor()
            
            return component
        except Exception as ex:
            raise ReferenceException(None, locator).with_cause(ex)

    def _resolve_missing(self, locator):
        component = self._create_statically(locator)

        # Add to the list
        if component != None:
            self.put(component, locator)
        
        # Reference with other components
        if isinstance(component, IReferenceable):
            component.set_references(self)
        
        return component

    def put_from_config(self, config):
        for component_config in config:
            component = None
            locator = None

            try:
                # Create component dynamically
                if component_config.type != None:
                    locator = component_config.type
                    component = TypeReflector.create_instance_by_descriptor(component_config.type)
                # Or create component statically
                elif component_config.descriptor != None:
                    locator = component_config.descriptor
                    component = self._create_statically(component_config.descriptor)

                # Check that component was created
                if component == None:
                    raise CreateException(
                        "CANNOT_CREATE_COMPONENT", "Cannot create component"
                    ).with_details("config", config)

                # Add component to the list
                if isinstance(component, ILocateable) or isinstance(component, IDescriptable):
                    self.put(component)
                else:
                    self.put(component, locator)
                
                # Configure component
                if isinstance(component, IConfigurable):
                    component.configure(component_config.config)
            except Exception as ex:
                raise ReferenceException(None, locator).with_cause(ex)
