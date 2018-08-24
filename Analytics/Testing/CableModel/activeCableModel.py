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

########################################
###           Packages               ###
######################################## 
from NeuroCore.Neuron.Segment.Base import ISegment
from NeuroCore.Models.CableModel.Passive.Transient import CableModel
from NeuroCore.Models.Conventions import Domains,Steps
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from NeuroCore.Approximations.Time.BackwardEuler import BackwardEuler
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Dirichlets import KilledEnd
from Analytics.Solutions.Validations.Transient import CableModelWithF
from Plotting.Simulation import Simulation
from Plotting.IDataPlot import IDataPlot
from numpy import arange

#from cmath import pi,cos
#from math import pow

#import inspect

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(space=[0,1],time=[0,10])
simSteps = Steps(space=0.1,time=0.1)

diffusionValue = 1
reactionValue = 1
kValue = 1

boundaryConditions = BoundaryConditions(KilledEnd(),KilledEnd())

sElements = arange(0, simDomain.space[-1] + simSteps.space,\
                                simSteps.space)

########################################
###      Setting the Simulation      ###
######################################## 


analytical = CableModelWithF(domain=simDomain,steps=simSteps,\
                             BCs=boundaryConditions,\
                             kValue = kValue)
 
font = analytical.createFont()
#firstFont = partial(font,t=0.1)

#def linear(x):
#    x = (simSteps.space/2)*x + (1/2)*0.1
#    return firstFont(x)*((1+x)/2)*simSteps.time*simSteps.space/2

#integration = Gaussian()
#value = integration.solve(function=linear)

initialCondition = analytical.createInitialCondition()

V_0 = []

for x in sElements:
    V_0.append(initialCondition(x))

#V_0 = numpy.transpose(V_0)

simModel = CableModel(iApproximation=GalerkinApproximation(),\
                      timeApproximation=BackwardEuler(),\
                      initialCondition=V_0,\
                      font=font,coeff_dx2 = -diffusionValue,\
                      coeff_v = reactionValue,\
                      coeff_t = 1/kValue)

segment0 = ISegment('Axon0',boundaryConditions,simDomain,simSteps,simModel)

########################################
###      Running the Simulation      ###
######################################## 

analyticalResult = analytical.solve()

#print("Analytical Solution:",analyticalResult)

#t_start = time.clock()
result = []
result.append(V_0)

timeElements = arange(simSteps.time , simDomain.time[-1] + simSteps.time, simSteps.time) 
for t in timeElements:
    result.append(segment0.solve(currentTime=t))

#print("Approx Solution:",result)
approxPlot = IDataPlot(name=simModel.name,domain=simDomain,steps=simSteps,results=result)
analyPlot = IDataPlot(name=analytical.name,domain=simDomain,steps=simSteps,results=analyticalResult)

plotting = Simulation(iDataPlots=analyPlot)
plotting.save("analyResult.mp4")

plotting = Simulation(iDataPlots=approxPlot)
plotting.save("approxResult.mp4")

#print("Result:",result)
#print("Elapsed Time:",time.clock()-t_start)
    
