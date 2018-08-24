from Conventions.Parameters import Parameters


class BaseParameters(Parameters):

    @property
    def Disturbance(self):
        return "disturbance"

    @property
    def CoeffT(self):
        return "coeffT"

    @property
    def Font(self):
        return "Font"

    @property
    def Reaction(self):
        return "Reaction"

    @property
    def Step(self):
        return "step"