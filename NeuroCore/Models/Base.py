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

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().IModel,
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
        whole_options = default_options << options

        # print("IModel Kw Options:",kw)
        # print("\nIModel Whole Options:",whole_options.__dict__)

        super(IModel, self).__init__(whole_options, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __setattr__(self, attributeName, value):
        super(IModel, self).__setattr__(attributeName, value)

        if attributeName == constants().CurrentTime and value is not None:
            self.iApproximation.currentTime = self.currentTime

        if attributeName == constants().CoeffT and value is not None:
            try:
                self.checkExistance(constants().TimeApproximation)
                self.timeApproximation.coeffT = value
                setattr(self, constants().CurrentTime, 0)
            except AttributeError:
                error_message = "You have to set the time approximation" \
                                " for the software to use the coeff_t."
                raise AttributeError(error_message)

        if attributeName == constants().InitialCondition and value is not None:
            self.iApproximation.results.append(self.initialCondition)
            self.results.append(self.initialCondition)
            # self.iApproximation.timeModifiers = self.timeApproximation.

        if attributeName == constants().BCs and value is not None:
            self.iApproximation.BCs = self.BCs

        if (attributeName == constants().Coeffs or attributeName == constants().Domain or
            attributeName == constants().Steps) and value is not None:

            try:

                if self.checkExistance(constants().Domain) and self.domain is not None \
                        and self.checkExistance(constants().Coeffs) and self.coeffs is not None \
                        and self.checkExistance(constants().Steps) and self.steps is not None:

                    if self.timeApproximation is not None:
                        self.timeApproximation.step = self.steps.time

                    self.iApproximation.domain = self.domain
                    self.iApproximation.steps = self.steps
                    self.iApproximation.font = self.font
                    self.iApproximation.coeffs = self.coeffs
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
