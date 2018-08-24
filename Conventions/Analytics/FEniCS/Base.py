from Conventions.Analytics.Base import BaseParameters


class FEniCSBaseParameters(BaseParameters):

    @property
    def SpatialSteps(self):
        return "spatialSteps"

    @property
    def Mesh(self):
        return "mesh"

    @property
    def BCs(self):
        return "BCs"
