# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''
from abc import ABC

from Analytics.Solutions.TransientBase import TransientBase
from Analytics.Solutions.Validations.YDomain.Base import YDomain
from Utilities.DataEntry import Options
'''
Problem being solved is: [0,1]U[1,2]U[1,3] X [0,1]
    This is an example used by Jemmy in a Y Domain.
    Although it does not look like it, all the 
    segments have the same length.    
    BC:
    du/dx(0) = du/dx(3) = du/dx(2) = 0
    du/dx(1) - du/dx(1) - du/dx(1) = 0 - derivative continuity
    u(1) = u(1) = u(1) - variable continuity

    Initial Conditions:
    u(0,x) = cos(pi*x)
'''


class YDomainTransientBase(TransientBase, YDomain, ABC):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(name="Y Domain for Transient Solution",
                                  numSegments=None,bifurcationPoints=None,
                                  sElementsE=None,sElementsLw=None,sElementsUp=None,
                                  domainDef=["domainE","domainLw","domainUp"],
                                  sElementDef=["sElementsE","sElementsLw","sElementsUp"],
                                  description="This is a base solution for the Y Domain Problem)")

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(YDomainTransientBase, self).__init__(whole_options, **kw)