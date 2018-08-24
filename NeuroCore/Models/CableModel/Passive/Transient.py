# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:12:21 2017

@author: daniel
"""

from Utilities.DataEntry import Options
from NeuroCore.Models.Base import IModel
from NeuroCore.Equations.Conventions import Sides,Components
from numpy import ones
import sys

class CableModel(IModel):
    
    ########################################
    ###           Constructor            ###
    ######################################## 
    
    def __init__(self,options=Options(), **kw):

        #Other Example would be:
        # Ek = -77,
        # ENa = 50,
        # ELeaky = -54.4,
        
        # Define the default options
        default_options = Options(name = "Cable Model",
                                  results = [],
                                  gk = 36, 
                                  gNa = 120,
                                  gLeaky = 0.3,
                                  Ek = -12,
                                  ENa = 115,
                                  ELeaky = 10.6,
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

    # noinspection PyArgumentList
    def __setattr__(self,attributeName,value):
        
        super(CableModel,self).__setattr__(attributeName,value)
        
        if (attributeName == "coeff_dx2" or attributeName == "coeff_v"):
            try:
                getattr(self,"coeff_dx2")
                getattr(self,"coeff_font")
                
                if self.coeff_dx2 is not None and self.initialCondition is not None:
                    if self.coeff_font is None:
                        self.coeff_font = 1

                    self.currentM = self.initialM*ones(len(self.initialCondition))
                    self.currentN = self.initialN*ones(len(self.initialCondition))
                    self.currentH = self.initialH*ones(len(self.initialCondition))
                    
                    self.coeffs = {Components().Diffusion: self.coeff_dx2,
                                   Components().Reaction: self.coeffReaction(),
                                   Components().Font: self.coeffFont(m=self.currentM,n=self.currentN,h=self.currentH)}
                    
            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)

    def calculateK(self):
        self.currentK = self.gk*pow(self.currentN,4)

    def calculateNa(self):
        self.currentNa = self.gNa*pow(self.currentM,3)*self.currentH

    ######################################## 
    ###       Public Functions           ###
    ######################################## 

    def coeffReaction(self,x):
        return self.currentK + self.currentNa + self.gLeaky

    def coeffFont(self,**elements):
        return self.currentK*(-self.Ek) + self.currentNa*(-self.ENa) + \
                self.gLeaky*(-self.ELeaky)

    def solve(self,**arguments):
       
        [self.currentM,self.currentN,self.currentH] = coupledApproximation.solve(m=self.currentM,n=self.currentN,h=self.currentH,V=self.results[-1])

        self.currentTime = arguments["currentTime"]
        self.calculateK()
        self.calculateNa()
        results.append(self.iApproximation.solve(**arguments))
    
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

        discreteComponent = self.iApproximation.create_discrete(self.iApproximation.\
                      create_reaction(reactionCoeff))

        discreteComponent.discreteElements

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