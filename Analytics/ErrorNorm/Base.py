# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:14:55 2017

@author: daniel
"""

from abc import abstractmethod
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options

class IErrorNorm(IHaveOption):
    
    ########################################
    ###           Constructor            ###
    ######################################## 
    
    def __init__(self,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(name = "Error Norm",
                                       u = None,
                                       uh = None,
                                       coeff_v = None,
                                       coeff_font = None)
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(IErrorNorm,self).__init__(whole_options,**kw) 
    
    ########################################
    ###       Abstract Functions         ###
    ########################################
    
    @abstractmethod
    def calculate(self):
        raise NotImplementedError
        
    @abstractmethod
    def write(self,outFile):
        raise NotImplementedError