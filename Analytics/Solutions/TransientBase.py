# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''
from abc import ABC

from Analytics.Solutions.ISolution import ISolution
from Conventions.Analytics.Solutions.Validations.Transient import TransientParameters as constants
from Conventions.Classes import Names, Descriptions
from Utilities.DataEntry import Options


class TransientBase(ISolution, ABC):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().TransientBaseClass,
                                     constants().SElements: None,
                                     constants().BCs: None,
                                     constants().Solution: [],
                                     constants().Description: Descriptions().TransientBaseClass})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(TransientBase, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Public Functions           ###
    ########################################

    def createFont(self):

        def fontFunction(x,t):
            return 0.0

        return fontFunction