# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:59:04 2017

@author: Daniel Abrunhosa
"""
from abc import ABC

from Conventions.Classes import Components
from Conventions.NeuroCore.Equation.Components.FEM.Base import FEMBaseParameters as constants
from NeuroCore.Equations.Component.FEM.Base import IFEM
from Utilities.DataEntry import Options


class Diffusion(IFEM, ABC):
    '''A class to define the term diffusion to be used
    by the Galerkin Approximation.'''

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        '''Class initializer. Use it's Base Class initializer
        and adds the weight function to be used. '''

        # Define the default options
        default_options = Options(**{constants().Name: Components().Diffusion})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(Diffusion, self).__init__(whole_options, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def build_function(self, x):
        '''A method used by the call method to return 
        the definition of the function in a given x.'''

        return self.coeff(x) * self.weightFunction.diffFunction(self.line)(x) * \
               self.weightFunction.diffFunction(self.column)(x)
