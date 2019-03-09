# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:08:35 2017

@author: Daniel Abrunhosa
"""

from Utilities.DataEntry import Options
from Utilities.BaseOption import IHaveOption
from Conventions.Utilities.UtilitiesParameters import UtilitiesParameters
from Conventions.Classes import Names
import inspect


# noinspection PyDeprecation,PyDeprecation
class Function(IHaveOption):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, userFunction, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{UtilitiesParameters().Name: Names().Function,
                                   UtilitiesParameters().InFunction: self.__fixFunction(userFunction),
                                   UtilitiesParameters().InConstant: 1.0})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(Function, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __fixFunction(self, userFunction):

        if not callable(userFunction):
            value = userFunction

            def function(qsi):
                return value

            userFunction = function

        return userFunction

    def __call__(self, x):
        return self.inConstant * self.inFunction(x)

    ########################################
    ###       Public Functions           ###
    ########################################

    def requiredArguments(self):
        args, varargs, varkw, defaults = inspect.getargspec(self.inFunction)
        if defaults:
            args = args[:-len(defaults)]

        return args

    def isMissingArguments(self, argdict):
        return set(self.__requiredArguments()).difference(argdict)

    def isValidArguments(self, argdict):
        args, varargs, varkw, defaults = inspect.getargspec(self.inFunction)

        if varkw:
            return set()  # All accepted

        return set(argdict) - set(args)

    def isCallableArguments(self, argdict):
        return not self.__isMissingArguments(argdict) and not self.__isValidArguments(argdict)
