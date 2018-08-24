# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 07:59:42 2017

@author: daniel
"""

from numpy import zeros, cfloat
from scipy.sparse import lil_matrix

from Conventions.Classes import Components
from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Space.FEM.Elements.IElementParameters import IElementParameters as constants
from Utilities.BaseOption import ISolvable
from Utilities.DataEntry import Options


class IElement(ISolvable):

    ########################################
    ###           Constructor            ###
    ########################################

    # def __new__(cls, *args, **kwargs):

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().FEMElement,
                                     constants().Domain: None,
                                     constants().NumLocalNodes: None,
                                     constants().NumIntegration: None,
                                     constants().Matrix: None,
                                     constants().Font: None,
                                     constants().CoupledApprox: None,
                                     constants().ExtraData: {constants().Previous: []},
                                     constants().Bilinear: None,
                                     constants().Linear: None})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IElement, self).__init__(whole_options, **kw)

        self.__prepareData()

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __prepareData(self):
        self.matrix = lil_matrix((self.numLocalNodes, self.numLocalNodes), dtype=cfloat)
        self.font = zeros(self.numLocalNodes, dtype=cfloat)

    #        self.matrix = lil_matrix((self.numLocalNodes,self.numLocalNodes))
    #        self.font = zeros(self.numLocalNodes)

    ########################################
    ###       Public Functions           ###
    ########################################   

    def stationarySolve(self, **arguments):

        for i in range(self.numLocalNodes):

            for j in range(self.numLocalNodes):
                self.matrix[i, j] = self.numIntegration. \
                    solve(function=self.bilinear(domain=self.domain, \
                                                 line=i, column=j))

            self.font[i] = self.numIntegration. \
                solve(function=self.linear(domain=self.domain, \
                                           line=i, column=i))

        return [self.matrix, self.font]

    def transientSolve(self, **arguments):

        paramters = {}
        paramters[constants().Domain] = self.domain

        for i in range(self.numLocalNodes):

            paramters[Components().Time] = self.extraData[constants().Previous]
            paramters[constants().Column] = i
            paramters[constants().Column().Line] = i

            for j in range(self.numLocalNodes):
                self.matrix[i, j] = self.numIntegration.solve(
                    function=self.bilinear(domain=self.domain, line=i, column=j))

                paramters[Components().Time] = self.extraData[constants().Previous]
                paramters[constants().Domain] = self.domain
                paramters[constants().Column] = i
                paramters[constants().Line] = i

                self.font[i] = self.numIntegration. \
                    solve(function=self.linear(**paramters))

        return [self.matrix, self.font]

    def coupledSolve(self, **arguments):

        for i in range(self.numLocalNodes):

            for j in range(self.numLocalNodes):
                self.matrix[i, j] = self.numIntegration. \
                    solve(function=self.bilinear(domain=self.domain, \
                                                 line=i, column=j))

            self.font[i] = self.numIntegration. \
                solve(function=self.linear(domain=self.domain, \
                                           line=i, column=i, \
                                           Time=self.extraData[constants().Previous]))

        return [self.matrix, self.font]

    def solve(self, **arguments):

        #        print(self.bilinear)
        #        print(self.linear)

        if len(self.extraData[constants().Previous]) != 0:
            if self.coupledApprox is not None:
                return self.coupledSolve(**arguments)
            else:
                return self.transientSolve(**arguments)
        else:
            return self.stationarySolve(**arguments)
