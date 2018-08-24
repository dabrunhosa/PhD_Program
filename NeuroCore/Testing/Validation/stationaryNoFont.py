# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:04:01 2017

@author: Daniel Abrunhosa
"""


'''
This is the solution for the following problem:
    Problem being solved is: [0,1]
    -epsilon*d2u/dx2 + u = 0
    
    BC:
        du/dx(0) = u0
        du/dx(1) = u1
        
    Solution:
        u = alpha*sinh(lambda*x) + beta*cosh(lambda*x)
        alpha = u0/lambda
        beta = u1 - u0*cosh(lambda)/lambda*sinh(lambda)
        lambda = 1/sqrt(epsilon)

'''

########################################
###           Packages               ###
######################################## 

from NeuroCore.Neuron.Segment.Base import ISegment
from NeuroCore.Models.Base import GeneralModel
from NeuroCore.Models.Conventions import Domains,Steps
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Neumanns import Neumann
from Analytics.Solutions.Validations.Stationary import ValidationZeroF as analyCableModel
from NeuroCore.Approximations.Space.FEM.Integration.Trapezoidal import Trapezoidal
from Plotting.Simulation import Simulation
from Plotting.IDataPlot import IDataPlot
 
import numpy
import time

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(space=[0,1])
simSteps = Steps(space=0.1)

########################################
###      Setting the Simulation      ###
######################################## 

def f(x):
    return 0

diffusionValue = -0.01
reactionValue = 1

boundaryConditions = BoundaryConditions(Neumann(bcValue=1),Neumann(bcValue=1))

simModel = GeneralModel(iApproximation=GalerkinApproximation(numIntegration=Trapezoidal()),\
                      font=f,coeff_dx2 = diffusionValue,coeff_v = reactionValue)

segment0 = ISegment('Axon0',boundaryConditions,simDomain,simSteps,simModel)

########################################
###      Running the Simulation      ###
######################################## 

sElements = numpy.arange(0, simDomain.space[-1] + simSteps.space,\
                                simSteps.space)

analytical = analyCableModel(domain=simDomain,steps=simSteps,\
                             BCs=boundaryConditions,\
                             diffusionValue = -diffusionValue,\
                             reactionValue = reactionValue)
analyticalResult = analytical.solve()

t_start = time.clock()
result = segment0.solve()

approxPlot = IDataPlot(name=simModel.name,domain=simDomain,steps=simSteps,results=result,color="red")
analyPlot = IDataPlot(name=analytical.name,domain=simDomain,steps=simSteps,results=analyticalResult,color="blue")

plotting = Simulation(iDataPlots=[analyPlot,approxPlot])
plotting.save("StationaryNoFont.jpg")
