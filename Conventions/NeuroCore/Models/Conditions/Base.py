# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:50:32 2017

@author: Daniel Abrunhosa
"""

from Conventions.Parameters import Parameters


class BaseParameters(Parameters):

    @property
    def Dirichlet(self):
        return "Dirichlet"

    @property
    def Neumann(self):
        return "Neumann"

    @property
    def BcValue(self):
        return "bcValue"

    @property
    def BcType(self):
        return "bcType"
