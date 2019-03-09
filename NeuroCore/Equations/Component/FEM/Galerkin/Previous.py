# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:11:35 2017

@author: daniel
"""
from abc import ABC

from Conventions.Classes import Components
from Conventions.NeuroCore.Equation.Components.FEM.Base import FEMBaseParameters as constants
from NeuroCore.Equations.Component.FEM.Base import IFEM
from Utilities.DataEntry import Options


class Previous(IFEM, ABC):
    '''A class to define the term reaction to be used
    by the Galerkin Approximation.'''

    ########################################
    ###          Constructor             ###
    ########################################

    # '''The actual real constructor of the classes in Python. '''
    # def __new__(cls, *args, **kwargs):
    #     pass

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        '''Class initializer. Use it's Base Class initializer
        and adds the weight function to be used. '''

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Components().Time,
                                   constants().Previous: None})

        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions

        super(Previous, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ########################################        

    def __call__(self, **arguments):

        if Components().Time in arguments.keys():
            self.previous = arguments[Components().Time]

        return super(Previous, self).__call__(**arguments)

    '''A class to create a term based on the basic terms.
    This class can be used in runtime or for the developer 
    to define a new term.'''

    def build_function(self, x):
        '''Method used by the call method to be able to
        create the composed term. It requires the position
        x and returns the total value to the user.'''

        finalValue = 0.0

        for line in range(self.weightFunction.numLocalNodes):
            finalValue += self.coeff(x) * self.previous[line] * \
                          self.weightFunction.function(line)(x) * \
                          self.weightFunction.function(self.column)(x)

        return finalValue
