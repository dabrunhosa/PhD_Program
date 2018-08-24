# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:10:37 2017

@author: daniel
"""

from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Space.FEM.Integration.TrapezoidalParameters import \
    TrapezoidalParameters as constants
from NeuroCore.Approximations.Space.FEM.Integration.Base import IIntegration
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options


class Trapezoidal(IIntegration):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Name: Names().Trapezoidal,
                                     constants().NumPoints: 2})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(Trapezoidal, self).__init__(whole_options, **kw)

    ########################################
    ###       Abstract Functions         ###
    ######################################## 

    def solve(self, **arguments):
        deltaX = (self.domain[-1] - self.domain[0]) / float(self.numberPoints)
        Integral = arguments[constants().Function](self.domain[0]) + \
                   arguments[constants().Function](self.domain[-1])

        for k in range(1, self.numberPoints + 1, 1):
            x = self.domain[0] + k * deltaX
            Integral += 2 * arguments[constants().Function](x)

        Integral *= deltaX / 2
        return Integral
