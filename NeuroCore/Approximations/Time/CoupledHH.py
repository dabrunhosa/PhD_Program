'''
Created on Jul 14, 2014

@author: dabrunhosa
'''
from abc import ABC
from cmath import exp

from Conventions.Classes import Names
from Conventions.NeuroCore.Approximations.Time.HHParameters import HHParameters as constants
from NeuroCore.Approximations.Time.Base import IApproximation
from Utilities.DataEntry import Options


# Initial Conditions for the HH
# Coupled Equations

# m(0) = 0.1,
# n(0) = 0.4,
# h(0) = 0.1

class CoupledHHApprox(IApproximation, ABC):
    '''A class to approximate any problem using the 
    BackwardEuler Approximation an Implicit
    Method.'''

    ########################################
    ###           Constructor            ###
    ######################################## 

    def __init__(self, options=Options(), **kw):
        '''A class initializer.'''

        # Define the default options
        default_options = Options(**{constants().Name: Names().CoupledHHAproximations,
                                   constants().M: [],
                                   constants().N: [],
                                   constants().H: []})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(CoupledHHApprox, self).__init__(whole_options, **kw)

    ########################################
    ###       Private Functions          ###
    ########################################

    def __alphaN(self, V):
        return 0.01 * (10 - V) / (exp((10 - V) / 10) - 1)
        # return 0.01*(V + 55)/(1 - exp(-(V + 55)/10))

    def __alphaM(self, V):
        return 0.1 * (25 - V) / (exp((25 - V) / 10) - 1)
        # return 0.1*(V + 40)/(1 - exp(-(V + 40)/10))

    def __alphaH(self, V):
        return 0.07 * exp(-V / 20)
        # return 0.07*exp(-(V + 65)/20)

    def __reactionN(self, V):
        return self.__alphaN(V) + 0.125 * exp(-V / 80)
        # return self.__alphaN(V) + 0.125*exp(-(V + 65)/80)

    def __reactionM(self, V):
        return self.__alphaM(V) + 4 * exp(-V / 18)
        # return self.__alphaM(V) + 4*exp(-(V + 65)/18)

    def __reactionH(self, V):
        return self.__alphaH(V) + 1 / (exp((30 - V) / 10) + 1);
        # return self.__alphaH(V) + 1/(1 + exp(-(V + 35)/10))

    ########################################
    ###       Public Functions           ###
    ######################################## 

    def solve(self, **arguments):
        self.n.append((arguments[constants().N] + self.step * self.__alphaN(arguments[constants().V])) / \
                      (1 + self.step * self.__reactionN(arguments[constants().V])))

        self.m.append((arguments[constants().M] + self.step * self.__alphaM(arguments[constants().V])) / \
                      (1 + self.step * self.__reactionM(arguments[constants().V])))

        self.h.append((arguments[constants().H] + self.step * self.__alphaH(arguments[constants().V])) / \
                      (1 + self.step * self.__reactionH(arguments[constants().V])))

        return {constants().M: self.m,
                constants().N: self.n,
                constants().H: self.h}
