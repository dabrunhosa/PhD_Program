from Conventions.Classes import Names
from Conventions.Plotting.BasicPlottingColors import BasicPlottingColors
from Conventions.Plotting.PlotingParameters import PlotingParameters as constants
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options


class IDataPlotError(ValueError):
    pass


class IDataPlot(IHaveOption):

    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().IDataPlot,
                                     constants().Domain: None,
                                     constants().Steps: None,
                                     constants().Results: None,
                                     constants().Transient: False,
                                     constants().Color: BasicPlottingColors().Black})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IDataPlot, self).__init__(whole_options, **kw)

        self.transient = False if self.steps.time is None else True

    ########################################
    ###        Private Functions         ###
    ########################################

    def __repr__(self):
        return "Domain: " + str(self.domain) + "\n" + "Steps: " + str(self.steps) + \
               "\n" + "Size: " + str(len(self.results))

    def __eq__(self, other):

        equal = False

        if other is None:
            equal = self.domain is None and self.steps is None and self.results is None and self.transient == False
        elif isinstance(other, IDataPlot):
            equal = self.domain == other.domain and self.steps == other.steps and len(self.results) == len(
                other.results)

        return equal
