from Conventions.Plotting.PlotingParameters import PlotingParameters

class IPlotingParameters(PlotingParameters):

    @property
    def Plots(self):
        return "plots"

    @property
    def Xlim(self):
        return "xlim"

    @property
    def Ylim(self):
        return "ylim"