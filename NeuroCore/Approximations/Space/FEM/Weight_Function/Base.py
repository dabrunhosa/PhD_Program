# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 06:18:44 2017

@author: daniel
"""

from abc import abstractmethod

from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Space.FEM.Elements.IElementParameters import IElementParameters as constants
from Utilities.BaseOption import IHaveOption
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options

'''
This class in reality defines a collection of Weight Function
as is commonly defined in Finite Element Methods.
All the weight functions are defined in the reference
element [-1,1], because it makes a lot of 
calculations easier and can be done once for 
the whole domain.
'''


class IWeightFunction(IHaveOption):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().WeightFunction,
                                     constants().NumLocalNodes: None})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(IWeightFunction, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Abstract Functions         ###
    ######################################## 

    '''
    Choice define wich of the weight functions is 
    going to be used
    '''

    @abstractmethod
    def function(self, choice):
        raise NotImplementedError

    @abstractmethod
    def diffFunction(self, choice):
        raise NotImplementedError
