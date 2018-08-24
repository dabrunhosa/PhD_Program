# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:08:35 2017

@author: Daniel Abrunhosa
"""
from abc import ABC

from Utilities.DataEntry import Options
from NeuroCore.Equations.IEquation import IEquation
from NeuroCore.Equations.Coefficient.Conventions import CoeffId
import inspect


# noinspection PyDeprecation
class ICoefficient(IEquation, ABC):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, userCoeff, options=Options(), **kw):

        # Define the default options
        default_options = Options(name="Coefficient",
                                  customFunctions={},
                                  coeffType=self.__identifyType(userCoeff),
                                  value=userCoeff)

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(ICoefficient, self).__init__(whole_options, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __identifyType(self, userCoeff):

        coeffType = CoeffId().Constant
        if callable(userCoeff):
            args, varargs, varkw, defaults = inspect.getargspec(userCoeff)
            if defaults:
                args = args[:-len(defaults)]

            if len(args) == 1 and 'x' in args:
                coeffType = CoeffId().Stationary
            elif len(args) == 2 and 'x' in args and 't' in args:
                coeffType = CoeffId().Transient
            elif len(args) == 3 and 'x' in args and 't' in args and 'V' in args:
                coeffType = CoeffId().NonLinear
            else:
                raise NotImplementedError("The Coefficient passed is not supported yet.")

        return coeffType

    def __call__(self, **arguments):
        return self.userCoeff(**arguments)
