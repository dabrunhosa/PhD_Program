 # -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''

from Analytics.Solutions.ISolution import ISolution
from Utilities.DataEntry import Options
from cmath import exp,sin,pi
from numpy import arange

'''
Problem being solved is: [0,1]X[0,T]
    1/k*du/dt - d2u/dx2 + u = f
    f = 4*pi2*(e^(-kt))*sin(2*pi*x)
    
    BC:
        u(0,t) = u(1,t) = 0
        
    Initial Conditions:
        u(x,0) = sin(2*pi*x)
'''
class CableModel(ISolution):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name = "Cable Model With Font",
                                  kValue = 1,
                                  description = "This is the solution for the \
                                                  following problem:\
                                                  Problem being solved is: [0,X]X[0,T]\
                                                  1/k*du/dt - d2u/dx2 + u = f \
                                                  f = 4*pi2*(e^(-kt))*sin(2*pi*x)\
                                                  BC: u(0,t) = u(1,t) = 0 \
                                                  Initial Conditions:\
                                                  u(x,0) = sin(2*pi*x)\
                                                  Solution: u = (e^(-kt))*sin(2*pi*x)")
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(ValidationWithF,self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Public Functions           ###
    ######################################## 
    
    def createFont(self):
        
        timeK = self.kValue
        
        def fontFunction(x,t):
            return 4*pow(pi,2)*exp(-timeK*t)*sin(2*pi*x)
            
        return fontFunction
    
    def createInitialCondition(self):
        
        def initialFunction(x):
            return sin(2*pi*x)
            
        return initialFunction
    
    def solve(self,**arguments):
        
        '''Calculating all the points for the exact solution. 
        Obs: That would be a way without the loop if the 
        functions sinh and cosh accepted the vector form as well.'''
        
        timeElements = arange(0 , self.domain.time[-1] + self.steps.time, self.steps.time) 

        def u(x,t):
            return exp(-self.kValue*t)*sin(2*pi*x)

        for t in timeElements:

            currentTime = []

            for x in self.sElements:
                currentTime.append(u(x,t))

            self.solution.append(currentTime)
            
        return self.solution