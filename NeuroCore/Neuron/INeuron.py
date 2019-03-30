# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

from abc import abstractmethod
from Conventions.Classes import Names
from Conventions.NeuroCore.Neuron.Segment.Base import BaseParameters as constants
from Utilities.BaseOption import ISolvable
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options


class INeuron(ISolvable):

    ########################################
    ###           Constructor            ###
    ########################################

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().INeuron,
                                     constants().NeuronName: None,
                                     constants().GlobalConditions: None})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(INeuron, self).__init__(options=options, defaultOptions=defaultOptions, **kw)
    
    ########################################
    ###       Abstract Functions         ###
    ######################################## 
    
    @abstractmethod
    def insertSegment(self,segment):
        raise NotImplementedError
    
    @abstractmethod    
    def connectSegments(self,first_segment,second_segment,
                         first_pos=1,sec_pos=0):
        raise NotImplementedError
