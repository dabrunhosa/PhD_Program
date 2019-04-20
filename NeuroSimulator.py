# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 05:34:15 2017

@author: daniel
"""

# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

########################################
###           Packages               ###
######################################## 

from Neuron.Segment import ISegment
from Utilities.DataEntry import Options
from Neuron.NetXNeuron import NetX_Neuron
from Models.CableModel import Cable_Model
from Approximations.GalerkinApproximation import GalerkinApproximation
from Approximations.FEM.Weight_Function import LinearLagrange
from Approximations.FEM.Integration import Gaussian
from Approximations.ODESolver import BackwardEuler
from Models.Conditions import Dirichlet
from Utilities.DataEntry import Options,Options_User
from BaseOption import BaseOption

import numpy
import math
import time

class NeuroSimulator(BaseOption):
    
    ########################################
    ###       Private Variables          ###
    ######################################## 
    
    # All the attributes allowed to be access.
    class_attributes = ['name']
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
         # Define the default options
        inDefaultOptions =Options(name = "Default",
                                  neuron = NetX_Neuron())
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        # Initialize the options and the extra arguments
        self.class_option.init_options(self,whole_options,kw)
        
        self.__prepareClasses()
   
    ########################################
    ###       Class Functions            ###
    ######################################## 

    @classmethod
    def version(self): return "1.0"
    
    ########################################
    ###       Private Functions          ###
    ######################################## 
        
        
    ########################################
    ###       Public Functions           ###
    ########################################
    
    def createSegment(self,length,model,name):
        return [ISegment(length=length,imodel=model,name=name)]
    
    def insert_segment(self,segment):
        self.neuron.insert_segment(segment)
       
    def connect_segments(self,first_segment,second_segment,first_pos=1,sec_pos=0):
        self.neuron.connect_segments(first_segment,second_segment,first_pos,sec_pos)
    
    def identify_boundary_conditions(self):          
        return self.__define_boundary_conditions()
    
    def solve(self,boundary_conditions,delta_t,final_time):
        
        for region in self.__regions:
            region.solve(boundary_conditions,delta_t,final_time)
