# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:59:22 2017

@author: Daniel Abrunhosa
"""
from abc import ABC

from Conventions.Classes import Components
from Conventions.NeuroCore.Equation.Components.FEM.Base import FEMBaseParameters as constants
from NeuroCore.Equations.Component.FEM.Base import IFEM
from Utilities.DataEntry import Options


class Font(IFEM, ABC):
    '''A class to define the term reaction to be used
    by the Galerkin Approximation.'''

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        '''Class initializer. Use it's Base Class initializer
        and adds the weight function to be used. '''

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Components().Font,
                                   constants().Font: None})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(Font, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def build_function(self, x):
        '''A method used by the call method to return 
        the definition of the function in a given x.'''

        return self.coeff(x) * self.font(x) * \
               self.weightFunction.function(self.line)(x)
