# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:51:20 2017

@author: Daniel Abrunhosa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:50:56 2017

@author: daniel
"""
# To save data pickle or json very code tools for that

from abc import abstractmethod

from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Space.FEM.IApproximation import IApproximationParameters as constants
from Utilities.BaseOption import ISolvable
from Utilities.DataEntry import Options


class IApproximation(ISolvable):

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Name: Names().Approximation,
                                     constants().BCs: None,
                                     constants().CurrentTime: None,
                                     constants().Coeffs: None,
                                     constants().Domain: None,
                                     constants().Steps: None,
                                     constants().InMatrix: None,
                                     constants().InFont: None,
                                     constants().Font: None,
                                     constants().Results: [],
                                     constants().Equation: None})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IApproximation, self).__init__(whole_options, **kw)

    ########################################
    ###       Abstract Functions         ###
    ######################################## 

    # @abstractmethod
    # def create_discrete(self,component):
    #    raise NotImplementedError

    @abstractmethod
    def create_composed(self):
        raise NotImplementedError

    @abstractmethod
    def create_diffusion(self, coeff=1.0):
        raise NotImplementedError

    @abstractmethod
    def create_reaction(self, coeff=1.0):
        raise NotImplementedError

    @abstractmethod
    def create_font(self):
        raise NotImplementedError

    @abstractmethod
    def create_previous(self, coeff=1.0):
        raise NotImplementedError
