# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:27:55 2017

@author: daniel
"""
from Analytics.ErrorNorm.Base import IErrorNorm
import numpy as np

class Error_Lifty(IErrorNorm):
    
    ########################################
    ###       Public Functions           ###
    ######################################## 
    
    def calculate(self,calcPosition=False):
        error_vector = self.u - self.uh
        error_vector = list(error_vector)
         
        max_error = np.linalg.norm(error_vector, np.Inf)
        
        if(calcPosition):
            error_position = error_vector.index(max_error)    
            return [max_error,error_position]
        else:
            return max_error
        
    def write(self,outFile,writePosition=False,positionCorrector=None):
        [max_error,error_position] = self.calculate(writePosition)
        
        outFile.write('\nError in L_ifty - '+str(max_error))
        if(writePosition):
            outFile.write('\nSpatial Position - ' +\
                          str(error_position*positionCorrector))
