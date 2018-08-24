# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:30:09 2017

@author: daniel
"""

from abc import abstractmethod

from Conventions.Classes import Names
from Conventions.NeuroCore.Equation.IEquation import IEquationParameters as constants
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options


class IEquation(IHaveOption):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Name: Names().Equation,
                                   constants().Coeffs: {}})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IEquation, self).__init__(whole_options, **kw)

    ########################################
    ###       Abstract Functions         ###
    ######################################## 

    @abstractmethod
    def __call__(self):
        '''Adds support for the call operation'''
        raise NotImplementedError

    @abstractmethod
    def __build_function(self, x):
        '''The required function to be implemented
         by the class that inherit this one.'''
        raise NotImplementedError
