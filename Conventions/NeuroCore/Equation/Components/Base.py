from Conventions.NeuroCore.Equation.IEquation import IEquationParameters

class BaseParameters(IEquationParameters):

    @property
    def Coeff(self):
        return "coeff"