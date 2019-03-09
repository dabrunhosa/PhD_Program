# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:31:16 2017

@author: Daniel Abrunhosa
"""

from Conventions.Classes import Names
from Conventions.NeuroCore.Models.Conventions import ConventionsParameters as constants
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options


class Domains(IHaveOption):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions=Options(), **kw):

        # Define the default options
        inDefaultOptions = Options(**{constants().Name: Names().Domain,
                                      constants().Space: None,
                                      constants().Time: None})

        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions

        super(Domains, self).__init__(options=options, defaultOptions=defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, Domains):
            return self.space == other.space and self.time == other.time

    def __repr__(self):
        return "Space: " + str(self.space) + "\n Time :" + str(self.time)

    def __setattr__(self, attributeName, value):

        if (attributeName == "space" or attributeName == "time") and value is not None:

            if type(value) != list:
                error_message = "The " + attributeName + " domain has to be a list"
                raise AttributeError(error_message)

        super(Domains, self).__setattr__(attributeName, value)


class Steps(IHaveOption):

    ########################################
    ###          Constructor             ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions=Options(), **kw):
        # Define the default options
        inDefaultOptions = Options(**{constants().Name: Names().Steps,
                                      constants().Space: None,
                                      constants().Time: None})

        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions

        super(Steps, self).__init__(options=options, defaultOptions=defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __eq__(self, other):
        if isinstance(other, Steps):
            return self.space == other.space and self.time == other.time

    def __repr__(self):
        return "Space: " + str(self.space) + "\n Time :" + str(self.time)
