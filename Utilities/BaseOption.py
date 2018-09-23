# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 05:34:15 2017

@author: daniel
"""

import sys
from abc import ABCMeta, abstractmethod
from Conventions.Variables import Variables
from Utilities.DataEntry import Options, Options_User


class IHaveOption(object):
    ########################################
    ###       Private Variables          ###
    ######################################## 

    # Setting this class as an abstract class
    __metaclass__ = ABCMeta

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions=Options(), **kw):

        # Class to threat the Option Class 
        class_option = Options_User()

        self.__dict__[Variables().Class_Attributes] = []

        # All the attributes allowed to be access.
        self.__dict__[Variables().Class_Attributes] = defaultOptions.names

        # All the attributes and expected types
        self.__dict__[Variables().ExpectedTypes] = self.__createExpectedTypes(defaultOptions)

        # All the attributes and default values
        self.__dict__[Variables().DefaultValues] = self.__createDefaultValues(defaultOptions)

        # print("\n\nBase Option Kw Options:", kw)
        # print("Base Option Whole Options:", self.__dict__)

        # Initialize the options and the extra arguments
        class_option.init_options(self, options, kw)

    ########################################
    ###       Class Functions            ###
    ######################################## 

    @classmethod
    def version(self):
        return "1.0"

    ########################################
    ###       Public Functions           ###
    ########################################

    def checkExistance(self, attributeNames):

        if isinstance(attributeNames, list):
            for attribute in attributeNames:
                if attribute not in self.__dict__:
                    return False
        else:
            if attributeNames not in self.__dict__:
                return False

        return True

    def RaiseOnUnexpectedType(self):
        for attribute in self.__dict__[Variables().Class_Attributes]:
            if not isinstance(self.__dict__[attribute], self.__dict__[Variables().ExpectedTypes][attribute]):
                error_message = "The attribute:", attribute, " from the class:", self.name, \
                                " is not of the correct type. The type should be:", \
                                self.__dict__[Variables().ExpectedTypes][attribute]

                raise AttributeError(error_message)

    def checkDefaultValues(self, nameVariablesToCheck):

        if isinstance(nameVariablesToCheck, list):
            for variableName in nameVariablesToCheck:
                if self.__dict__[variableName] ==  self.__dict__[Variables().DefaultValues][variableName]:
                    return True
                    pass

        else:
            if self.__dict__[nameVariablesToCheck] is self.__dict__[Variables().DefaultValues][nameVariablesToCheck]:
                return True

        return False

    ########################################
    ###       Private Functions          ###
    ########################################

    def __createDefaultValues(self, wholeOptions):
        defaultValues = {}

        for attribute, value in wholeOptions:
            defaultValues[attribute] = value

        return defaultValues

    def __createExpectedTypes(self, wholeOptions):
        expectTypeDict = {}

        for attribute, value in wholeOptions:
            expectTypeDict[attribute] = type(value)

        return expectTypeDict

    def __setattr__(self, attributeName, value):

        # Check if the given attribute is 
        # an allowed one.
        if attributeName in self.__dict__[Variables().Class_Attributes]:
            # If it's add it to the internal
            # dictionary
            self.__dict__[attributeName] = value
        else:
            error_message = "The attribute: '" + attributeName + \
                            "' is not an allowed attribute to set."

            raise AttributeError(error_message)

    def __getattr__(self, attributeName):

        if attributeName is Variables().ExpectedTypes or attributeName in self.__dict__[Variables().Class_Attributes]:
            value = None
            try:
                value = self.__dict__[attributeName]
            except KeyError:
                e = sys.exc_info()
                print(self, self.__dict__, attributeName)
                raise Exception(e)
            except Exception as e:
                print(e)
                raise Exception(e)

            return value
        else:
            error_message = "The attribute name: " + attributeName + \
                            " is not an allowed attribute to get."
            raise AttributeError(error_message)


class ISolvable(IHaveOption):

    ########################################
    ###       Abstract Functions         ###
    ######################################## 

    @abstractmethod
    def solve(self, **arguments):
        raise NotImplementedError
