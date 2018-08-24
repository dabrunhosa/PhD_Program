# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:25:14 2018

@author: Daniel Abrunhosa
"""
from Conventions.NeuroCore.Equation.Composite.Base import BaseParameters


class FEMParameters(BaseParameters):
    @property
    def Line(self):
        return "line"

    @property
    def Column(self):
        return "column"

    @property
    def Previous(self):
        return "previous"
