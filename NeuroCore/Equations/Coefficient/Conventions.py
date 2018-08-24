# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:25:14 2017

@author: Daniel Abrunhosa
"""


class CoeffId(object):
    @property
    def Constant():
        return "Constant"
    @property
    def Stationary():
        return "Stationary"
    @property
    def Transient():
        return "Transient"
    @property
    def NonLinear():
        return "NonLinear"


