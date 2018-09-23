# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:03:39 2017

@author: daniel
"""
from abc import ABC
from functools import partial

from scipy.sparse.linalg import spsolve

from Conventions.Classes import Names
from Conventions.Classes import Sides, Components
from Conventions.NeuroCore.Approximations.Space.FEM.Base import BaseParameters as constants
from NeuroCore.Approximations.Space.FEM.Elements.IElements import IElements
from NeuroCore.Approximations.Space.FEM.Integration.Gaussian import Gaussian
from NeuroCore.Approximations.Space.FEM.Weight_Function.LinearLagrange import Linear_Lagrange
from NeuroCore.Approximations.Space.IApproximation import IApproximation
# from Equations.Component.FEM.Galerkin.Discrete import Discrete
from NeuroCore.Equations.Composite.FEM import IFEM
from Utilities.DataEntry import Options
from Utilities.Handler import Function


class FEM_Approximation(IApproximation, ABC):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().FEM,
                                     constants().ReferenceElement: True,
                                     constants().Modifiers: {},
                                     constants().WeightFunction: Linear_Lagrange(),
                                     constants().NumIntegration: Gaussian(),
                                     constants().IElements: None})

        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions

        super(FEM_Approximation, self).__init__(options=options, defaultOptions = defaultOptions, **kw)
        self.iElements = IElements(numLocalNodes=self.weightFunction.numLocalNodes, \
                                   numIntegration=self.numIntegration)

    ########################################
    ###       Private Functions          ###
    ########################################

    def __defineModifiers(self):
        self.modifiers[Components().Diffusion] = (-2 / self.steps.space)
        self.modifiers[Components().Reaction] = (self.steps.space / 2)
        self.modifiers[Components().Font] = (self.steps.space / 2)
        self.modifiers[Components().Time] = (self.steps.space / 2)

    def __setattr__(self, attributeName, value):
        super(FEM_Approximation, self).__setattr__(attributeName, value)

        #        print("Attribute:",attributeName,"Value:",value)

        if attributeName == constants().CurrentTime and value is not None:
            if self.currentTime > 0:
                currentLinear = self.iElements.linear
                currentLinear.getEquation(Components().Font). \
                    font = partial(self.font, t=self.currentTime)

                self.iElements.linear = currentLinear

        if attributeName == constants().Domain and value is not None:
            self.iElements.domain = self.domain

        if attributeName == constants().Steps and value is not None:
            self.iElements.steps = self.steps
            self.__defineModifiers()

        if attributeName == constants().Equation and value is not None:
            font = self.font

            if self.currentTime == 0:
                self.iElements.previous = self.results[-1]
                font = partial(font, t=0)

            self.equation[Sides().Right].getEquation(Components().Font).font = font
            self.iElements.bilinear = self.equation[Sides().Left]
            self.iElements.linear = self.equation[Sides().Right]

    ########################################
    ###       Public Functions           ###
    ########################################

    def modifyCoeff(self, equationName, coeff):

        if self.referenceElement:
            coeff = Function(coeff)
            coeff.inConstant = self.modifiers[equationName]

        return coeff

    def create_composed(self, **arguments):
        return IFEM(**arguments)

    def solve(self, **arguments):
        [self.inMatrix, self.inFont] = self.iElements.solve(**arguments)

        [self.inMatrix, self.inFont] = self.BCs.apply(self.inMatrix, \
                                                      self.inFont, Diffusion=self. \
                                                      coeffs[Components().Diffusion])

        #        print("Matrix:",self.inMatrix,"\nFont:",self.inFont)

        self.results.append(spsolve(self.inMatrix, self.inFont))
        self.iElements.previous = self.results[-1]

        #        self.results.append(solve(self.inMatrix,self.inFont))

        return self.results[-1]
