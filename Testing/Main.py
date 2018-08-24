# -*- coding: utf-8 -*-
'''
Created on May 30, 2014

@author: dabrunhosa
'''

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
from NeuroCore.Models.PassiveCableModel import GenericModel
from NeuroCore.Models.Conventions import Domains,Steps
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
#from Approximations.Time.BackwardEuler import BackwardEuler
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Dirichlets import KilledEnd
from math import pi, pow, sin

import numpy
import math
import time

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(time=[0,10],space=[0,1])
simSteps = Steps(time=0.1,space=0.1)

spatial_elements = numpy.arange(0, simDomain.space[-1] + simSteps.space,\
                                simSteps.space)

time_elements = numpy.arange(0, simDomain.time[-1] + simSteps.time, simSteps.time)
 
V_0 = []

def u0(x):
    return math.sin(2*math.pi*x)  

for x in spatial_elements:
    V_0.append(u0(x))

V_0 = numpy.transpose(V_0)

########################################
###      Setting the Simulation      ###
######################################## 

k = 1

#def f(x,t):
#    return 4*(math.pi**2)*math.exp(-t)*math.sin(2*math.pi*x)

def f(x):
    return (1 + 4*pow(pi,2))*sin(2*pi*x)

#simModel = CableModel(iApproximation=GalerkinApproximation(),\
#                     timeApproximation=BackwardEuler(),font=f,\
#                     coeff_t = 1/k,coeff_dx2 = -1,coeff_v = 1)

simModel = GenericModel(iApproximation=GalerkinApproximation(),\
                      font=f,coeff_dx2 = -1,coeff_v = 1)

segment0 = ISegment('Axon0',BoundaryConditions(KilledEnd(),KilledEnd()),\
                    simDomain,simSteps,simModel)

#geoMesh = NetXNeuron()
#sgeoMesh.insert_segments(segment0)

########################################
###      Running the Simulation      ###
######################################## 

t_start = time.clock()
#number_time_loops = (int)(simDomain.time[-1] / simSteps.time)  
#for t in range(number_time_loops):
result = segment0.solve()
print("Result:",result)
print("Elapsed Time:",time.clock()-t_start)
    
