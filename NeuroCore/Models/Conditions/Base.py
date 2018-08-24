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
    
    def __init__(self,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(name = "Boundary Condition")
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(ICondition,self).__init__(whole_options,**kw)  