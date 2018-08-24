from Conventions.Parameters import Parameters

class PlotingParameters(Parameters):

    @property
    def Color(self):
        return "color"

    @property
    def ListPlots(self):
        return "listPlots"

    @property
    def IterablePlots(self):
        return "iterablePlots"

    @property
    def Length(self):
        return "length"

    @property
    def XElems(self):
        return "xElems"

    @property
    def TElems(self):
        return "tElements"