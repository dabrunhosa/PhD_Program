# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''

from Analytics.Base import IAnalysis
from Utilities.DataEntry import Options
from abc import abstractmethod
import sys
from Conventions.Analytics.Solutions.Base import BaseParameters as constants
from Conventions.Classes import Names,Descriptions

import numpy as np

class ISolution(IAnalysis):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions = Options(**{constants().Name: Names().ISolution,
                                      constants().Description: Descriptions().ISolution,
                                      constants().SElements: None,
                                      constants().BCs: None,
                                      constants().Solution: []})
        
        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions
        
        super(ISolution,self).__init__(options=options, defaultOptions = defaultOptions, **kw)

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

        if self.checkExistance([constants().Domain,constants().Steps]):
            if attributeName in [constants().Domain,constants().Steps] and value is not None:
                try:
                    if not self.checkDefaultValues([constants().Domain,constants().Steps]):
                        self.sElements = np.arange(self.domain.space[0], self.domain.space[-1] +
                                                         self.steps.space, self.steps.space)

                except AttributeError:
                    e = sys.exc_info()
                    print(e)
                    raise Exception(e)