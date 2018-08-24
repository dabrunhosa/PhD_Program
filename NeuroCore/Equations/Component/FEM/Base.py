'''
Created on May 29, 2014

@author: dabrunhosa
'''
from abc import ABC

from Conventions.Classes import Names
from Conventions.NeuroCore.Equation.Components.FEM.Base import FEMBaseParameters as constants
from NeuroCore.Equations.Component.Base import IComponent
from NeuroCore.Equations.Conventions import femTransformation
from Utilities.DataEntry import Options


class IFEM(IComponent, ABC):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        '''Class initializer. Use it's Base Class initializer
        and adds the weight function to be used. '''

        # Define the default options
        default_options = Options(**{constants().Name: Names().FEMComponent,
                                   constants().WeightFunction: None,
                                   constants().ReferenceElement: True,
                                   constants().Line: 0,
                                   constants().Column: 0})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IFEM, self).__init__(whole_options, **kw)

    ########################################
    ###       Private Functions          ###
    ########################################             

    def __call__(self, **arguments):
        '''Add supports for the call method. The difference
        is that it requires the line and column arguments to work.
        This is used to identify the kind of weight function
        that is going to be used, in order words to identify
        the element that is being processed.'''

        self.line = arguments[constants().Line]
        self.column = arguments[constants().Column]

        function = self.build_function

        if self.referenceElement:
            function = femTransformation(function, arguments[constants().Domain])

        return function
