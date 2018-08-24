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

    def __init__(self,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(name = "IData",
                                  enriched = None)
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(FEMData,self).__init__(whole_options,**kw)

    ########################################
    ###        Private Functions         ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, FEMData):
            return super(FEMData,self).__eq__(self, other)\
               and len(self.enriched) == len(other.enriched)



