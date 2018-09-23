# -*- coding: utf-8 -*-
'''
Created on September 4, 2017

@author: dabrunhosa
'''
from abc import ABC

from fenics import IntervalMesh

from Analytics.Base import IAnalysis
from Conventions.Analytics.FEniCS.Base import FEniCSBaseParameters as constants
from Conventions.Classes import Names, Descriptions
from Utilities.DataEntry import Options
import sys


class IProblem(IAnalysis, ABC):

    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().IProblem,
                                   constants().Description: Descriptions().IProblem,
                                   constants().SpatialSteps: None,
                                   constants().Mesh: None,
                                   constants().BCs: None})

        # Merge the default options and the user generated options
        .
				 defaultOptions = inDefaultOptions << defaultOptions

        super(IProblem, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

        ########################################

    ###       Private Functions          ###
    ########################################

    def __setattr__(self, attributeName, value):

        super(IProblem, self).__setattr__(attributeName, value)

        if (attributeName == constants().Domain or attributeName == constants().Steps) and value is not None:

            try:
                self.checkExistance(constants().Domain)
                self.checkExistance(constants().Steps)

                if self.domain is not None and self.steps is not None:
                    # define Spatial steps
                    self.spatialSteps = int(self.domain.space[-1] / self.steps.space)
                    # definig mesh
                    self.mesh = IntervalMesh(self.spatialSteps, \
                                             self.domain.space[0], \
                                             self.domain.space[-1])

            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)
