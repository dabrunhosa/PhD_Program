# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:10:50 2017

@author: daniel
"""

from math import sqrt

from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Space.FEM.Integration.GaussianParameters import \
    GaussianParameters as constants
from NeuroCore.Approximations.Space.FEM.Integration.Base import IIntegration
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options


class Gaussian(IIntegration):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().GaussianQuadrature,
                                     constants().Degree: 2,
                                     constants().IntPoints: {}})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(Gaussian, self).__init__(whole_options, **kw)

        self.__calculatePoints()

    ########################################
    ###       Private Functions          ###
    ########################################

    def __setattr__(self, attributeName, value):
        super(Gaussian, self).__setattr__(attributeName, value)

        if attributeName == constants().Degree and value is not None:
            if self.degree > 3:
                raise NotImplementedError("degrees higher then 4 were not implemented.")

    def __calculatePoints(self):

        m = (1 / 2.) * (self.domain[0] + self.domain[-1])
        delta = (self.domain[-1] - self.domain[0])

        intPoints = {
            1: [[m], [delta]],

            2: [[m + (delta / 2.) * (sqrt(3) / 3.), m - (delta / 2.) * (sqrt(3) / 3.)], \
                [delta / 2., delta / 2.]],

            3: [[m + (delta / 2.) * (sqrt(3 / 5.)), m - (delta / 2.) * (sqrt(3 / 5.)), m], \
                [(5 / 18.) * delta, (5 / 18.) * delta, (8 / 18.) * delta]],

        }

        self.intPoints = intPoints[self.degree]

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def solve(self, **arguments):

        integral_value = 0

        #        print("intPoints:",self.intPoints)

        for integral_point, weight in zip(self.intPoints[0], self.intPoints[-1]):
            # print("Integral Point:", integral_point)
            integral_value += weight * arguments[constants().Function](integral_point)

        #        print("Total Integral Value:",integral_value)
        return integral_value
