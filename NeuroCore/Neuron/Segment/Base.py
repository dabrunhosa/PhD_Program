# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:44:13 2017

@author: daniel
"""

from Conventions.Classes import Names
from Conventions.NeuroCore.Neuron.Segment.Base import BaseParameters as constants
from Utilities.BaseOption import ISolvable
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options
from NeuroCore.Models.Base import IModel


class ISegment(ISolvable):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Domain: None,
                                     constants().Steps: None,
                                     constants().Name: Names().ISegment,
                                     constants().SegmentName: None,
                                     constants().LocalConditions: None,
                                     constants().IModel: []})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(ISegment, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ########################################

    def __setattr__(self, attributeName, value):
        super(ISegment, self).__setattr__(attributeName, value)

        if self.checkExistance([constants().Domain, constants().LocalConditions,
                                        constants().Steps, constants().IModel]):
            if not self.checkDefaultValues([constants().Domain, constants().LocalConditions,
                                            constants().Steps, constants().IModel]):

                if isinstance(value,list):
                    for model in value:
                        model.domain = self.domain
                        model.steps = self.steps
                        model.BCs = self.localConditions
                elif isinstance(value,IModel):
                    value = [value]
                    setattr(self,constants().IModel,value)

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def solve(self, **arguments):
        results = []
        for model in self.iModel:
            results.append(model.solve(**arguments))

        return results
