# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''
from abc import ABC

from Analytics.Solutions.StationaryBase import StationaryBase
from Utilities.DataEntry import Options
from cmath import cos, pi, sqrt, sinh, cosh
from Conventions.Analytics.Solutions.Validations.Stationary import StationaryParameters as constants
from Conventions.Classes import Names, Descriptions

'''
 This is the solution for the following problem:
     Problem being solved is: [0,X]
     -epsilon*d2u/dx2 + theta*u = 0
 
     BC:
         du/dx(0) = u0
         du/dx(1) = u1
 
     Solution:
         u = alpha*sinh(lambda*x) + beta*cosh(lambda*x)
         alpha = u0/lambda
         beta = u1 - u0*cosh(lambda)/lambda*sinh(lambda)
         lambda = sqrt(theta)/sqrt(epsilon)
'''


class ValidationZeroF(StationaryBase, ABC):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name:Names().ValidationZeroF,
                                  constants().DiffusionValue:1,
                                  constants().ReactionValue:1,
                                  constants().Description:Descriptions().ValidationZeroF})

        # Merge the default options and the user generated options
        .
				 defaultOptions = inDefaultOptions << defaultOptions

        super(ValidationZeroF, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions         ###
    ########################################

    def __setattr__(self, attributeName, value):
        super(ValidationZeroF, self).__setattr__(attributeName, value)

        if (attributeName == constants().DiffusionValue or attributeName == constants().ReactionValue) and value < 0:
            error_message = "The attribute: '" + attributeName + \
                            "' can't assume negative values.\
                            The value for this term has physical meaning.\
                            Negative values will not make sense physically."

            raise AttributeError(error_message)

    ########################################
    ###      Public Functions            ###
    ########################################

    def solve(self, **arguments):

        '''Using the real part of the result for lambda calculated for
        the general solution '''

        lambdaValue = sqrt(self.reactionValue) / sqrt(self.diffusionValue)

        beta = (self.BCs.inEnd.bcValue - self.BCs.inStart.bcValue *
                cosh(lambdaValue)) / (lambdaValue * sinh(lambdaValue))

        alpha = self.BCs.inStart.bcValue / lambdaValue

        '''Calculating all the points for the exact solution. 
        Obs: That would be a way without the loop if the 
        functions sinh and cosh accepted the vector form as well.'''

        for x in self.sElements:
            self.solution.append(alpha * sinh(lambdaValue * x) +
                                 beta * cosh(lambdaValue * x))

        return self.solution


'''
This is the solution for the following problem:
    Problem being solved is: [0,X]
    - epsilon*d2u/dx2 + theta*u = f
    f =  (theta + epsilon*4*(pi^2))*sin(2*pi*x)
    
    BC:
        du/dx(0) = du/dx(1) = 0
        
    Solution:
        u = cos(2*pi*x)
'''


class ValidationWithF(StationaryBase, ABC):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name:Names().ValidationWithF,
                                  constants().DiffusionValue:1,
                                  constants().ReactionValue:1,
                                  constants().Description:Descriptions().ValidationWithF})

        # Merge the default options and the user generated options
        .
				 defaultOptions = inDefaultOptions << defaultOptions

        super(ValidationWithF, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions         ###
    ######################################## 

    def __setattr__(self, attributeName, value):
        super(ValidationWithF, self).__setattr__(attributeName, value)

        if (attributeName == constants().DiffusionValue or attributeName == constants().ReactionValue) and value < 0:
            error_message = "The attribute: '" + attributeName + \
                            "' can't assume negative values.\
                            The value for this term has physical meaning.\
                            Negative values will not make sense physically."

            raise AttributeError(error_message)

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def createFont(self):

        theta = self.reactionValue
        epsilon = self.diffusionValue

        # print("Theta: ", theta)
        # print("Epsilon: ", epsilon)

        def fontFunction(x):
            return (theta + epsilon * 4 * pow(pi, 2)) * cos(2 * pi * x)

        return fontFunction

    def solve(self, **arguments):

        '''Calculating all the points for the exact solution. 
        Obs: That would be a way without the loop if the 
        functions sinh and cosh accepted the vector form as well.'''

        for x in self.sElements:
            self.solution.append(cos(2 * pi * x))

        return self.solution
