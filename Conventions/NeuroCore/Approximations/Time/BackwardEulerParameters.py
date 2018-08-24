from Conventions.NeuroCore.Approximations.Time.Base import BaseParameters


class BackwardEulerParameters(BaseParameters):

    @property
    def All(self):
        return "all"

    @property
    def Previous(self):
        return "previous"