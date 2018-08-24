# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:59:15 2017

@author: Daniel Abrunhosa
"""
from abc import ABC

from NeuroCore.Equations.Component.FEM.Base import IFEM
from Conventions.Classes import Components
from Conventions.NeuroCore.Equation.Components.FEM.Base import FEMBaseParameters as constants
from Utilities.DataEntry import Options

class Reaction(IFEM, ABC):
    '''A class to define the term reaction to be used
    by the Galerkin Approximation.'''
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,options=Options(), **kw):
        '''Class initializer. Use it's Base Class initializer
        and adds the weight function to be used. '''
        
        # Define the default options
        default_options = Options(**{constants().Name:Components().Reaction})
                                     
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(Reaction,self).__init__(whole_options,**kw)
        
    ########################################
    ###       Private Functions          ###
    ######################################## 
    
    def build_function(self, x):
        '''A method used by the call method to return 
        the definition of the function in a given x.'''
        
        value = self.coeff(x)*self.weightFunction.function(self.line)(x)*\
                            self.weightFunction.function(self.column)(x)
        
#        print("Reaction:",value," with:",x)
        
        return value