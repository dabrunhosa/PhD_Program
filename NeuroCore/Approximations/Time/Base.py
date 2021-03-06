# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 09:16:22 2017

@author: daniel
"""

from abc import abstractmethod

from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Time.Base import BaseParameters as constants
from Utilities.BaseOption import ISolvable
from Utilities.DataEntry import Options

()


class IApproximation(ISolvable):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Name: Names().TimeApproximation,
                                     constants().Disturbance: {},
                                     constants().CoeffT: None,
                                     constants().Font: 1.0,
                                     constants().Reaction: 1.0,
                                     constants().Step: None})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IApproximation, self).__init__(whole_options, **kw)

    ########################################
    ###       Abstract Functions          ###
    ######################################## 

    @abstractmethod
    def modifyCoeff(self, coeffName, value):
        return NotImplementedError
