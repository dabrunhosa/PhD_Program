# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:38:34 2017

@author: Daniel Abrunhosa
"""


'''
This is the solution for the following problem:
    Problem being solved is: [0,X]
    - epsilon*d2u/dx2 + theta*u = f
    f =  (theta + epsilon*4*(pi^2))*cos(2*pi*x)
    
    BC:
        du/dx(0) = du/dx(1) = 0
        
    Solution:
        u = cos(2*pi*x)
'''

########################################
###           Packages               ###
######################################## 

from Neuron.Segment.Base import ISegment
from Models.CableModel import CableModel
from Models.Conventions import Domains,Steps
from Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from Models.Conditions.BCs import BoundaryConditions
from Models.Conditions.Neumanns import Neumann
from Analytics.Solutions.Validations.Stationary import CableModelWithF
from Approximations.Space.FEM.Integration.Trapezoidal import Trapezoidal
from Plotting.Simulation import Simulation
from Plotting.IDataPlot import IDataPlot

#from cmath import pi,cos
#from math import pow

import numpy
import time

#import inspect

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(space=[0,1])
simSteps = Steps(space=0.01)

diffusionValue = 0.1
reactionValue = 1

boundaryConditions = BoundaryConditions(Neumann(bcValue=0),Neumann(bcValue=0))

sElements = numpy.arange(0, simDomain.space[-1] + simSteps.space,\
                                simSteps.space)

#def f(x):
#    return (reactionValue + diffusionValue*4*pow(pi,2))*cos(2*pi*x)

########################################
###      Setting the Simulation      ###
######################################## 

analytical = CableModelWithF(domain=simDomain,steps=simSteps,\
                             BCs=boundaryConditions,\
                             diffusionValue = diffusionValue,\
                             reactionValue = reactionValue)

font = analytical.createFont()
#font = f

simModel = CableModel(iApproximation=GalerkinApproximation(numIntegration=Trapezoidal()),\
                      font=font,coeff_dx2 = -diffusionValue,\
                      coeff_v = reactionValue)

segment0 = ISegment('Axon0',boundaryConditions,simDomain,simSteps,simModel)

########################################
###      Running the Simulation      ###
######################################## 

analyticalResult = analytical.solve()

t_start = time.clock()
result = segment0.solve()

approxPlot = IDataPlot(name=simModel.name,domain=simDomain,steps=simSteps,results=result,color="red")
analyPlot = IDataPlot(name=analytical.name,domain=simDomain,steps=simSteps,results=analyticalResult,color="blue")

plotting = Simulation(iDataPlots=[analyPlot,approxPlot])
plotting.save("StationaryWithFont.jpg")

#print("Result:",result)
#print("Elapsed Time:",time.clock()-t_start)
    
