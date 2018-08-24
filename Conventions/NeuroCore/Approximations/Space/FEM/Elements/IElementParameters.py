from Conventions.Parameters import Parameters

class IElementParameters(Parameters):

    @property
    def NumLocalNodes(self):
        return "numLocalNodes"

    @property
    def NumIntegration(self):
        return "numIntegration"

    @property
    def Matrix(self):
        return "matrix"

    @property
    def Font(self):
        return "font"

    @property
    def CoupledApprox(self):
        return "coupledApprox"

    @property
    def Bilinear(self):
        return "bilinear"

    @property
    def Linear(self):
        return "linear"

    @property
    def ExtraData(self):
        return "extraData"

    @property
    def Previous(self):
        return "previous"