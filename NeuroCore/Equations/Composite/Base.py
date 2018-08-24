# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:24:46 2017

@author: daniel
"""

from abc import abstractmethod

from Conventions.Classes import Names
from Conventions.NeuroCore.Equation.Composite.Base import BaseParameters as constants
from NeuroCore.Equations.IEquation import IEquation
from Utilities.DataEntry import Options


class IComposite(IEquation):
    '''A class to create a term based on the basic terms.
    This class can be used in runtime or for the developer 
    to define a new term.'''

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        '''The initializer for the class receives a list
        of terms that the composed term is going to
        be based in.
        
        It's used like: 
        Composed_Term(diffusion = Galerking_Diffusion,...)'''

        # Define the default options
        default_options = Options(**{constants().Name: Names().Composite,
                                   constants().Domain: None,
                                   constants().Equation: {}})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IComposite, self).__init__(whole_options, **kw)

        ########################################

    ###       Abstract Functions         ###
    ######################################## 

    @abstractmethod
    def __call__(self, **arguments):
        raise NotImplementedError

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def addEquation(self, equation):
        try:
            self.equation[equation.name] = equation
        except KeyError:
            error_message = "Only iEquation types can be added to the:\
             composed equation"

            raise TypeError(error_message)

    def getEquation(self, nameOfEquation):
        """Try to get the type of term passed. 
        If it does not exist an error is raised.
        """

        try:
            return self.equation[nameOfEquation]
        except KeyError:
            error_message = "There is no equation with the name:" \
                            + nameOfEquation + " verify with you wrote the wrong name" \
                                               "when entering the equation."

            raise KeyError(error_message)

    def setEquation(self, nameOfEquation, modEquation):
        """Try to set the modified term for the type 
        of term. If it does not exist an error is raised."""

        try:
            self.equation[nameOfEquation] = modEquation
        except KeyError:
            error_message = "There is no term with the name:" \
                            + nameOfEquation + " verify with you wrote the wrong name" \
                                               "when entering the term. If you did first try to" \
                                               "add the term by calling add_term method."

            raise KeyError(error_message)
