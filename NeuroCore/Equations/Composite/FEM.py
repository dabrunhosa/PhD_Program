# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:55:37 2017

@author: Daniel Abrunhosa
"""
from abc import ABC

from Conventions.Classes import Components
from Conventions.NeuroCore.Equation.Composite.FEM import FEMParameters as constants
from NeuroCore.Equations.Composite.Base import IComposite
from Utilities.DataEntry import Options


class IFEM(IComposite, ABC):
    '''A class to create a term based on the basic terms.
    This class can be used in runtime or for the developer 
    to define a new term.'''

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        '''The initializer for the class receives a list
        of terms that the composed term is going to
        be based in.
        
        It's used like: 
        Composed_Term(diffusion = Galerking_Diffusion,...)'''

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: "FEM Composite",
                                   constants().Line: 0.0,
                                   constants().Column: 0.0,
                                   constants().Previous: None,
                                   constants().Domain: None})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(IFEM, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

        ########################################

    ###       Private Functions          ###
    ######################################## 

    def __repr__(self):
        """Handle the print statement and shows a nicer
        string then the original."""
        result = self.name + "formed by: "

        for iEquation in self.equation.values():
            result += " " + iEquation.name

        return result

    def __call__(self, **arguments):
        '''Add supports for the call method. The difference
        is that it requires some arguments to work.'''
        self.line = arguments[constants().Line]
        self.column = arguments[constants().Column]
        self.domain = arguments[constants().Domain]

        if Components().Time in arguments:
            self.previous = arguments[Components().Time]

        return self.build_function

    def build_function(self, x):
        '''Method used by the call method to be able to
        create the composed term. It requires the position
        x and returns the total value to the user.'''

        finalValue = 0.0

        for iEquation in self.equation.values():

            if iEquation.name == Components().Time:
                iEquation.previous = self.previous

            value = iEquation(line=self.line, column=self.column, domain=self.domain)(x)
            finalValue += value

        return finalValue
