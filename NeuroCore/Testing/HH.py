#-*- coding: utf-8 -*-
"""
Created on Mon December 18 09:23:02 2017

@author: Daniel Abrunhosa
"""


'''
Problem being solved is: [0,1]X[0,T]
    HH
'''

########################################
###           Packages               ###
######################################## 

from NeuroCore.Neuron.Segment.Base import ISegment
from NeuroCore.Models.HHModel import HHModel
from NeuroCore.Models.Conventions import Domains,Steps
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from NeuroCore.Approximations.Time.BackwardEuler import BackwardEuler
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Neumanns import SealedEnd
from Plotting.Simulation import Simulation
from Plotting.IDataPlot import IDataPlot
from numpy import arange

#from cmath import pi,cos
#from math import pow

from NeuroCore.Approximations.Space.FEM.Integration.Trapezoidal import Trapezoidal

#import inspect

from NeuroCore.Equations.Coefficient.Base import ICoefficient

def f_x(x):
    return x*1.0

#def f_x_t(x,t):
#    return 1.0

#def f_x_t_V(x,t,V):
#    return 1.0

#ICoefficient(1.0)
test = ICoefficient(f_x)
test(x=2)
#ICoefficient(f_x_t)
#ICoefficient(f_x_t_V)

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(space=[0,1],time=[0,1])
simSteps = Steps(space=0.1,time=0.1)

diffusionValue = 1/pow(2,10)
reactionValue = 1
timeValue = 1

boundaryConditions = BoundaryConditions(SealedEnd(),SealedEnd())

sElements = arange(0, simDomain.space[-1] + simSteps.space,\
                                simSteps.space)

########################################
###      Setting the Simulation      ###
######################################## 

V_0 = []

for x in sElements:
    V_0.append(0.0)

simModel = HHModel(iApproximation=GalerkinApproximation(numIntegration=Trapezoidal()),\
                      timeApproximation=BackwardEuler(),\
                      initialCondition=V_0,coeff_dx2 = -diffusionValue,\
                      coeff_v = reactionValue,\
                      coeff_t = timeValue)

segment0 = ISegment('Axon0',boundaryConditions,simDomain,simSteps,simModel)

########################################
###      Running the Simulation      ###
######################################## 

result = []
result.append(V_0)

timeElements = arange(simSteps.time , simDomain.time[-1] + simSteps.time, simSteps.time) 
for t in timeElements:
    result.append(segment0.solve(currentTime=t))

#print("Approx Solution:",result)
approxPlot = IDataPlot(name=simModel.name,domain=simDomain,steps=simSteps,results=result,color="red")

plotting = Simulation(iDataPlots=approxPlot)
plotting.save("HHResult.mp4")
    

