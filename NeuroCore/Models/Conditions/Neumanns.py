# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:50:01 2017

@author: Daniel Abrunhosa
"""

from math import pi

from Conventions.Classes import Names
from Conventions.NeuroCore.Models.Conditions.Base import BaseParameters as constants
from Conventions.NeuroCore.Models.Conditions.CurrentInjection import CurrentParameters as currentConstanst
from NeuroCore.Models.Conditions.Base import ICondition
from Utilities.DataEntry import Options
from Utilities.Handler import Function


class Neumann(ICondition):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().Neumann,
                                   constants().BcValue: 1.0,
                                   constants().BcType: constants().Neumann})

        # Merge the default options and the user generated options
        .
				 defaultOptions = inDefaultOptions << defaultOptions

        super(Neumann, self).__init__(options=options, defaultOptions = defaultOptions, **kw)


class SealedEnd(Neumann):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().SealedEnd,
                                   constants().BcValue: 0.0})

        # Merge the default options and the user generated options
        .
				 defaultOptions = inDefaultOptions << defaultOptions

        super(SealedEnd, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

        ########################################

    ###       Private Functions          ###
    ######################################## 

    def __setattr__(self, attributeName, value):

        if attributeName == constants().BcValue and value != 0.0:
            error_message = "The Sealed-End Boundary Condition \
                            can't have the value modified. By definition \
                            the value is 0 (zero)"
            raise AttributeError(error_message)
        else:
            super(SealedEnd, self).__setattr__(attributeName, value)


class CurrentInjection(Neumann):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options({currentConstanst().Name: Names().CurrentInjection,
                                   currentConstanst().Diameter: None,
                                   currentConstanst().ResistanceL: None,
                                   currentConstanst().Current: None,
                                   currentConstanst().BcValue: 1.0})

        # Merge the default options and the user generated options
        .
				 defaultOptions = inDefaultOptions << defaultOptions

        super(CurrentInjection, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

        ########################################

    ###       Private Functions          ###
    ######################################## 

    def __setattr__(self, attributeName, value):

        if attributeName is currentConstanst().Current:
            value = Function(value)

        super(CurrentInjection, self).__setattr__(attributeName, value)

        if self.diameter is not None and self.resistanceL is not None and self.current is not None:
            self.value = ((4 * self.resistanceL) / (pi * pow(self.diameter, 2))) * self.current
