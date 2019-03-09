# -*- coding: utf-8 -*-
"""
Created on Mon May  21

@author: Daniel Abrunhosa
"""


'''
Problem being solved is: [0,1]U[1,2]U[1,3] X [0,1]
    This is an example used by Jemmy in a Y Domain.
    Although it does not look like it, all the 
    segments have the same length.    
    BC:
    du/dx(0) = du/dx(3) = du/dx(2) = 0
    du/dx(1) - du/dx(1) - du/dx(1) = 0 - derivative continuity
    u(1) = u(1) = u(1) - variable continuity

    Initial Conditions:
    u(0,x) = cos(pi*x)

'''

########################################
###           Packages               ###
######################################## 
from NeuroCore.Neuron.Segment.Base import ISegment
from NeuroCore.Models.GeneralModel import GeneralModel
from NeuroCore.Models.Conventions import Domains,Steps
from NeuroCore.Approximations.Space.FEM.GalerkinApproximation import GalerkinApproximation
from NeuroCore.Approximations.Time.BackwardEuler import BackwardEuler
from Analytics.Solutions.Validations.YDomain.Transient import JemmyEx1
from Plotting.Simulation import Simulation
from Plotting.IDataPlot import IDataPlot
from numpy import arange,zeros

########################################
###      Simulation Variable         ###
########################################

simSteps = Steps(space=0.1,time=0.1)

analytical = JemmyEx1(steps=simSteps)

########################################
###      Setting the Simulation      ###
######################################## 

 
font = analytical.createFont()

initialCondition = analytical.createInitialCondition()

[V_0E,V_0Lw,V_0Up] = [[initialCondition(x) for x in analytical.sElementsE],
                      [initialCondition(x) for x in analytical.sElementsLw],
                      [initialCondition(x) for x in analytical.sElementsUp]]

# print("V_0:",len(analytical.sElementsE))
# print("\n\nV_0Lw:",len(analytical.sElementsLw))
# print("\n\nV_0 Up:",len(analytical.sElementsUp))

#V_0 = numpy.transpose(V_0)

diffusionValue = 1.0
reactionValue = 1.0
timeValue = 1.0

simModelE = GeneralModel(iApproximation=GalerkinApproximation(),timeApproximation=BackwardEuler(),
                         initialCondition=V_0E,font=font,coeff_dx2=-diffusionValue,
                         coeff_v=reactionValue,coeff_t=timeValue)

simModelLw = GeneralModel(iApproximation=GalerkinApproximation(),timeApproximation=BackwardEuler(),
                          initialCondition=V_0Lw,font=font,coeff_dx2 = -diffusionValue,
                          coeff_v = reactionValue,coeff_t = timeValue)

simModelUp = GeneralModel(iApproximation=GalerkinApproximation(),timeApproximation=BackwardEuler(),
                          initialCondition=V_0Up,font=font,coeff_dx2=-diffusionValue,
                          coeff_v=reactionValue,coeff_t=timeValue)

segmentE = ISegment('AxonE',analytical.bcDomainE,analytical.domainE,simSteps,simModelE)
segmentLw = ISegment('AxonLw',analytical.bcDomainLw,analytical.domainLw,simSteps,simModelLw)
segmentUp = ISegment('AxonUp',analytical.bcDomainUp,analytical.domainUp,simSteps,simModelUp)

########################################
###      Running the Simulation      ###
########################################

#Domain Decomposition Part

decompMatrix = zeros((6, 6))
decompMatrix[0][0] = 1

decompMatrix[1][1] = 1
decompMatrix[1][2] = -1
decompMatrix[1][4] = -1

decompMatrix[2][2] = 1

decompMatrix[3][0] = -1
decompMatrix[3][1] = -1
decompMatrix[3][2] = -1
decompMatrix[3][3] = -1

decompMatrix[4][4] = 1

decompMatrix[5][0] = -1
decompMatrix[5][1] = -1
decompMatrix[5][4] = -1
decompMatrix[5][5] = -1

decompFont = zeros(6)
decompFont[0] = analytical.bcDomainE
decompFont[2] = analytical.bcDomainUp
decompFont[3] = 1
decompFont[4] = analytical.bcDomainLw
decompFont[5] = 1

[analyticalResultE,analyticalResultLw,analyticalResultUp] = analytical.solve()

[resultE,resultLw,resultUp] = [[V_0E],[V_0Lw],[V_0Up]]

timeElements = arange(simSteps.time , analytical.domainE.time[-1] + simSteps.time, simSteps.time)
for t in timeElements:
    resultE.append(segmentE.solve(currentTime=t))
    resultLw.append(segmentLw.solve(currentTime=t))
    resultUp.append(segmentUp.solve(currentTime=t))







# print("Left Result:")
#
# for leftTime in resultE:
#     print(len(leftTime))

# print("\n\n Lower Domain:")
#
# for lowerTime in resultLw:
#     print(lowerTime)

# print("\n\n Upper Domain:")
#
# for upperTime in resultUp:
#     print(upperTime)


approxPlotE = IDataPlot(name=simModelE.name,domain=analytical.domainE,steps=simSteps,results=resultE)
approxPlotLw = IDataPlot(name=simModelLw.name,domain=analytical.domainLw,steps=simSteps,results=resultLw)
approxPlotUp = IDataPlot(name=simModelUp.name,domain=analytical.domainUp,steps=simSteps,results=resultUp)

analyPlotE = IDataPlot(name=analytical.name,domain=analytical.domainE,steps=simSteps,results=analyticalResultE)
analyPlotLw = IDataPlot(name=analytical.name,domain=analytical.domainLw,steps=simSteps,results=analyticalResultLw)
analyPlotUp = IDataPlot(name=analytical.name,domain=analytical.domainUp,steps=simSteps,results=analyticalResultUp)

plotting = Simulation(plots=[analyPlotE,approxPlotE])
plotting.save("leftDomain.mp4")

plotting = Simulation(plots=[analyPlotLw,approxPlotLw])
plotting.save("lowerDomain.mp4")

plotting = Simulation(plots=[analyPlotUp,approxPlotUp])
plotting.save("upperDomain.mp4")

