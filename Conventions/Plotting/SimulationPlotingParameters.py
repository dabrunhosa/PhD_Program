from Conventions.Plotting.PlotingParameters import PlotingParameters

class SimulationPlotingParameters(PlotingParameters):

    @property
    def Marker(self):
        return "marker"

    @property
    def Linestyles(self):
        return "linestyles"