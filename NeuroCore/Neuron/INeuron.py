# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

from abc import abstractmethod
from Utilities.DataEntry import Options
from Utilities.BaseOption import IHaveOption

class INeuron(IHaveOption):
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
         # Define the default options
        self.inDefaultOptions =Options(name = "Neuron")
        
        # Merge the default options and the user generated options
        whole_options = self.default_options << options
        
        # Initialize the options and the extra arguments
        self.class_option.init_options(self,whole_options,kw)
    
    ########################################
    ###       Abstract Functions         ###
    ######################################## 
    
    @abstractmethod
    def insert_segments(self,segment):
        raise NotImplementedError
    
    @abstractmethod    
    def connect_segments(self,first_segment,second_segment,
                         first_pos=1,sec_pos=0):
        raise NotImplementedError 
        
    @abstractmethod
    def solve(self,timeApproximation=None):
        raise NotImplementedError
