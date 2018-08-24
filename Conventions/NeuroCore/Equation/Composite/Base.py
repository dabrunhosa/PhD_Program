# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:25:14 2018

@author: Daniel Abrunhosa
"""
from Conventions.NeuroCore.Equation.IEquation import IEquationParameters


class BaseParameters(IEquationParameters):
    @property
    def Equation(self):
        return "equation"
