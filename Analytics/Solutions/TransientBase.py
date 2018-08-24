# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''
from abc import ABC

from Analytics.Solutions.ISolution import ISolution
from Utilities.DataEntry import Options


class TransientBase(ISolution, ABC):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(name="Transient Base Class",
                                  description="A Base Class for Transient Solutions",
                                  sElements=None,
                                  BCs=None,
                                  solution=[])

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(TransientBase, self).__init__(whole_options, **kw)

    ########################################
    ###       Public Functions           ###
    ########################################

    def createFont(self):

        def fontFunction(x,t):
            return 0.0

        return fontFunction