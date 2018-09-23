 # -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''

'''
 Created on August 24, 2017
 
 @author: dabrunhosa
 '''

from Analytics.Solutions.ISolution import ISolution
from Utilities.DataEntry import Options
from cmath import exp,sin,pi,sqrt
from numpy import arange

'''
Problem being solved is: [0,1]X[0,T]

    
    BC:

        
    Initial Conditions:

'''


 # noinspection PyArgumentList
 class CableModelTwoBranches(ISolution):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name = "Passive Cable Model Example for 2 Branches",
                                  kValue = 1,
                                  description = "This is the solution for the \
                                                  following problem:\
                                                  Problem being solved is: [0,X]X[0,T]\
                                                  du/dt - D*d2u/dx2 + 1/tau*u = 0 \
                                                  BC: u(0,t) = u(1,t) = 0 \
                                                  Initial Conditions:\
                                                  u(x,0) = sin(2*pi*x)\
                                                  Solution: u = (e^(-kt))*sin(2*pi*x)",
                                  rm=None,
                                  cm=None,
                                  rc=None,
                                  tau=None,
                                  D=None)
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(CableModelTwoBranches,self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Public Functions           ###
    ######################################## 
    
    def createFont(self):
        
        def fontFunction(x,t):
            return 0
            
        return fontFunction
    
    def createInitialCondition(self):
        
        def initialFunction(x):

            if (x == 0):
                return alpha*delta(x_a + a)

            if (x == 1):
                return -beta*delta(x_b + b)
            
        return initialFunction
    
    def solve(self,**arguments):
        
        '''Calculating all the points for the exact solution. 
        Obs: That would be a way without the loop if the 
        functions sinh and cosh accepted the vector form as well.'''
        
        timeElements = arange(0 , self.domain.time[-1] + self.steps.time, self.steps.time)

        D = 1/(arguments['rc'] * arguments['cm'])
        tau = arguments['rm'] * arguments['cm']

        # noinspection PyArgumentList
        def u(x,t):
            # noinspection PyArgumentList
            return (1/ (sqrt(4*pi*D*(t-self.domain.time[-1]))) ) \
                   * exp((x-pow(x-self.domain.space[-1]))/
                         (4*D*(t-self.domain.time[-1])) -
                         ((t-self.domain.time[-1]))/(tau))

        for t in timeElements:

            currentTime = []

            for x in self.sElements:
                currentTime.append(u(x,t))

            self.solution.append(currentTime)
            
        return self.solution


class CableModelWithSoma(ISolution):

     ########################################
     ###       Constructor                ###
     ########################################

     def __init__(self, options=Options(), defaultOptions = Options(), **kw):

         # Define the default options
         inDefaultOptions =Options(name="Passive Cable Model",
                                   kValue=1,
                                   description="This is the solution for the \
                                                  following problem:\
                                                  Problem being solved is: [0,X]X[0,T]\
                                                  1/k*du/dt - d2u/dx2 + u = f \
                                                  f = 4*pi2*(e^(-kt))*sin(2*pi*x)\
                                                  BC: u(0,t) = u(1,t) = 0 \
                                                  Initial Conditions:\
                                                  u(x,0) = sin(2*pi*x)\
                                                  Solution: u = (e^(-kt))*sin(2*pi*x)",
                                   rm=None,
                                   cm=None,
                                   rc=None,
                                   tau=None,
                                   D=None)

         # Merge the default options and the user generated options
         .
				 defaultOptions = inDefaultOptions << defaultOptions

         super(CableModelWithSoma, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

     ########################################
     ###       Public Functions           ###
     ########################################

     def createFont(self):

         def fontFunction(x, t):
             return 0

         return fontFunction

     def createInitialCondition(self):

         def initialFunction(x):

             if (x == 0):
                 return alpha * delta(x_a + a)

             if (x == 1):
                 return -beta * delta(x_b + b)

         return initialFunction

     def solve(self, **arguments):

         '''Calculating all the points for the exact solution.
         Obs: That would be a way without the loop if the
         functions sinh and cosh accepted the vector form as well.'''

         timeElements = arange(0, self.domain.time[-1] + self.steps.time, self.steps.time)

         D = 1 / (arguments['rc'] * arguments['cm'])
         tau = arguments['rm'] * arguments['cm']

         def u(x, t):
             return (-70 / (sqrt(4 * pi * D * t))) \
                    * exp( (pow(x,2) / (4 * D * t)) - (t / (tau)))

         for t in timeElements:

             currentTime = []

             for x in self.sElements:
                 currentTime.append(u(x, t))

             self.solution.append(currentTime)

         return self.solution