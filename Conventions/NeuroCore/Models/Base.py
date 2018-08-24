from Conventions.Parameters import Parameters

class BaseParameters(Parameters):

    @property
    def CurrentTime(self):
        return "currentTime"

    @property
    def InitialCondition(self):
        return "initialCondition"

    @property
    def Coeffs(self):
        return "coeffs"

    @property
    def Font(self):
        return "font"

    @property
    def BCs(self):
        return "BCs"

    @property
    def IApproximation(self):
        return "iApproximation"

    @property
    def TimeApproximation(self):
        return "timeApproximation"

    @property
    def Equation(self):
        return "equation"

    @property
    def CoeffT(self):
        return "coeff_t"