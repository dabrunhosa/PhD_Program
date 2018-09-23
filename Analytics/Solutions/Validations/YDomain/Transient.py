 # -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''


from Analytics.Solutions.Validations.YDomain.TransientBase import YDomainTransientBase
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Neumanns import SealedEnd
from NeuroCore.Models.Conventions import Domains
from Utilities.DataEntry import Options
from cmath import cos,pi,exp,sin
from numpy import arange

'''
Problem being solved is: [0,1]U[1,2]U[1,3] X [0,1]
    This is an example used by Jemmy in a Y Domain.
    Although it does not look like it, all the 
    segments have the same length.    
    BC:
    du/dx(0) = du/dx(3) = du/dx(2) = 0
    du/dx(1) - du/dx(1) - du/dx(1) = 0 - derivative continuity
    u(1) = u(1) = u(1) - variable continuity
        
    Initial Conditions:
    u(0,x) = cos(pi*x)

'''
class JemmyEx1(YDomainTransientBase):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name="Jemmy's Example 1",
                                  numSegments=3,
                                  bifurcationPoints=1,
                                  domainE=Domains(space=[0, 1],time=[0,1]),
                                  domainLw=Domains(space=[1, 2],time=[0,1]),
                                  domainUp=Domains(space=[1, 3],time=[0,1]),
                                  bcDomainE=BoundaryConditions(SealedEnd(), SealedEnd()),
                                  bcDomainLw=BoundaryConditions(SealedEnd(), SealedEnd()),
                                  bcDomainUp=BoundaryConditions(SealedEnd(), SealedEnd()),
                                  solutionE=[],
                                  solutionLw=[],
                                  solutionUp=[],
                                  description="This is the solution for the \
                                                  following problem:\
                                                  Problem being solved is: [0,3]X[0,1]\
                                                  d2u/dx2 = du\dt + u \
                                                  BC:  du/dx(0,t) = du/dx(2,t) = du/dx(3,t) = 0 \
                                                  Initial Conditions:\
                                                  u(x,0) = cos(pi*x)\
                                                  Solution: u = (e^(-(1 + pi^2)*t)*cos(pi*x)")
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(JemmyEx1,self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Public Functions           ###
    ########################################

    def createInitialCondition(self):
        
        def initialFunction(x):
            return cos(pi*x)
            
        return initialFunction
    
    def solve(self,**arguments):
        
        '''Calculating all the points for the exact solution. 
        Obs: That would be a way without the loop if the 
        functions sinh and cosh accepted the vector form as well.'''
        
        timeElements = arange(0 , self.domainE.time[-1] + self.steps.time, self.steps.time)

        def u(x,t):
            return exp(-(1 + pow(pi,2))*t)*cos(pi*x)

        for t in timeElements:
            self.solutionE.append([u(x,t) for x in self.sElementsE])
            self.solutionLw.append([u(x, t) for x in self.sElementsLw])
            self.solutionUp.append([u(x, t) for x in self.sElementsUp])
            
        return [self.solutionE,self.solutionLw,self.solutionUp]


class JemmyEx2(YDomainTransientBase):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(name="Jemmy's Example 2",
                                  numSegments=3,
                                  bifurcationPoints=1,
                                  segmentsDomain=[Domains(space=[0, pi/2],time=[0,1]), Domains(space=[pi/2, pi],time=[0,1]),
                                                  Domains(space=[pi/2, 3*(pi/2)],time=[0,1])],
                                  boundaryConditions=[BoundaryConditions(SealedEnd(), SealedEnd()),
                                                      BoundaryConditions(SealedEnd(), SealedEnd()),
                                                      BoundaryConditions(SealedEnd(), SealedEnd())],
                                  description="This is the solution for the \
                                                  following problem:\
                                                  Problem being solved is: [0,3*pi/2]X[0,1]\
                                                  d2u/dx2 = du\dt - 2*u \
                                                  BC:  du/dx(0,t) = -e^t, du/dx(pi,t) = e^t , du/dx(3*pi/2,t) = 0 \
                                                  Initial Conditions:\
                                                  u(x,0) = -sin(x)\
                                                  Solution: u = (e^-t)*sin(x)")

        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions

        super(JemmyEx2, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Public Functions           ###
    ########################################

    def createInitialCondition(self):

        def initialFunction(x):
            return -sin(x)

        return initialFunction

    def solve(self, **arguments):

        '''Calculating all the points for the exact solution.
        Obs: That would be a way without the loop if the
        functions sinh and cosh accepted the vector form as well.'''

        timeElements = arange(0, self.domain.time[-1] + self.steps.time, self.steps.time)

        def u(x, t):
            return -exp(t) * sin(x)

        for t in timeElements:

            currentTime = []

            for x in self.sElements:
                currentTime.append(u(x, t))

            self.solution.append(currentTime)

        return self.solution