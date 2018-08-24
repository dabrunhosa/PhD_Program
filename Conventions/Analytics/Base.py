from Conventions.Parameters import Parameters


class BaseParameters(Parameters):

    @property
    def Description(self):
        return "description"

    @property
    def Solution(self):
        return "solution"
