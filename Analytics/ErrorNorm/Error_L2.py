# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:24:59 2017

@author: daniel
"""

from Analytics.ErrorNorm.Base import IErrorNorm

class Error_L2(IErrorNorm):
    
    ########################################
    ###       Public Functions           ###
    ######################################## 
    
    def calculate(self):
        raise NotImplementedError
        
    def write(self,outFile):
        raise NotImplementedError