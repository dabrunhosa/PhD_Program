# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:53:14 2017

@author: daniel
"""

import sys

from numpy import cfloat
from numpy import zeros
from scipy.sparse import lil_matrix

from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Space.FEM.Elements.IElementsParameters import IElementsParameters as constants
from Conventions.NeuroCore.Models.Conventions import ConventionsParameters as conventionsConstants
from NeuroCore.Approximations.Space.FEM.Elements.IElement import IElement
from Utilities.BaseOption import ISolvable
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options


# from abc import ABCMeta, abstractmethod

class IElements(ISolvable):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().FEMElements,
                                     constants().NumElements: None,
                                     constants().Domain: None,
                                     constants().Steps: None,
                                     constants().Matrix: None,
                                     constants().Font: None,
                                     constants().Previous: [],
                                     constants().NumLocalNodes: None,
                                     constants().NumIntegration: None,
                                     constants().Bilinear: None,
                                     constants().Linear: None,
                                     constants().Elements: []})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IElements, self).__init__(whole_options, **kw)

    ########################################
    ###       Private Functions         ###
    ######################################## 

    def __setattr__(self, attributeName, value):
        super(IElements, self).__setattr__(attributeName, value)

        if self.checkExistance([constants().Bilinear,constants().Linear,constants().Steps,constants().Domain]):
            if (attributeName in [constants().Bilinear,constants().Linear,constants().Steps,constants().Domain]
                    and value is not None):

                try:
                    if not self.checkDefaultValues([constants().Bilinear,constants().Linear,
                                                constants().Steps,constants().Domain]):
                        self.__prepareData()

                except AttributeError:
                    e = sys.exc_info()
                    print(e)
                    raise Exception(e)

            if not self.checkDefaultValues([constants().Linear, constants().Elements, constants().Previous]):
                pos = 0
                for element in getattr(self, constants().Elements):
                    element.linear = value
                    element.extraData[constants().Previous] = getattr(self, constants().Previous)[pos:pos + 2]
                    pos += 1

    def __prepareData(self):

        try:
            size = getattr(getattr(self, constants().Domain),conventionsConstants().Space)[-1] - \
                   getattr(getattr(self, constants().Domain),conventionsConstants().Space)[0]

            self.num_elements = (int)(size / self.steps.space)
            self.matrix = lil_matrix((self.num_elements + 1, self.num_elements + 1), dtype=cfloat)
            self.font = zeros(self.num_elements + 1, dtype=cfloat)

            #        self.matrix = lil_matrix((self.num_elements+1,self.num_elements+1))
            #        self.font = zeros(self.num_elements+1)
            #        self.result = zeros(self.num_elements+1)

            for i in range(self.num_elements):
                elementDomain = [i * self.steps.space, (i * self.steps.space) + self.steps.space]
                temp_element = IElement(domain=elementDomain, \
                                        numLocalNodes=self.numLocalNodes, \
                                        numIntegration=self.numIntegration, \
                                        bilinear=self.bilinear, \
                                        linear=self.linear)

                self.elements.append(temp_element)

        except:
            e = sys.exc_info()
            print(e)
            raise Exception(e)

    ########################################
    ###       Public Functions           ###
    ########################################

    def solve(self, **arguments):

        # print("Num Elementos:",self.num_elements)

        for i in range(self.num_elements):
            startPos = i
            finalPos = i + self.numLocalNodes

            [tempMatrix, tempFont] = self.elements[i].solve(**arguments)

            #            print("Matrix:",tempMatrix,"\nFont:",tempFont,"\nfor:",i," element")

            self.matrix[startPos:finalPos, startPos:finalPos] += tempMatrix
            self.font[startPos:finalPos] += tempFont

        return [self.matrix, self.font]
