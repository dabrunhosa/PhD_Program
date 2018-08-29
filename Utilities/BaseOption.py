# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 05:34:15 2017

@author: daniel
"""

from abc import ABCMeta, abstractmethod

from Utilities.DataEntry import Options, Options_User
from Conventions.Variables import Variables
from Conventions.Parameters import Parameters
from Conventions.Classes import Names
import sys


class IHaveOption(object):
    ########################################
    ###       Private Variables          ###
    ######################################## 

    # Setting this class as an abstract class
    __metaclass__ = ABCMeta

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), **kw):

        # Class to threat the Option Class 
        class_option = Options_User()

        self.__dict__[Variables().Class_Attributes] = []

        # Define the default options
        default_options = Options(**{Parameters().Name: Names().Default})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        # All the attributes allowed to be access.
        self.__dict__[Variables().Class_Attributes] = whole_options.names

        # print("\n\nBase Option Kw Options:", kw)
        # print("Base Option Whole Options:", self.__dict__)

        # Initialize the options and the extra arguments
        class_option.init_options(self, whole_options, kw)

    ########################################
    ###       Class Functions            ###
    ######################################## 

    @classmethod
    def version(self):
        return "1.0"

    ########################################
    ###       Private Functions          ###
    ########################################

    def checkExistance(self, attributeName):

        for attribute in attributeName:
            return attributeName in self.__dict__[Variables().Class_Attributes]

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

        if attributeName in self.__dict__[Variables().Class_Attributes]:
            value = None
            try:
                value = self.__dict__[attributeName]
            except KeyError:
                e = sys.exc_info()
                print(self,self.__dict__,attributeName)
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
