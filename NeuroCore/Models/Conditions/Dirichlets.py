# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:50:13 2017

@author: Daniel Abrunhosa
"""

from Conventions.Classes import Names
from Conventions.NeuroCore.Models.Conditions.Base import BaseParameters as constants
from NeuroCore.Models.Conditions.Base import ICondition
from Utilities.DataEntry import Options


class Dirichlet(ICondition):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().Dirichlet,
                                   constants().BcValue: 1.0,
                                   constants().BcType: constants().Dirichlet})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(Dirichlet, self).__init__(options=options, defaultOptions = defaultOptions, **kw)


'''
The holding of Electrical Potential at some
fixed level. So that: V(0 or L) = Vc
'''


class VoltageClamp(Dirichlet):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, bcValue, options=Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().VoltageClamp,
                                   constants().BcValue: bcValue})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(VoltageClamp, self).__init__(options=options, defaultOptions = defaultOptions, **kw)


class KilledEnd(Dirichlet):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().KilledEnd,
                                   constants().BcValue: 0.0})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(KilledEnd, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __setattr__(self, attributeName, value):

        if attributeName == constants().BcValue and value != 0.0:
            error_message = "The Killed-End Boundary Condition \
                            can't have the value modified. By definition \
                            the value is 0 (zero)"
            raise AttributeError(error_message)
        else:
            super(KilledEnd, self).__setattr__(attributeName, value)
