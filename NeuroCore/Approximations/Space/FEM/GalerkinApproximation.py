# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:50:56 2017

@author: daniel
"""
# To save data pickle or json very code tools for that

from Conventions.Classes import Components
from Conventions.Classes import Names
from Conventions.Parameters import Parameters as constants
from NeuroCore.Approximations.Space.FEM.Base import FEM_Approximation
from NeuroCore.Equations.Component.FEM.Galerkin.Diffusion import Diffusion
from NeuroCore.Equations.Component.FEM.Galerkin.Font import Font
from NeuroCore.Equations.Component.FEM.Galerkin.Previous import Previous
from NeuroCore.Equations.Component.FEM.Galerkin.Reaction import Reaction
from Utilities.DataEntry import Options


class GalerkinApproximation(FEM_Approximation):

    ########################################
    ###           Constructor            ###
    ########################################  

    def __init__(self, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Name: Names().ClassicGalerkin})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(GalerkinApproximation, self).__init__(whole_options, **kw)

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def create_diffusion(self, coeff=1.0):
        '''A method necessary to define how to create a galerkin
        diffusion. It adds this new term of the equation to the
        model's equation.'''
        coeff = self.modifyCoeff(Components().Diffusion, coeff)
        return Diffusion(weightFunction=self.weightFunction, coeff=coeff)

    def create_reaction(self, coeff=1.0):
        '''A method necessary to define how to create a galerkin
        reaction. It adds this new term of the equation to the
        model's equation.'''
        coeff = self.modifyCoeff(Components().Reaction, coeff)
        return Reaction(weightFunction=self.weightFunction, coeff=coeff)

    def create_font(self, coeff=1.0):
        '''A method necessary to define how to create a galerkin
        reaction. It adds this new term of the equation to the
        model's equation.'''
        coeff = self.modifyCoeff(Components().Font, coeff)
        return Font(weightFunction=self.weightFunction, coeff=coeff)

    def create_previous(self, coeff=1.0):
        '''A method necessary to define how to create a galerkin
        reaction. It adds this new term of the equation to the
        model's equation.'''
        coeff = self.modifyCoeff(Components().Time, coeff)
        return Previous(weightFunction=self.weightFunction, coeff=coeff)
