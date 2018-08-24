## -*- coding: utf-8 -*-
# '''
# Created on May 30, 2014

# @author: dabrunhosa
# '''

# '''
# Problem being solved is: [0,1]X[0,T]
#    1/k*du/dt - d2u/dx2 + u = f
#    f = 4*pi2*(e^(-kt))*sin(2*pi*x)

#    BC:
#        u(0,t) = u(1,t) = 0

#    Initial Conditions:
#        u(x,0) = sin(2*pi*x)
# '''

#########################################
####           Packages               ###
######################################### 

from NeuroCore.Neuron.Segment.Base import ISegment
from NeuroCore.Models.PassiveCableModel import CableModel
from NeuroCore.Models.Conventions import Domains,Steps
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
#from Approximations.Time.BackwardEuler import BackwardEuler
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Dirichlets import KilledEnd

import numpy
import math
import time

########################################
###      Simulation Variable         ###
########################################

length = 1
T = 10

delta_x = 0.1
delta_t = 0.1

simDomain = Domains(time=[0,T],space=[0,length])
simSteps = Steps(time=delta_t,space=delta_x)

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
###      Mesh Prep Work              ###
########################################

k = 1
coeff_t = 1/k
coeff_dx2 = -1
coeff_v = 1

def f(x,t):
   return 4*(math.pi**2)*math.exp(-t)*math.sin(2*math.pi*x)

simModel = CableModel(iApproximation=GalerkinApproximation(),\
                      font=f,coeff_dx2 = coeff_dx2,coeff_v = coeff_v,
                      coeff_t=coeff_t,)

segment0 = ISegment('Axon0',BoundaryConditions(KilledEnd(),KilledEnd()),\
                    simDomain,simSteps,simModel)

#geoMesh = ISegment()
#geoMesh.insert_segments(segment0)


########################################
###      Setting the Simulation      ###
########################################

#ode_approximation = BackwardEuler(delta_t=delta_t,coeff_t=coeff_t)


#geoMesh.create_region(cable_model)

#Identify all the boundary conditions and return a list with
#default values and types
#boundary_conditions = geoMesh.identify_boundary_conditions()

#Set the boundary conditions to the desired type and
#value
#for key in boundary_conditions.keys():
#   boundary_conditions.set(key,Dirichlet(0))

########################################
###      Running the Simulation      ###
########################################

t_start = time.clock()
#geoMesh.solve(boundary_conditions, delta_t=delta_t, final_time=T)
result = segment0.solve()
print("Result:",result)
print("Elapsed Time:",time.clock()-t_start)


