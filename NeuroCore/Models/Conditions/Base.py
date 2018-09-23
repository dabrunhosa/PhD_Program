# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:50:32 2017

@author: Daniel Abrunhosa
"""

from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options

class ICondition(IHaveOption):
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name = "Boundary Condition")
        
        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions
        
        super(ICondition,self).__init__(options=options, defaultOptions = defaultOptions, **kw)