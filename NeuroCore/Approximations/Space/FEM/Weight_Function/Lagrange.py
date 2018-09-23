# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 06:47:12 2017

@author: daniel
"""

from abc import abstractmethod

from Conventions.NeuroCore.Approximations.Space.FEM.Weight_Function.Lagrange import LagrangeParameters as constants
from NeuroCore.Approximations.Space.FEM.Weight_Function.Base import IWeightFunction
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options


class Lagrange(IWeightFunction):
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
        inDefaultOptions =Options(**{constants().NumLocalNodes: None,
                                     constants().Degree: None,
                                     constants().DiffWeightFunction: [],
                                     constants().WeightFunction: []})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(Lagrange, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

        self._create_weight_functions()

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def diffFunction(self, choice):
        return self.diffWeightFunction[choice]

    def function(self, choice):
        #         print "Weight",choice,[self.x_values[0],self.x_values[1]]
        return self.weightFunction[choice]

    ########################################
    ###       Abstract Functions         ###
    ######################################## 

    @abstractmethod
    def _create_weight_functions(self):
        pass
