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

    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name = "IData",
                                  domain = None,
                                  steps = None,
                                  results = None,
                                  transient = False)
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(IDataPlot,self).__init__(options=options, defaultOptions = defaultOptions, **kw)

        self.transient = False if self.steps.time is None else True

    ########################################
    ###        Private Functions         ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, IData):
            return self.domain == other.domain and\
                self.steps == other.steps and\
               len(self.results) == len(other.results)



