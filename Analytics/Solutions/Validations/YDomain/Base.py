# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''
from abc import ABC

from Analytics.Solutions.ISolution import ISolution
from Utilities.DataEntry import Options
from numpy import arange
import sys
'''
Problem being solved is: [0,1]U[1,2]U[1,3] X [0,1]
    This is an example used by Jemmy in a Y Domain.
    Although it does not look like it, all the 
    segments have the same length.    
    BC:
    du/dx(0) = du/dx(3) = du/dx(2) = 0
    du/dx(1) - du/dx(1) - du/dx(1) = 0 - derivative continuity
    u(1) = u(1) = u(1) - variable continuity

    Initial Conditions:
    u(0,x) = cos(pi*x)

'''


class YDomain(ISolution, ABC):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(name="Y Domain Base Solution",
                                  numSegments=None,
                                  bifurcationPoints=None,sElementsE=None,sElementsLw=None,sElementsUp=None,
                                  domainDef=["domainE","domainLw","domainUp"],
                                  sElementDef=["sElementsE","sElementsLw","sElementsUp"],
                                  description="This is a base solution for the Y Domain Problem)")

        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions

        super(YDomain, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ########################################

    def __defineSpatialElements(self,attributeName,value):

        if (attributeName in self.domainDef or attributeName == "steps") and value is not None:
            try:
                getattr(self, attributeName)
                getattr(self, "steps")

                for domain in self.domainDef:
                    self.__dict__["sElements"+domain[6:]] = arange(self.__dict__[domain].space[0], self.__dict__[domain].space[-1] +
                                                                   self.steps.space, self.steps.space)

            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)

    def __setattr__(self, attributeName, value):

        super(YDomain, self).__setattr__(attributeName, value)
        # print("Attribute:",attributeName)
        # print("Values:",value)
        if self.domainDef is not None and self.steps is not None:
            self.__defineSpatialElements(attributeName,value)