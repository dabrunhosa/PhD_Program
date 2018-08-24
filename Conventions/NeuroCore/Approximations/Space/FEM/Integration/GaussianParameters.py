from Conventions.Parameters import Parameters

class GaussianParameters(Parameters):

    @property
    def Degree(self):
        return "degree"

    @property
    def IntPoints(self):
        return "intPoints"