from Conventions.Plotting.IPlotingParameters import IPlotingParameters

class SimulationPlotingParameters(IPlotingParameters):

    @property
    def Marker(self):
        return "marker"

    @property
    def Linestyles(self):
        return "linestyles"