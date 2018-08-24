from Conventions.Parameters import Parameters


class StationaryBaseParameters(Parameters):

    @property
    def Description(self):
        return "description"

    @property
    def SElements(self):
        return "sElements"

    @property
    def BCs(self):
        return "BCs"

    @property
    def Solution(self):
        return "solution"

    @property
    def DiffusionValue(self):
        return "diffusionValue"

    @property
    def ReactionValue(self):
        return "reactionValue"




