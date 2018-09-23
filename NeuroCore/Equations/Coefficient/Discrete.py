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
    
    def __init__(self,userCoeff,options=Options(), defaultOptions = Options(), **kw):
        
         # Define the default options
        inDefaultOptions =Options(name = "Discrete",
                                  positionCalculations = {})
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(Discrete,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
    
    ########################################
    ###       Private Functions          ###
    ########################################  

    def __call__( self,**arguments):
        return NotImplementedError()


class HH(ICoefficient, ABC):
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,userCoeff,options=Options(), defaultOptions = Options(), **kw):
        
         # Define the default options
        inDefaultOptions =Options(name = "Discrete",
                                  positionCalculations = {})
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(HH,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
    
    ########################################
    ###       Private Functions          ###
    ########################################  

    def __call__( self,**arguments):
        return NotImplementedError()