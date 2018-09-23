
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:59:15 2017

@author: Daniel Abrunhosa
"""
from abc import ABC

from NeuroCore.Equations.Component.FEM.Base import IFEM
from NeuroCore.Equations.Conventions import Components
from Utilities.DataEntry import Options

# Actually the thing is to make all the Components() again
# but with NonLinear Coefficients. Because that's basically
# what my reaction of the HH Model is.  

class NonLinear(IFEM, ABC):
    '''A class to define the term reaction to be used
    by the Galerkin Approximation.'''
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,component,options=Options(), defaultOptions = Options(), **kw):
        '''Class initializer. Use it's Base Class initializer
        and adds the weight function to be used. '''
        
        # Define the default options
        inDefaultOptions =Options(name = "NonLinear" + component.name,
                                  inComponent = component,
                                  discreteElements = {})
                                     
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(Discrete,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
        
    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __call__( self,**arguments):

        if Components().Discrete in arguments.keys():
            self.discreteElements = arguments[Components().Discrete]

        return super(Discrete,self).__call__(**arguments)
    
    def build_function(self, x):
        '''A method used by the call method to return 
        the definition of the function in a given x.'''

        finalValue = 0.0
        inComponentValue = self.inComponent(line = self.line,\
                                        column = self.column,\
                                        domain = self.domain)(x)

        for value in range(self.discreteElements.values()):
            finalValue += value[self.line]*inComponentValue
        
        return finalValue