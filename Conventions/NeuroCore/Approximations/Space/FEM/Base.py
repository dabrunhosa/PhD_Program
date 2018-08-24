from Conventions.Parameters import Parameters

class BaseParameters(Parameters):

    @property
    def ReferenceElement(self):
        return "referenceElement"

    @property
    def Modifiers(self):
        return "modifiers"

    @property
    def WeightFunction(self):
        return "weightFunction"

    @property
    def NumIntegration(self):
        return "numIntegration"

    @property
    def IElements(self):
        return "iElements"

    @property
    def CurrentTime(self):
        return "currentTime"

    @property
    def Equation(self):
        return "equation"