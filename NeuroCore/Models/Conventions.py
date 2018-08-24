# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:31:16 2017

@author: Daniel Abrunhosa
"""

from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options

class Domains(IHaveOption):
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,space,time=None,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(name = "Domain",
                                       space = space,
                                       time = time)
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(Domains,self).__init__(whole_options,**kw)
        
    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, Domains):
            return self.space == other.space and self.time == other.time

    def __repr__(self):
        return "Space: " + str(self.space) + "\n Time :"+ str(self.time)
            
    def __setattr__(self,attributeName,value):
        
        if (attributeName == "space" or attributeName == "time") and value is not None:
            
             if type(value) != list:
                error_message = "The "+attributeName+" domain has to be a list"
                raise AttributeError(error_message)
        
        super(Domains,self).__setattr__(attributeName,value)
        
class Steps(IHaveOption):
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,space,time=None,options=Options(), **kw):
        
         # Define the default options
        default_options = Options(name = "Steps",
                                       space = space,
                                       time = time)
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(Steps,self).__init__(whole_options,**kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, Steps):
            return self.space == other.space and self.time == other.time

    def __repr__(self):
        return "Space: " + str(self.space) + "\n Time :"+ str(self.time)