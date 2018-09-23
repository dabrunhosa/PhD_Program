# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 04:59:12 2017

@author: daniel
"""

# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from abc import ABC

from Conventions.Classes import Names
from Conventions.Parameters import Parameters as constants
from Utilities.BaseOption import ISolvable
from Utilities.DataEntry import Options


class IIntegration(ISolvable, ABC):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().GenericIntegration,
                                     constants().Domain: [-1, 1]})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(IIntegration, self).__init__(options=options, defaultOptions = defaultOptions, **kw)
