from Conventions.Parameters import Parameters

class IEquationParameters(Parameters):

    @property
    def Coeffs(self):
        return "coeffs"

    @property
    def Right(self):
        return "Right"

    @property
    def Left(self):
        return "Left"