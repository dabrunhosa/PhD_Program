'''
Created on May 29, 2014

@author: dabrunhosa
'''
from abc import ABC

from Conventions.Classes import Names
from Conventions.NeuroCore.Equation.Components.Base import BaseParameters as constants
from NeuroCore.Equations.IEquation import IEquation
from Utilities.DataEntry import Options
from Utilities.Handler import Function


class IComponent(IEquation, ABC):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        '''Class initializer. Use it's Base Class initializer
        and adds the weight function to be used. '''

        # Define the default options
        default_options = Options(**{constants().Name: Names().Component,
                                   constants().Coeff: None})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IComponent, self).__init__(whole_options, **kw)

        ########################################

    ###       Private Functions          ###
    ######################################## 

    def __setattr__(self, attributeName, value):
        if attributeName == constants().Coeff and value is not None:
            value = Function(value)

        super(IComponent, self).__setattr__(attributeName, value)
