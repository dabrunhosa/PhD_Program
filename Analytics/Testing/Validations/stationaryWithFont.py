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
from Conventions.Analytics.Solutions.Validations.Stationary import StationaryParameters as analyticConstants
from Conventions.NeuroCore.Models.GeneralModel import GeneralModelParameters as modelConstants
from Conventions.Plotting.BasicPlottingColors import BasicPlottingColors as colorConstants
from Conventions.Plotting.SimulationPlotingParameters import SimulationPlotingParameters as plotConstants
from Conventions.NeuroCore.Neuron.Segment.Base import BaseParameters as segmentConstants
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

analytical = ValidationWithF(**{analyticConstants().Domain: simDomain,
                                analyticConstants().Steps: simSteps,
                                analyticConstants().BCs: boundaryConditions,
                                analyticConstants().DiffusionValue: diffusionValue, \
                                analyticConstants().ReactionValue: reactionValue})

font = analytical.createFont()

simModel = GeneralModel(**{modelConstants().IApproximation: GalerkinApproximation(),
                           modelConstants().Font: font,
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
plotting.save("stationaryWithFont.png")
