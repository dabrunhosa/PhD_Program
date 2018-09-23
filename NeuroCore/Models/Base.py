# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

import sys
from abc import abstractmethod

from Conventions.Classes import Names
from Conventions.NeuroCore.Models.Base import BaseParameters as constants
from Utilities.BaseOption import ISolvable
from Utilities.DataEntry import Options


class IModel(ISolvable):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().IModel,
                                     constants().Domain: None,
                                     constants().Steps: None,
                                     constants().CurrentTime: None,
                                     constants().InitialCondition: None,
                                     constants().Results: [],
                                     constants().Coeffs: None,
                                     constants().Font: None,
                                     constants().BCs: None,
                                     constants().IApproximation: None,
                                     constants().TimeApproximation: None,
                                     constants().Equation: {}})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        # print("IModel Kw Options:",kw)
        # print("\nIModel Whole Options:",whole_options.__dict__)

        super(IModel, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __setattr__(self, attributeName, value):
        super(IModel, self).__setattr__(attributeName, value)

        if attributeName == constants().CurrentTime and value is not None:
            self.iApproximation.currentTime = self.currentTime
        elif attributeName == constants().CoeffT and value is not None:
            try:
                self.checkExistance(constants().TimeApproximation)
                self.timeApproximation.coeffT = value
                setattr(self, constants().CurrentTime, 0)
            except AttributeError:
                error_message = "You have to set the time approximation" \
                                " for the software to use the coeff_t."
                raise AttributeError(error_message)

        elif attributeName == constants().InitialCondition and value is not None:
            self.iApproximation.results.append(self.initialCondition)
            self.results.append(self.initialCondition)
            # self.iApproximation.timeModifiers = self.timeApproximation.

        elif attributeName == constants().BCs and value is not None:
            self.iApproximation.BCs = self.BCs

        elif (attributeName in [constants().Coeffs,constants().Domain,constants().Steps]) and value is not None:

            try:
                if self.checkExistance([constants().Domain,constants().Coeffs,
                                        constants().Steps,constants().Font,constants().Coeffs]):

                    self.iApproximation.domain = getattr(self,constants().Domain)
                    self.iApproximation.font = getattr(self,constants().Font)
                    self.iApproximation.coeffs = getattr(self,constants().Coeffs)

                    if not self.checkDefaultValues(constants().Steps):
                        self.iApproximation.steps = self.steps

                        if not self.checkDefaultValues(constants().TimeApproximation):
                            self.timeApproximation.step = self.steps.time

                        self.createEquations()
                        self.iApproximation.equation = self.equation

            except:
                e = sys.exc_info()
                print(e)
                raise Exception(e)

    ######################################## 
    ###       Public Functions           ###
    ######################################## 

    def solve(self, **arguments):

        if constants().CurrentTime in arguments.keys():
            self.currentTime = arguments[constants().CurrentTime]

        return self.iApproximation.solve(**arguments)

    ########################################
    ###       Abstract Functions         ###
    ######################################## 

    @abstractmethod
    def createEquations(self):
        raise NotImplementedError("Must override in Model Class")

#    @abstractmethod
#    def createFont(self):
#        raise NotImplementedError("Must override in Model Class")
#        
#    @abstractmethod
#    def createInitialConditions(self):
#        raise NotImplementedError("Must override in Model Class")
#        
#    @abstractmethod
#    def createBCs(self):
#        raise NotImplementedError("Must override in Model Class")
