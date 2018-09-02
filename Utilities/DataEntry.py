# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

from Conventions.Variables import Variables
import sys
    
class Options(dict):
    """A form to more elegantly allow for default parameters
    to be set by the user. It also let's these parameters be
    changed when used in different context."""
    
    def __init__(self, **kw):
        """Initialize the default parameters with a dictionary"""        
        self.__dict__.update(kw)
        
    def __lshift__(self, other): 
        """A form to define a new set of parameters based
        in one already defined. Can be 
        overloading operator << """ 
        s = self.__copy__( ) 
        s.__dict__.update(other.__dict__) 
        
        return s
    
    def __iter__(self):
        return self.__dict__

    def __getitem__(self, item):
        return self.__dict__[item]

    def __getattr__(self,attributeName):

        if attributeName == Variables().Names:
            return self.__dict__.keys()
        else:
            error_message = "The attribute name: "+attributeName+ \
                            " is not an allowed attribute to get."
            raise AttributeError(error_message)
    
    def __copy__(self): 
        """Support for the copy statement"""
        return self.__class__(**self.__dict__)
    
    def __repr__(self): 
        """Handle the print statement and shows a nicer
        string then the original."""
#        elems = map(repr,self.__dict__.items()) 
        return str(self.__dict__.items())
#        return "%s(%s)" % ("Options",str.join(elems, ', '))

class Options_User(object): 
    
    """ Base class for classes that need to use options"""
    class OptionError(AttributeError): pass
    
    def init_options(self,requested_class,option, kw):
        """To be called from the class constructor.
        Puts the options into objects scope."""
        
        for k, v in option.__dict__.items():
            try:
                setattr(requested_class,k,v)
            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)
                
        for k, v in kw.items():
            try:
                setattr(requested_class,k,v)
            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)
            
    def reconfigure(self,requested_class,option=Options(), **kw): 
        """ used to change options during object life """ 
        self.init_options(requested_class,option, kw) 
        self.on_reconfigure()
        
    def on_reconfigure(self): 
        """ To be overloaded by derived classes. Called by
        the reconfigure method or from outside after direct 
        changes to option attributes. """
        pass


