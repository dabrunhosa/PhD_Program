# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:24:50 2017

@author: daniel
"""

'''
===================
Saving an animation
===================

This example showcases the same animations as `basic_example.py`, but instead
of displaying the animation to the user, it writes to files using a
MovieWriter instance.
'''

import itertools
import os

# -*- noplot -*-
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt

matplotlib.use("Agg")

from Plotting.IPlot import IPlot
from Utilities.DataEntry import Options
from Conventions.Plotting.SimulationPlotingParameters import SimulationPlotingParameters as constants
from Conventions.Classes import Names


class Simulation(IPlot):

    ########################################
    ###       Constructor                ###
    ######################################## 

    def __init__(self, options=Options(), **kw):

        # Define the default options
        default_options = Options(**{constants().Name: Names().SimuPlots,
                                     constants().Marker: itertools.cycle((',', '+', '.', 'o', '*', 'v', '>', '<')),
                                     constants().Linestyles: itertools.cycle(('--', '-', '-.', ':'))})

        # Merge the default options and the user generated options
        whole_options = default_options << options

        super(Simulation, self).__init__(whole_options, **kw)

    ########################################
    ###        Public Functions          ###
    ######################################## 

    def show(self):
        raise NotImplementedError

    def save(self, pathLocation):
        if self.transient:
            return self.__transientSave(pathLocation)
        else:
            return self.__stationarySave(pathLocation)

    def __stationarySave(self, pathLocation):

        plt.figure()
        plt.subplot(111)
        for iDataPlot in self.plots:
            # print("Plotting iDataPlot: ",iDataPlot)
            # print("Elems: ", self.xElems)
            plt.plot(self.xElems, iDataPlot.results, linestyle=next(self.linestyles), color=iDataPlot.color,
                     label=iDataPlot.name, marker=next(self.marker))

        plt.legend()
        plt.savefig(pathLocation)
        print("Image saved successfully. Image saved in:" + os.path.dirname(os.path.abspath(pathLocation)) + "\\"
              + pathLocation)

    def __transientSave(self, pathLocation):

        infoLog = {}

        figure = plt.figure()
        ax = plt.axes(xlim=self.xlim, ylim=self.ylim)
        time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
        lines = []
        timeStep = 0

        for iDataPlot in self.plots:
            lobj = ax.plot([], [], lw=2, color=iDataPlot.color, linestyle=next(self.linestyles),
                           marker=next(self.marker), label=iDataPlot.name)[0]
            lines.append(lobj)
            timeStep = iDataPlot.steps.time

        def init():
            for line in lines:
                line.set_data([], [])
            return lines

        for timePos in range(len(self.tElements)):
            # print("Time Pos:",timePos)
            infoLog[timePos] = []
            for iDataPlot in self.plots:
                floatResult = [i.real for i in iDataPlot.results[timePos]]
                infoLog[timePos].append(floatResult)

        # print(infoLog)

        def update_line(timePos, results, lines):

            # print("Time Position:",timePos)
            # print("\n\n Lines:",lines)

            # for result,time in zip(results.values(),results):
            #     print("\n\nResult at time:", time, "Result:",result)

            for lnum, line in enumerate(lines):
                # print("Lines:", lines)
                line.set_data(self.xElems, results[timePos][lnum])
                line.set_label(line.get_label())

            timePos = timePos * timeStep
            # timePos = timePos*0.1

            time_text.set_text('t = %.1f' % timePos)

            ax.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                      ncol=2, borderaxespad=0)

            title = "Transient Example"
            ax.set_title(title)
            return tuple(lines) + (time_text,)

        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=10, metadata=dict(artist='NeuroSimu'), bitrate=18000)

        plt.xlabel('x')
        plt.xlabel('u(x)')
        plt.title(self.plots.name)
        line_ani = animation.FuncAnimation(figure, update_line, len(self.tElements), init_func=init,
                                           fargs=(infoLog, lines), interval=5000, blit=True)

        line_ani.save(pathLocation, writer=writer)
        print("Video saved successfully. Video saved in:" + os.path.dirname(os.path.abspath(pathLocation)) + "\\"
              + pathLocation)
