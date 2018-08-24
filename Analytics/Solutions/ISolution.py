# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''

from Analytics.Base import IAnalysis
from Utilities.DataEntry import Options
from abc import abstractmethod
import sys

import numpy as np

class ISolution(IAnalysis):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(name="ISolution",
                                  description="A Solution Interface",
                                  sElements=None,
                                  BCs=None,
                                  solution=[])
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(ISolution,self).__init__(whole_options,**kw)

    ########################################
    ###       Abstract Functions         ###
    ########################################

    # @abstractmethod
    # def createInitialCondition(self):
    #     return NotImplementedError

    @abstractmethod
    def createFont(self):
        return NotImplementedError
    
    ######################################## 
    ###       Private Functions          ###
    ########################################
    
    def __setattr__(self, attributeName, value):
        
        super(ISolution,self).__setattr__(attributeName,value)
        if (attributeName == "domain" or attributeName == "steps") and value is not None:
            
            try:
                getattr(self, "domain")
                getattr(self, "steps")
                
                if self.domain is not None and self.steps is not None:
                    self.sElements = np.arange(self.domain.space[0], self.domain.space[-1] +
                                                     self.steps.space, self.steps.space)
                
            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)