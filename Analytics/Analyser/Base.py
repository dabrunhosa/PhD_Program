# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:32:21 2017

@author: daniel
"""

from Utilities.BaseOption import ISolvable
from Utilities.DataEntry import Options
import sys

class AnalyserError(AttributeError): 
    pass

class IAnalyser(ISolvable):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
         # Define the default options
        inDefaultOptions =Options(name = "IAnalyser",
                                       testProtocols = None,
                                       analyticalSolution = None,
                                       approxSolution = None,
                                       domain = None)
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(IAnalyser,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
        
    ########################################
    ###       Private Functions          ###
    ######################################## 
    
    def __verifySolutions(self):
        
        analytical = self.analyticalSolution.solve()
        approx = self.approxSolution.solve()
        
        if len(analytical) != len(approx):
            error_message = "The solutions have be the same size"
            raise AnalyserError(error_message)
            
    def __setattr__(self,attributeName,value):
        
        if (attributeName == "analyticalSolution" or\
            attributeName == "approxSolution") and value is not None:
            
            try:
                getattr(self,"analyticalSolution")
                getattr(self,"approxSolution")
                
                if self.analyticalSolution is not None and self.approxSolution is not None:
                    self.__verifySolutions()
                            
            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)
            
        super(IAnalyser,self).__setattr__(attributeName,value)
        
    ########################################
    ###       Public Functions           ###
    ######################################## 

    ''' 
    This routine will execute the tests for each approximation against the analytical
    solution and create a file containing the results.
    '''
    def solve(self,**arguments):
        
        for test in self.testProtocols:

            solution_log = self.analyticalSolution.solve()   
            [approximation_log,approximation_time] = self.approxSolution.solve()
             
            outfile = open("Test_Results/"+ self.approxSolution.name +\
                           "/coeff_dx2_" + str(coeffs['coeff_dx_2']) +\
                           "_Delta_X_" + str(steps['delta_x']) + '.txt', 'w')

            
            outfile.write('\nDelta_X - '+str(steps['delta_x']))
            outfile.write('\ncoeff_dx2 - '+str(coeffs['coeff_dx_2']))
            outfile.write('\n\nSimulation Time (in seconds) - '+str(approximation_time))
            outfile.write('\n')
            
            arguments["errorNorm"].u = solution_log
            arguments["errorNorm"].uh = approximation_log
            
            self.errorNorm.write(outfile,writePosition=True,\
                            positionCorrector=steps['delta_x'])

            outfile.close()
    
