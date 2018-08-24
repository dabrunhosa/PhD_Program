# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:12:36 2017

@author: Daniel Abrunhosa
"""


class DataAnalysed(object):
    @property
    def Diffusion():
        return "diffusion"
    
    @property
    def Reaction():
        return "reaction"
    
    @property
    def Time():
        return "time"
    
    @property
    def timeDomain():
        return "timeDomain"
    
    @property
    def spaceDomain():
        return "spaceDomain"
    
    @property
    def timeSteps():
        return "timeSteps"
    
    @property
    def spaceSteps():
        return "spaceSteps"