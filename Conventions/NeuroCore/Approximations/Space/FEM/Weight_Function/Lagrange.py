from Conventions.NeuroCore.Approximations.Space.FEM.Elements.IElementParameters import IElementParameters


class LagrangeParameters(IElementParameters):

    @property
    def DiffWeightFunction(self):
        return "diffWeightFunction"

    @property
    def WeightFunction(self):
        return "weightFunction"

    @property
    def Degree(self):
        return "degree"
