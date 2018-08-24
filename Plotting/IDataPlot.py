
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options
import itertools
from numpy import arange
from Conventions.Plotting.PlotingParameters import PlotingParameters as constants
from Conventions.Plotting.BasicPlottingColors import BasicPlottingColors
from Conventions.Classes import Names

class IDataPlotError(ValueError):
    pass

class IDataPlotsError(ValueError):
    pass

class IDataPlot(IHaveOption):
    
    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self,options=Options(), **kw):
        
        # Define the default options
        default_options = Options(**{constants().Name:Names().IDataPlot,
                                  constants().Domain:None,
                                  constants().Steps:None,
                                  constants().Results:None,
                                  constants().Transient:False,
                                  constants().Color: BasicPlottingColors().Black})

        # Merge the default options and the user generated options
        whole_options = default_options << options
        
        super(IDataPlot,self).__init__(whole_options,**kw)

        self.transient = False if self.steps.time is None else True

    ########################################
    ###        Private Functions         ###
    ########################################

    def __repr__(self):
        return "Domain: " + str(self.domain) + "\n" + "Steps: " + str(self.steps) +\
               "\n" + "Size: " + str(len(self.results))

    def __eq__(self, other):

        equal = False

        if other is None:
            equal = self.domain is None and self.steps is None and self.results is None and self.transient == False
        elif isinstance(other, IDataPlot):
            equal = self.domain == other.domain and self.steps == other.steps and len(self.results) == len(other.results)

        return equal


class IDataPlots(IHaveOption):

    ########################################
    ###       Constructor                ###
    ########################################

    def __init__(self, options=Options(), **kw):
        # Define the default options
        default_options = Options(**{constants().Name:Names().IDataPlots,
                                   constants().ListPlots:None,
                                   constants().IterablePlots:None,
                                   constants().Length:None,
                                   constants().XElems:None,
                                   constants().Transient:False})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(IDataPlots, self).__init__(whole_options, **kw)

    ########################################
    ###        Public Functions         ###
    ########################################

    def append(self, valueToAppend):
        if isinstance(valueToAppend,IDataPlot):
            if self.listPlots is None:
                self.__dict__[constants().ListPlots] = [valueToAppend]
            else:
                self.listPlots.append(valueToAppend)
        elif isinstance(valueToAppend,IDataPlots):
            raise IDataPlotsError("The method used to add IDataPlots objects is the extend")

    def extend(self, valueToExtend):
        if isinstance(valueToExtend,IDataPlots):
            if self.listPlots is None:
                self.__dict__[constants().ListPlots] = valueToExtend.listPlots
            else:
                self.listPlots.extend(valueToExtend.listPlots)
        elif isinstance(valueToExtend,list):
            if isinstance(valueToExtend[0],IDataPlot):
                if self.listPlots is None:
                    self.__dict__[constants().ListPlots] = valueToExtend
                else:
                    self.listPlots.extend(valueToExtend)
        elif isinstance(valueToExtend,IDataPlot):
            raise IDataPlotsError("The method used to add IDataPlot objects is the append")


    ########################################
    ###        Private Functions         ###
    ########################################

    def __setattr__(self, attributeName, value):

        if attributeName == constants().ListPlots and isinstance(value,list):
            for itemA, itemB in itertools.combinations(value, 2):
                if itemA != itemB:
                    raise IDataPlotError("The iDataPlot object in the list are not compatibles")

            if self.listPlots is None:
                self.__dict__[constants().ListPlots] = value
            else:
                self.listPlots.extend(value)

            super(IDataPlots, self).__setattr__(constants().Length, value[-1].domain.space[-1] - value[-1].domain.space[0])
            super(IDataPlots, self).__setattr__(constants().XElems,
                                           arange(0, self.length + value[-1].steps.space, value[-1].steps.space))
            super(IDataPlots, self).__setattr__(constants().Transient, value[-1].transient)
        else:
            super(IDataPlots, self).__setattr__(attributeName, value)

    def __eq__(self, other):
        equal = False

        if other is None:
            equal = self.listPlots is None and self.iterablePlots is None
        elif isinstance(other,IDataPlots):
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

    def __next__(self): # Python 3: def __next__(self)
        return next(self.iterablePlots)


