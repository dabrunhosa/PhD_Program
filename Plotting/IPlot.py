# -*- coding: utf-8 -*-
'''
Created on September 6, 2017

@author: dabrunhosa
'''

from abc import abstractmethod
from Utilities.BaseOption import IHaveOption
from Utilities.DataEntry import Options
from Plotting.IDataPlot import IDataPlot, IDataPlotError
from Plotting.IDataPlots import IDataPlots
from numpy import arange
import itertools
from Conventions.Plotting.IPlotingParameters import IPlotingParameters as constants
from Conventions.Classes import Names


class IPlot(IHaveOption):

    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self, options=Options(), defaultOptions = Options(), **kw):

        # Define the default options
        inDefaultOptions =Options(**{constants().Name: Names().IPlot,
                                     constants().Plots: IDataPlots(),
                                     constants().Xlim: (-1.5, 1.5),
                                     constants().Ylim: (-1.5, 1.5),
                                     constants().Length: None,
                                     constants().XElems: None,
                                     constants().TElems: None,
                                     constants().Transient: False})

        # Merge the default options and the user generated options

        defaultOptions = inDefaultOptions << defaultOptions

        super(IPlot, self).__init__(options=options, defaultOptions = defaultOptions, **kw)

    ########################################
    ###       Private Functions          ###
    ######################################## 

    def __setattr__(self, attributeName, value):

        if attributeName == constants().Plots:
            if isinstance(value, IDataPlot):
                if self.plots is None:
                    self.__dict__[constants().Plots] = [value]
                else:
                    self.plots.append(value)

                print(self.plots)

                super(IPlot, self).__setattr__(constants().Length, value.domain.space[-1] - value.domain.space[0])
                super(IPlot, self).__setattr__(constants().XElems,
                                               arange(0, self.length + value.steps.space, value.steps.space))
                super(IPlot, self).__setattr__(constants().Transient, value.transient)

                if self.transient:
                    super(IPlot, self).__setattr__(constants().TElems, arange(0, value.domain.time[-1]
                                                                              + value.steps.time, value.steps.times))

            elif isinstance(value, IDataPlots):
                if value.isEmpty():
                    self.__dict__[constants().Plots] = value
                else:
                    self.plots.extend(value)

                super(IPlot, self).__setattr__(constants().Length, value.length)
                super(IPlot, self).__setattr__(constants().XElems, value.xElems)
                super(IPlot, self).__setattr__(constants().Transient, value.transient)

                if self.transient:
                    super(IPlot, self).__setattr__(constants().TElems, arange(0, value.domain.time[-1]
                                                                              + value.steps.time, value.steps.times))
            elif isinstance(value, list):
                for itemA, itemB in itertools.combinations(value, 2):
                    if itemA != itemB:
                        raise IDataPlotError("The iDataPlots are not compatibles")
                self.plots.extend(value)

                super(IPlot, self).__setattr__(constants().Length,
                                               value[-1].domain.space[-1] - value[-1].domain.space[0])
                super(IPlot, self).__setattr__(constants().XElems,
                                               arange(0, self.length + value[-1].steps.space, value[-1].steps.space))
                super(IPlot, self).__setattr__(constants().Transient, value[-1].transient)

                if self.transient:
                    super(IPlot, self).__setattr__(constants().TElems, arange(0, value[-1].domain.time[-1]
                                                                              + value[-1].steps.time,
                                                                              value[-1].steps.time))
            else:
                raise IDataPlotError("Not supported type for iDataPlots")
        else:
            super(IPlot, self).__setattr__(attributeName, value)

    ########################################
    ###       Abstract Functions         ###
    ########################################

    @abstractmethod
    def show(self):
        raise NotImplementedError

    @abstractmethod
    def save(self, pathLocation=None):
        raise NotImplementedError
