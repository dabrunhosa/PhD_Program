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

import time

import numpy

from Analytics.Solutions.Validations.Stationary import ValidationZeroF
from Conventions.Analytics.Solutions.Validations.Stationary import StationaryParameters as analyticConstants
from Conventions.NeuroCore.Models.GeneralModel import GeneralModelParameters as modelConstants
from Conventions.Plotting.BasicPlottingColors import BasicPlottingColors as colorConstants
from Conventions.Plotting.SimulationPlotingParameters import SimulationPlotingParameters as plotConstants
from Conventions.NeuroCore.Neuron.Segment.Base import BaseParameters as segmentConstants
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from NeuroCore.Models.Conditions.BCs import BoundaryConditions
from NeuroCore.Models.Conditions.Neumanns import Neumann
from NeuroCore.Models.Conventions import Domains, Steps
from NeuroCore.Models.GeneralModel import GeneralModel
from NeuroCore.Neuron.Segment.Base import ISegment
from Plotting.IDataPlot import IDataPlot
from Plotting.Simulation import Simulation

########################################
###      Simulation Variable         ###
######################################## 

simDomain = Domains(space=[0, 1])
simSteps = Steps(space=0.01)


########################################
###      Setting the Simulation      ###
######################################## 

def f(x):
    return 0


diffusionValue = 0.1
reactionValue = 10

boundaryConditions = BoundaryConditions(Neumann(bcValue=1), Neumann(bcValue=1))

simModel = GeneralModel(**{modelConstants().IApproximation: GalerkinApproximation(),
                           modelConstants().Font: f,
                           modelConstants().CoeffDx2: -diffusionValue,
                           modelConstants().CoeffV: reactionValue})

segment0 = ISegment(**{segmentConstants().Name:'Axon0',
                       segmentConstants().LocalConditions:boundaryConditions,
                       segmentConstants().Domain:simDomain,
                       segmentConstants().Steps:simSteps,
                       segmentConstants().IModel:simModel})

########################################
###      Running the Simulation      ###
######################################## 

sElements = numpy.arange(0, simDomain.space[-1] + simSteps.space, simSteps.space)

analytical = ValidationZeroF(**{analyticConstants().Domain: simDomain,
                                analyticConstants().Steps: simSteps,
                                analyticConstants().BCs: boundaryConditions,
                                analyticConstants().DiffusionValue: diffusionValue, \
                                analyticConstants().ReactionValue: reactionValue})
analyticalResult = analytical.solve()

t_start = time.clock()
result = segment0.solve()[-1]

approxPlot = IDataPlot(**{plotConstants().Name: simModel.name,
                          plotConstants().Domain: simDomain,
                          plotConstants().Steps: simSteps,
                          plotConstants().Results: result,
                          plotConstants().Color: colorConstants().Blue})

analyPlot = IDataPlot(**{plotConstants().Name: analytical.name,
                         plotConstants().Domain: simDomain,
                         plotConstants().Steps: simSteps,
                         plotConstants().Results: analyticalResult,
                         plotConstants().Color: colorConstants().Black})

plotting = Simulation(**{plotConstants().Plots: [analyPlot, approxPlot]})
plotting.save("stationaryNoFont.png")
