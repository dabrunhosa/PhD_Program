from Conventions.NeuroCore.Approximations.Space.FEM.Base import BaseParameters

class IApproximationParameters(BaseParameters):

    @property
    def BCs(self):
        return "BCs"

    @property
    def Coeffs(self):
        return "coeffs"

    @property
    def InMatrix(self):
        return "inMatrix"

    @property
    def InFont(self):
        return "inFont"

    @property
    def Font(self):
        return "font"