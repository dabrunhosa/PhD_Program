"""@author: Daniel Abrunhosa
"""

from Conventions.NeuroCore.Models.Conditions.Base import BaseParameters


class CurrentParameters(BaseParameters):

    @property
    def Diameter(self):
        return "diameter"

    @property
    def ResistanceL(self):
        return "resistanceL"

    @property
    def Current(self):
        return "current"
