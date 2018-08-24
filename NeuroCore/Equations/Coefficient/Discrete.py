# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21

@author: Daniel Abrunhosa
"""
from abc import ABC

from Utilities.DataEntry import Options
from NeuroCore.Equations.Coefficient.Base import ICoefficient
from NeuroCore.Equations.Coefficient.Conventions import CoeffId
import inspect

class Discrete(ICoefficient, ABC):
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,userCoeff,options=Options(), **kw):
        
         # Define the default options
        default_options = Options(name = "Discrete",
                                  positionCalculations = {})
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(Discrete,self).__init__(whole_options,**kw)
    
    ########################################
    ###       Private Functions          ###
    ########################################  

    def __call__( self,**arguments):
        return NotImplementedError()


class HH(ICoefficient, ABC):
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,userCoeff,options=Options(), **kw):
        
         # Define the default options
        default_options = Options(name = "Discrete",
                                  positionCalculations = {})
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(HH,self).__init__(whole_options,**kw)
    
    ########################################
    ###       Private Functions          ###
    ########################################  

    def __call__( self,**arguments):
        return NotImplementedError()