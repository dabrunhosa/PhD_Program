# -*- coding: utf-8 -*-
'''
Created on May 29, 2014

@author: dabrunhosa
'''

# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

from Utilities.DataEntry import Options
from NeuroCore.Models.Base import IModel
from NeuroCore.Equations.Conventions import Sides,Components
import sys

class CableModel(IModel):
    
    ########################################
    ###           Constructor            ###
    ######################################## 
    
    def __init__(self,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(name = "Passive Cable Model",
                                        rm = None,
                                        cm = None,
                                        rc = None,
                                        tau = None,
                                        D = None,
                                       coeff_t = None,
                                       coeff_dx2 = None,
                                       coeff_v = None,
                                       coeff_font = None)
        
        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        #print("CableModel Kw Options:",kw)
        #print("\nCableModel Whole Options:",whole_options.__dict__)
        
        super(CableModel,self).__init__(whole_options,**kw)
        
    ######################################## 
    ###       Private Functions          ###
    ########################################
    
    def __setattr__(self,attributeName,value):
        
        super(CableModel,self).__setattr__(attributeName,value)
        
        if (attributeName == "coeff_dx2" or attributeName == "coeff_v"):
            try:
                getattr(self,"coeff_dx2")
                getattr(self,"coeff_v")
                getattr(self,"coeff_font")
                
                if not self.coeff_dx2 and not self.coeff_v:
                    if self.coeff_font is None:
                        self.coeff_font = 1
                    
                    self.coeffs = {Components().Diffusion: self.coeff_dx2,
                                   Components().Reaction: self.coeff_v,
                                   Components().Font: self.coeff_font}
                    
            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)
    
    def createEquations(self):

        diffusionCoeff = self.coeffs[Components().Diffusion]
        reactionCoeff = self.coeffs[Components().Reaction]
        fontCoeff = self.coeffs[Components().Font]

        if self.timeApproximation is not None:
            diffusionCoeff = self.timeApproximation.modifyCoeff(Components().Diffusion,diffusionCoeff)
            reactionCoeff = self.timeApproximation.modifyCoeff(Components().Reaction,reactionCoeff)
            fontCoeff = self.timeApproximation.modifyCoeff(Components().Font,fontCoeff)

        leftEquation = self.iApproximation.create_composed(name="Left Side")
        
        leftEquation.addEquation(self.iApproximation.\
                      create_diffusion(diffusionCoeff))

        leftEquation.addEquation(self.iApproximation.\
                      create_reaction(reactionCoeff))
        
        #print("Left Start")
        rightEquation = self.iApproximation.create_composed(name="Right Side")
        
        rightEquation.addEquation(self.iApproximation.\
                      create_font(fontCoeff))
        
        if self.timeApproximation is not None:
            rightEquation.addEquation(self.iApproximation.\
                          create_previous(self.timeApproximation.coeffT))
            
        #print("Right Start")
            
        self.equation[Sides().Left] = leftEquation
        self.equation[Sides().Right] = rightEquation