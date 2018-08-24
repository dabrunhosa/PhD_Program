from Conventions.NeuroCore.Equation.Components.Base import BaseParameters

class FEMBaseParameters(BaseParameters):

    @property
    def WeightFunction(self):
        return "weightFunction"

    @property
    def ReferenceElement(self):
        return "referenceElement"

    @property
    def Line(self):
        return "line"

    @property
    def Column(self):
        return "column"

    @property
    def Font(self):
        return "font"

    @property
    def Previous(self):
        return "previous"