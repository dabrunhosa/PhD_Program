# -*- coding: utf-8 -*-
'''
Created on December 14, 2017

@author: dabrunhosa
'''

from abc import abstractmethod
from BaseOptions import IHaveOption
from DataEntry import Options

class IData(IHaveOption):
    
    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(name = "IData",
                                  domain = None,
                                  steps = None,
                                  results = None,
                                  transient = False)
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(IDataPlot,self).__init__(whole_options,**kw)

        self.transient = False if self.steps.time is None else True

    ########################################
    ###        Private Functions         ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, IData):
            return self.domain == other.domain and\
                self.steps == other.steps and\
               len(self.results) == len(other.results)



