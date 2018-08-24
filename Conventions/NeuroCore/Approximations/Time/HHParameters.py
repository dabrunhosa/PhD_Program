from Conventions.NeuroCore.Approximations.Time.Base import BaseParameters


class HHParameters(BaseParameters):

    @property
    def N(self):
        return "n"

    @property
    def M(self):
        return "m"

    @property
    def H(self):
        return "h"

    @property
    def V(self):
        return "v"