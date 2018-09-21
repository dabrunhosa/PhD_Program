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
from Conventions.Analytics.Solutions.Validations.Transient import TransientParameters as analyticConstants
from Conventions.NeuroCore.Models.GeneralModel import GeneralModelParameters as modelConstants
from Conventions.Plotting.BasicPlottingColors import BasicPlottingColors as colorConstants
from Conventions.Plotting.SimulationPlotingParameters import SimulationPlotingParameters as plotConstants
from Conventions.NeuroCore.Neuron.Segment.Base import BaseParameters as segmentConstants
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

analytical = ValidationWithF(**{analyticConstants().Domain: simDomain,
                                analyticConstants().Steps: simSteps,
                                analyticConstants().KValue: kValue})

font = analytical.createFont()

initialCondition = analytical.createInitialCondition()

V_0 = []

for x in sElements:
    V_0.append(initialCondition(x))

simModel = GeneralModel(**{modelConstants().IApproximation: GalerkinApproximation(),
                           modelConstants().TimeApproximation: BackwardEuler(),
                           modelConstants().InitialCondition:V_0,
                           modelConstants().Font: font,
                           modelConstants().CoeffDx2: -diffusionValue,
                           modelConstants().CoeffV: reactionValue,
                           modelConstants().CoeffT: 1/kValue})

segment0 = ISegment(**{segmentConstants().Name:'Axon0',
                       segmentConstants().LocalConditions:boundaryConditions,
                       segmentConstants().Domain:simDomain,
                       segmentConstants().Steps:simSteps,
                       segmentConstants().IModel:simModel})

########################################
###      Running the Simulation      ###
######################################## 

analyticalResult = analytical.solve()

result = []
result.append(V_0)

timeElements = arange(simSteps.time, simDomain.time[-1] + simSteps.time, simSteps.time)
for t in timeElements:
    result.append(segment0.solve(currentTime=t))

approxPlot = IDataPlot(**{plotConstants().Name: simModel.name + " - Approximation",
                          plotConstants().Domain: simDomain,
                          plotConstants().Steps: simSteps,
                          plotConstants().Results: result,
                          plotConstants().Color: colorConstants().Blue})

analyPlot = IDataPlot(**{plotConstants().Name: analytical.name + " - Analytical",
                         plotConstants().Domain: simDomain,
                         plotConstants().Steps: simSteps,
                         plotConstants().Results: analyticalResult,
                         plotConstants().Color: colorConstants().Black})

plotting = Simulation(**{plotConstants().Plots: [analyPlot, approxPlot]})
plotting.save("transientResult.mp4")
