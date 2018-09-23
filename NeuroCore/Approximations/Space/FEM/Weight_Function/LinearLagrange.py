# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 07:30:55 2017

@author: daniel
"""

from Conventions.NeuroCore.Approximations.Space.FEM.Weight_Function.Lagrange import LagrangeParameters as constants
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from NeuroCore.Approximations.Space.FEM.Weight_Function.Lagrange import Lagrange
from Utilities.DataEntry import Options


class Linear_Lagrange(Lagrange):
    ########################################
    ###           Constructor            ###
    ######################################## 

    '''
    The Weight Function are going to be defined in the Reference Element
    [-1,1] so the x_values are not going to be passed as a parameter
    anymore. Note that is easy to flip the switch back. 
    '''

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().NumLocalNodes: 2,
                                     constants().Degree: 1,
                                     constants().DiffWeightFunction: [],
                                     constants().WeightFunction: []})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(Linear_Lagrange, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def _create_weight_functions(self):
        self.weightFunction.append(lambda qsi: (1 + qsi) / 2)
        self.weightFunction.append(lambda qsi: (1 - qsi) / 2)

        self.diffWeightFunction.append(lambda qsi: 1 / 2)
        self.diffWeightFunction.append(lambda qsi: -1 / 2)
