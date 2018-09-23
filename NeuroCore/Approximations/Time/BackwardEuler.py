'''
Created on Jul 14, 2014

@author: dabrunhosa
'''

from NeuroCore.Approximations.Time.Base import IApproximation
from Conventions.Classes import Components
from Conventions.NeuroCore.Approximations.Time.BackwardEulerParameters import BackwardEulerParameters as constants
from Conventions.Classes import Names
from Utilities.DataEntry import Options

class BackwardEuler(IApproximation):
    '''A class to approximate any problem using the 
    BackwardEuler Approximation an Implicit
    Method.'''
    
    ########################################
    ###           Constructor            ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        '''A class initializer.'''
        
         # Define the default options
        inDefaultOptions =Options(**{constants().Name:Names().BackwardEuler})
        
        
        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions
        
        super(BackwardEuler,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
        
    ########################################
    ###       Private Functions          ###
    ######################################## 
    
    def __setattr__(self,attributeName,value):
        super(BackwardEuler,self).__setattr__(attributeName,value) 
        
        if attributeName == constants().CoeffT and value is not None:
            self.disturbance[Components().Reaction] = value
            
        if attributeName == constants().Step and value is not None:
            self.disturbance[constants().All] = value
            self.disturbance[Components().Diffusion] = value
            self.disturbance[Components().Font] = value
        
    ########################################
    ###       Public Functions           ###
    ######################################## 

    def modifyCoeff(self,coeffName,value):

        modCoeff = value*self.disturbance[coeffName]

        if coeffName is Components().Reaction:
            modCoeff = self.disturbance[coeffName] + value*self.disturbance[constants().All]

        return modCoeff

    def solve(self,**arguments):
        return (arguments[constants().Previous] + self.step*self.Font)/(1 + self.step*self.Reaction)