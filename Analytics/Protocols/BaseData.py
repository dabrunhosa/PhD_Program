# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:21:01 2017

@author: Daniel Abrunhosa
"""

from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options
from Analytics.Protocols.Conventions import DataAnalysed

class IDataAnalysed(IHaveOption):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), **kw): 
        
        self.__dict__['allowedAttributes'] = [DataAnalysed().Diffusion,\
                                                       DataAnalysed().Reaction,\
                                                       DataAnalysed().Time,
                                                       DataAnalysed().spaceSteps,
                                                       DataAnalysed().timeSteps]
        
         # Define the default options
        default_options = Options(name = "IDataAnalysed",
                                  diffusion = None,
                                  reaction = None,
                                  time = None,
                                  spaceDomain = None,
                                  spaceSteps = None,
                                  timeDomain = None,
                                  timeSteps = None,
                                  analysedAttributes = [])
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(IDataAnalysed,self).__init__(whole_options,**kw) 
        
#        self.__dict__["class_attributes"].extend(self.__dict__['allowedAttributes'])
        
    ########################################
    ###       Private Functions          ###
    ######################################## 
            
    def __setattr__(self,attributeName,value):
        
        if attributeName in self.__dict__['allowedAttributes'] and value is not None:
            if type(value) != list:
                error_message = "The attribute: "+attributeName+ \
                                "has to be a list."
                
                raise AttributeError(error_message) 
            else:
                self.analysedAttributes.append(attributeName)
            
        super(IDataAnalysed,self).__setattr__(attributeName,value)