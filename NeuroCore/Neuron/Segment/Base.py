# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:44:13 2017

@author: daniel
"""

from Conventions.NeuroCore.Neuron.Segment.Base import BaseParameters as constants
from Utilities.BaseOption import ISolvable
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options


class ISegment(ISolvable):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, name, localConditions, domain, steps, iModel, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Domain: domain,
                                     constants().Steps: steps,
                                     constants().Name: name,
                                     constants().LocalConditions: localConditions,
                                     constants().IModel: iModel})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(ISegment, self).__init__(whole_options, **kw)

        self.iModel.domain = self.domain
        self.iModel.BCs = self.localConditions
        self.iModel.steps = self.steps

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def solve(self, **arguments):
        return self.iModel.solve(**arguments)
