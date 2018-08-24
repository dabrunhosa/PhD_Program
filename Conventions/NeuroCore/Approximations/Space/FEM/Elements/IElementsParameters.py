from Conventions.NeuroCore.Approximations.Space.FEM.Elements.IElementParameters import IElementParameters

class IElementsParameters(IElementParameters):

    @property
    def Elements(self):
        return "elements"

    @property
    def NumElements(self):
        return "num_elements"