# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:12:36 2017

@author: Daniel Abrunhosa
"""


class Names(object):
    @property
    def Default(self):
        return "Default"

    @property
    def Function(self):
        return "Function"

    @property
    def IDataPlot(self):
        return "IDataPlot"

    @property
    def IDataPlots(self):
        return "IDataPlots"

    @property
    def SimuPlots(self):
        return "SimuPlots"

    @property
    def IPlot(self):
        return "IPlot"

    @property
    def FEMElement(self):
        return "FEMElement"

    @property
    def FEMElements(self):
        return "FEMElements"

    @property
    def FEMComponent(self):
        return "FEMComponent"

    @property
    def GenericIntegration(self):
        return "Generic Integration"

    @property
    def GaussianQuadrature(self):
        return "Gaussian Quadrature"

    @property
    def Trapezoidal(self):
        return "Trapezoidal"

    @property
    def FEM(self):
        return "FEM"

    @property
    def ClassicGalerkin(self):
        return "Classic Galerkin"

    @property
    def Approximation(self):
        return "Approximation"

    @property
    def GeneralModel(self):
        return "General Model"

    @property
    def StationaryBaseClass(self):
        return "Stationary Base Class"

    @property
    def ValidationZeroF(self):
        return "CableModel with F = 0"

    @property
    def ValidationWithF(self):
        return "CableModel Model With Font"

    @property
    def IModel(self):
        return "IModel"

    @property
    def GeneralModel(self):
        return "General Model"

    @property
    def WeightFunction(self):
        return "Weight Function"

    @property
    def TimeApproximation(self):
        return "Time Approximation"

    @property
    def BackwardEuler(self):
        return "Backward Euler"

    @property
    def CoupledHHAproximations(self):
        return "Coupled HH Aproximations"

    @property
    def Equation(self):
        return "Equation"

    @property
    def Component(self):
        return "Component"

    @property
    def Composite(self):
        return "Composite"

    @property
    def FEMComposite(self):
        return "FEM Composite"

    @property
    def IProblem(self):
        return "IProblem"

    @property
    def IAnalysis(self):
        return "IAnalysis"

    @property
    def BoundaryCondition(self):
        return "Boundary Condition"

    @property
    def BoundaryConditions(self):
        return "Boundary Conditions"

    @property
    def Dirichlet(self):
        return "Dirichlet"

    @property
    def VoltageClamp(self):
        return "Voltage-Clamp"

    @property
    def KilledEnd(self):
        return "Killed-End"

    @property
    def Neumann(self):
        return "Neumann"

    @property
    def SealedEnd(self):
        return "Sealed-End"

    @property
    def CurrentInjection(self):
        return "Current Injection"


class Sides(object):
    @property
    def Left(self):
        return "Left"

    @property
    def Right(self):
        return "Right"


class Components(object):
    @property
    def Diffusion(self):
        return "Diffusion"

    @property
    def Reaction(self):
        return "Reaction"

    @property
    def Font(self):
        return "Font"

    @property
    def Time(self):
        return "Time"

    @property
    def Discrete(self):
        return "Discrete"


class Descriptions(object):

    @property
    def IAnalysis(self):
        return "This is a Interface Class"

    @property
    def IProblem(self):
        return "A Problem Interface"

    @property
    def StationaryBaseClass(self):
        return "A Base Class for Stationary Solutions"

    @property
    def ValidationZeroF(self):
        return "This is the solution for the following problem:\
                                  Problem being solved is: [0,X] \
                                  -epsilon*d2u/dx2 + theta*u = 0 \
                                  BC:\
                                  du/dx(0) = u0 \
                                  du/dx(1) = u1\
                                  Solution:\
                                  u = alpha*sinh(lambda*x) + beta*cosh(lambda*x)\
                                  alpha = u0/lambda\
                                  beta = u1 - u0*cosh(lambda)/lambda*sinh(lambda)\
                                  lambda = sqrt(theta)/sqrt(epsilon)"

    @property
    def ValidationWithF(self):
        return "This is the solution for the \
                                                  following problem:\
                                                  Problem being solved is: [0,X]\
                                                  - epsilon*d2u/dx2 + theta*u = f \
                                                  f =  (theta + epsilon*4*(pi^2))*cos(2*pi*x)\
                                                  BC: du/dx(0) = du/dx(1) = 0 \
                                                  Solution: u = cos(2*pi*x)"
