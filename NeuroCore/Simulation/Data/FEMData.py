# -*- coding: utf-8 -*-
'''
Created on December 14, 2017

@author: dabrunhosa
'''

from abc import abstractmethod
from Simulation.Data.IData import IData
from DataEntry import Options

class FEMData(IData):
    
    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name = "IData",
                                  enriched = None)
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(FEMData,self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###        Private Functions         ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, FEMData):
            return super(FEMData,self).__eq__(self, other)\
               and len(self.enriched) == len(other.enriched)



