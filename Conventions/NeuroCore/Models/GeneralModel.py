from Conventions.NeuroCore.Models.Base import BaseParameters


class GeneralModelParameters(BaseParameters):

    @property
    def CoeffT(self):
        return "coeff_t"

    @property
    def CoeffDx2(self):
        return "coeff_dx2"

    @property
    def CoeffV(self):
        return "coeff_v"

    @property
    def CoeffFont(self):
        return "coeff_font"
