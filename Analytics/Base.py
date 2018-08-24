# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''
from abc import ABC

from Conventions.Analytics.Base import BaseParameters as constants
from Conventions.Classes import Names, Descriptions
from Utilities.BaseOption import ISolvable
from Utilities.DataEntry import Options


class IAnalysis(ISolvable, ABC):

    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Name: Names().IAnalysis,
                                   constants().Description: Descriptions().IAnalysis,
                                   constants().Solution: None,
                                   constants().Domain: None,
                                   constants().Steps: None})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IAnalysis, self).__init__(whole_options, **kw)
