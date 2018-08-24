# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:25:14 2017

@author: Daniel Abrunhosa
"""


'''
This function is a good idea but it should be in the Composite Equation or the 
higher level possible, and then a flag is passed to all the Components, weight functions
and integration rules that the calculation is going to be made in a reference element
'''


def femTransformation(function, domain):
    wrapFunction = function

    def paramFunction(qsi):
        return wrapFunction((((domain[-1] - domain[0]) / 2) * qsi) + (1 / 2) * (domain[0] + domain[-1]))

    return paramFunction
