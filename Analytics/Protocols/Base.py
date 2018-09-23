# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:22:10 2017

@author: daniel
"""

from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options
from Analytics.Protocols.BaseData import IDataAnalysed
from itertools import product

class TestProtocols(IHaveOption):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
         # Define the default options
        inDefaultOptions =Options(name = "IProtocol",
                                       dataToBeAnalysed = IDataAnalysed(),
                                       data = None)
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(TestProtocols,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
    
    ########################################
    ###       Private Functions          ###
    ######################################## 
                
    def __iter__(self):
        return self.data
    
    def __createIterableData(self):
        
        iterableData = []
        
        for attribute in self.dataToBeAnalysed.analysedAttributes:
            iterableData.append(self.dataToBeAnalysed.__dict__[attribute])
            
        self.data = list(product(*iterableData))