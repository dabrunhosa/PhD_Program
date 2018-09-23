import itertools

from numpy import arange

from Conventions.Classes import Names
from Conventions.Plotting.IDataPlotsParameters import IDataPlotsParameters as constants
from Plotting.IDataPlot import IDataPlot, IDataPlotError
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options


class IDataPlotsError(ValueError):
    pass


class IDataPlots(IHaveOption):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):
        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().IDataPlots,
                                     constants().ListPlots: None,
                                     constants().IterablePlots: None,
                                     constants().Length: None,
                                     constants().XElems: None,
                                     constants().Transient: False})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(IDataPlots, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###        Public Functions         ###
    ########################################

    def isEmpty(self):
        return self.length is None

    def append(self, valueToAppend):
        if isinstance(valueToAppend, IDataPlot):
            if self.listPlots is None:
                self.__dict__[constants().ListPlots] = [valueToAppend]
            else:
                self.listPlots.append(valueToAppend)
        elif isinstance(valueToAppend, IDataPlots):
            raise IDataPlotsError("The method used to add IDataPlots objects is the extend")

    def extend(self, valueToExtend):
        if isinstance(valueToExtend, IDataPlots):
            if self.listPlots is None:
                self.__dict__[constants().ListPlots] = valueToExtend.listPlots
            else:
                self.listPlots.extend(valueToExtend.listPlots)
        elif isinstance(valueToExtend, list):
            if isinstance(valueToExtend[0], IDataPlot):
                if self.listPlots is None:
                    self.__dict__[constants().ListPlots] = valueToExtend
                else:
                    self.listPlots.extend(valueToExtend)
        elif isinstance(valueToExtend, IDataPlot):
            raise IDataPlotsError("The method used to add IDataPlot objects is the append")

    ########################################
    ###        Private Functions         ###
    ########################################

    def __setattr__(self, attributeName, value):

        if attributeName == constants().ListPlots and isinstance(value, list):
            for itemA, itemB in itertools.combinations(value, 2):
                if itemA != itemB:
                    raise IDataPlotError("The iDataPlot object in the list are not compatibles")

            if self.listPlots is None:
                self.__dict__[constants().ListPlots] = value
            else:
                self.listPlots.extend(value)

            super(IDataPlots, self).__setattr__(constants().Length,
                                                value[-1].domain.space[-1] - value[-1].domain.space[0])
            super(IDataPlots, self).__setattr__(constants().XElems,
                                                arange(0, self.length + value[-1].steps.space, value[-1].steps.space))
            super(IDataPlots, self).__setattr__(constants().Transient, value[-1].transient)
        else:
            super(IDataPlots, self).__setattr__(attributeName, value)

    def __eq__(self, other):
        equal = False

        if other is None:
            equal = self.listPlots is None and self.iterablePlots is None
        elif isinstance(other, IDataPlots):
            equal = self.listPlots == other.listPlots and self.iterablePlots == other.iterablePlots

        return equal

    def __repr__(self):
        printString = ""

        if self.listPlots is None:
            printString += "The IDataPlots is empty"
        else:
            for numberPlot in range(len(self.listPlots)):
                printString += "Plot number " + str(numberPlot) + "\n"
                printString += self.listPlots[numberPlot].__repr__()
                printString += "\n\n"

        return printString

    def __iter__(self):
        self.iterablePlots = iter(self.listPlots)
        return self

    def __next__(self):  # Python 3: def __next__(self)
        return next(self.iterablePlots)
