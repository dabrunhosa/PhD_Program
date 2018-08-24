import sys

from Conventions.Classes import Components
from Conventions.Classes import Names
from Conventions.NeuroCore.Equation.IEquation import IEquationParameters as equationConstants
from Conventions.NeuroCore.Models.GeneralModel import GeneralModelParameters as constants
from NeuroCore.Models.Base import IModel
from Utilities.DataEntry import Options


class GeneralModel(IModel):

    ########################################
    ###           Constructor            ###
    ########################################

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().GeneralModel,
                                     constants().Results: [],
                                     constants().CoeffT: None,
                                     constants().CoeffDx2: None,
                                     constants().CoeffV: None,
                                     constants().CoeffFont: None})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        # print("\n\nGeneral Model Kw Options:",kw)
        # print("General Whole Options:",whole_options.__dict__)

        super(GeneralModel, self).__init__(whole_options, **kw)

    ########################################
    ###       Private Functions          ###
    ########################################

    def __setattr__(self, attributeName, value):

        super(GeneralModel, self).__setattr__(attributeName, value)

        if (attributeName == constants().CoeffDx2 or attributeName == constants().CoeffV):
            try:
                if self.checkExistance(constants().CoeffDx2) and self.checkExistance(constants().CoeffV):

                    if self.coeff_dx2 is not None and self.coeff_v is not None:
                        if self.coeff_font is None:
                            self.coeff_font = 1

                        self.coeffs = {Components().Diffusion: self.coeff_dx2,
                                       Components().Reaction: self.coeff_v,
                                       Components().Font: self.coeff_font}

            except AttributeError:
                e = sys.exc_info()
                print(e)
                raise Exception(e)

    ########################################
    ###       Public Functions           ###
    ########################################

    def createEquations(self):

        try:
            diffusionCoeff = self.coeffs[Components().Diffusion]
            reactionCoeff = self.coeffs[Components().Reaction]
            fontCoeff = self.coeffs[Components().Font]

            if self.timeApproximation is not None:
                diffusionCoeff = self.timeApproximation.modifyCoeff(Components().Diffusion, diffusionCoeff)
                reactionCoeff = self.timeApproximation.modifyCoeff(Components().Reaction, reactionCoeff)
                fontCoeff = self.timeApproximation.modifyCoeff(Components().Font, fontCoeff)

            leftEquation = self.iApproximation.create_composed(name=equationConstants().Left)

            leftEquation.addEquation(self.iApproximation.create_diffusion(diffusionCoeff))

            leftEquation.addEquation(self.iApproximation.create_reaction(reactionCoeff))

            # print("Left Start")
            rightEquation = self.iApproximation.create_composed(name=equationConstants().Right)

            rightEquation.addEquation(self.iApproximation.create_font(fontCoeff))

            if self.timeApproximation is not None:
                rightEquation.addEquation(self.iApproximation.create_previous(self.timeApproximation.coeffT))

            # print("Right Start")

            self.equation[equationConstants().Left] = leftEquation
            self.equation[equationConstants().Right] = rightEquation

        except:
            e = sys.exc_info()
            print(e)
            raise Exception(e)
