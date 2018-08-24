# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:40:33 2017

@author: Daniel Abrunhosa
"""

from Conventions.Classes import Components
from Conventions.Classes import Names
from Conventions.NeuroCore.Models.Conditions.BCs import BCsParameters as constants
from Conventions.NeuroCore.Models.Conditions.Base import BaseParameters as Type
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options


class BoundaryConditions(IHaveOption):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, inStart, inEnd, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().BoundaryCondition,
                                   constants().InStart: inStart,
                                   constants().InEnd: inEnd})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(BoundaryConditions, self).__init__(whole_options, **kw)

        ########################################

    ###       Public Functions           ###
    ######################################## 

    '''
    Could be a method that receives a matrix or font and applies 
    the boundary conditions. If in FEM (inheritance) can apply 
    in the correct way as well.
    '''

    def apply(self, matrix, font, **arguments):

        #        print("Apply BC:",self.inStart.bcType,self.inEnd.bcType)

        if self.inStart.bcType == Type().Neumann:
            font[0] += self.inStart.bcValue * arguments[Components().Diffusion]

        if self.inEnd.bcType == Type().Neumann:
            font[-1] += -self.inEnd.bcValue * arguments[Components().Diffusion]

        if self.inStart.bcType == Type().Dirichlet:
            matrix[0, :] = 0
            matrix[0, 0] = 1

            font[0] = self.inStart.bcValue

        if self.inEnd.bcType == Type().Dirichlet:
            matrix[-1, :] = 0
            matrix[-1, -1] = 1

            font[-1] = self.inEnd.bcValue

        return [matrix, font]
