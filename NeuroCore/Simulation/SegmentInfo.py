# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:33:22 2017

@author: daniel
"""

import string

from Utilities.DataEntry import Options, Options_User


class Segment_Info(object):
    
    ########################################
    ###       Private Variables          ###
    ######################################## 
    
    # All the attributes allowed to be access.
    class_attributes = ['connected','boundary','continuity',
                        'derivative','processing','column',
                        'nodes_handled']
    
    # Class to threat the Option Class 
    class_option = Options_User()
    
    ########################################
    ###       Private Functions          ###
    ######################################## 
    
    def __init__(self):         
        
        # Define the class options
        class_options = Options(connected = list(),
                                boundary = Set('Boundary'),
                                continuity = Set('Continuity'),
                                derivative = Set('Derivative'),
                                nodes_handled = list())
        
        # Initialize the options
        self.class_option.init_options(self,class_options,{})
        
    def __setattr__(self,attributeName,value):
        
        # Check if the given attribute is 
        # an allowed one.
        if attributeName in self.class_attributes:
            # If it's add it to the internal
            # dictionary
            self.__dict__[attributeName] = value
        else:
            error_message = "The attribute: '"+attributeName+ \
                            "' is not an allowed attribute to set."
            
            raise AttributeError(error_message)
        
    def __getattr__(self,attributeName):
        
        if attributeName in self.class_attributes:
            return self.__dict__[attributeName]
        elif attributeName == 'options':
            return self.class_attributes
        else:
            error_message = "The attribute name: "+attributeName+ \
                            " is not an allowed attribute to get."
            raise AttributeError(error_message)
        
    def items(self): 
        """ Return a list containing all items as tuples """
        return self.__dict__.items()
        
    def __repr__(self): 
        """Handle the print statement and shows a nicer
        string then the original."""
        elems = map(repr,self.items()) 
        return "(%s)" % (string.join(elems, ', '))