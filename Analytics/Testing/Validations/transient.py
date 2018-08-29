# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:50:02 2017

@author: Daniel Abrunhosa
"""

'''
Problem being solved is: [0,1]X[0,T]
    1/k*du/dt - d2u/dx2 + u = f
    f = 4*pi2*(e^(-kt))*sin(2*pi*x)
    
    BC:
        u(0,t) = u(1,t) = 0
        
    Initial Conditions:
        u(x,0) = sin(2*pi*x)
'''

from numpy import arange

from Analytics.Solutions.Validations.Transient import ValidationWithF
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from NeuroCore.Approximations.Time.BackwardEuler import BackwardEuler
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Dirichlets import KilledEnd
from NeuroCore.Models.Conventions import Domains, Steps
from NeuroCore.Models.GeneralModel import GeneralModel
########################################
###           Packages               ###
########################################
from NeuroCore.Neuron.Segment.Base import ISegment
from Plotting.IDataPlot import IDataPlot
from Plotting.Simulation import Simulation

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(space=[0, 1], time=[0, 10])
simSteps = Steps(space=0.01, time=0.1)

diffusionValue = 1
reactionValue = 1
kValue = 1

boundaryConditions = BoundaryConditions(KilledEnd(), KilledEnd())

sElements = arange(0, simDomain.space[-1] + simSteps.space, simSteps.space)

########################################
###      Setting the Simulation      ###
######################################## 


analytical = ValidationWithF(domain=simDomain, steps=simSteps, BCs=boundaryConditions, kValue=kValue)

font = analytical.createFont()

initialCondition = analytical.createInitialCondition()

V_0 = []

for x in sElements:
    V_0.append(initialCondition(x))

simModel = GeneralModel(iApproximation=GalerkinApproximation(), timeApproximation=BackwardEuler(),
                        initialCondition=V_0, font=font, coeff_dx2=-diffusionValue, coeff_v=reactionValue,
                        coeff_t=1 / kValue)

segment0 = ISegment('Axon0', boundaryConditions, simDomain, simSteps, simModel)

########################################
###      Running the Simulation      ###
######################################## 

analyticalResult = analytical.solve()

result = []
result.append(V_0)

timeElements = arange(simSteps.time, simDomain.time[-1] + simSteps.time, simSteps.time)
for t in timeElements:
    result.append(segment0.solve(currentTime=t))

approxPlot = IDataPlot(name=simModel.name + " - Approximation", domain=simDomain, steps=simSteps, results=result,
                       color="b")
analyPlot = IDataPlot(name=analytical.name + " - Analytical", domain=simDomain, steps=simSteps,
                      results=analyticalResult, color="k")

plotting = Simulation(plots=[analyPlot, approxPlot])
plotting.save("transientResult.mp4")

# plotting = Simulation(plots=approxPlot)
# plotting.save("approxResult.mp4")
