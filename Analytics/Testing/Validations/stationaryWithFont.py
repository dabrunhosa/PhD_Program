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

import time

import numpy

from Analytics.Solutions.Validations.Stationary import ValidationWithF
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Neumanns import SealedEnd
from NeuroCore.Models.Conventions import Domains, Steps
from NeuroCore.Models.GeneralModel import GeneralModel
from NeuroCore.Neuron.Segment.Base import ISegment
from Plotting.IDataPlot import IDataPlot
from Plotting.IDataPlots import IDataPlots
from Plotting.Simulation import Simulation

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(space=[0, 12])
simSteps = Steps(space=0.01)

diffusionValue = 100
reactionValue = 10

boundaryConditions = BoundaryConditions(SealedEnd(), SealedEnd())

sElements = numpy.arange(0, simDomain.space[-1] + simSteps.space, \
                         simSteps.space)

########################################
###      Setting the Simulation      ###
######################################## 

analytical = ValidationWithF(domain=simDomain, steps=simSteps, \
                             BCs=boundaryConditions, \
                             diffusionValue=diffusionValue, \
                             reactionValue=reactionValue)

font = analytical.createFont()

# import inspect
# print(inspect.getsource(font))

# font = f

simModel = GeneralModel(iApproximation=GalerkinApproximation(), \
                        BCs=boundaryConditions,
                        font=font, coeff_dx2=-diffusionValue, \
                        coeff_v=reactionValue)

segment0 = ISegment('Axon0', boundaryConditions, simDomain, simSteps, simModel)

########################################
###      Running the Simulation      ###
######################################## 

analyticalResult = analytical.solve()

t_start = time.clock()
result = segment0.solve()

approxPlot = IDataPlot(name=simModel.name, domain=simDomain, steps=simSteps, results=result, color="b")
analyPlot = IDataPlot(name=analytical.name, domain=simDomain, steps=simSteps, results=analyticalResult, color="k")

plots = IDataPlots(listPlots=[analyPlot, approxPlot])

plotting = Simulation(plots=plots)
plotting.save("stationaryWithFont.png")
