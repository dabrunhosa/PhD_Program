from Conventions.Analytics.Base import BaseParameters


class BaseParameters(BaseParameters):

    @property
    def SElements(self):
        return "sElements"

    @property
    def BCs(self):
        return "BCs"
