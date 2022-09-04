from Library.Output.plot_filters import result_not_threw_error, result_not_timeout, result_is_from_algorithm, \
    only_dtmc_and_mdp
from Library.Output.results_printer import ResultsPrinter
from Library.Output.scatter_plot import ScatterPlot
from Library.Output.tool_plot import ToolPlot
from Library.Results.measurements import Measurements
from Library.setup_environment import Setup
from Library.storage import Storage
import matplotlib.pyplot as plt
import numpy as np

from Specific.Output.percentage_total_plot import PercentageTotalPlot
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Storm.storm_tool import StormTool


class PlotSprint6(object):

    def CreatePlots(self):
        storage = Storage()
        benchmark = storage.load_latest_benchmark()
        #self.time_versus_characteristic(benchmark)
        self.percentage_state_property_to_total(benchmark)

    def percentage_state_property_to_total(self, benchmark):
        PercentageTotalPlot(benchmark, True, True, "Percentage total both").save_plot()
        PercentageTotalPlot(benchmark, True, False, "Percentage total state space time").save_plot()
        PercentageTotalPlot(benchmark, False, True, "Percentage total property time").save_plot()

    def time_versus_characteristic(self, benchmark):
        #times = [Measurements.WALL_TIME]
        times = [Measurements.PARSING_TIME,Measurements.STATE_SPACE_TIME,Measurements.PROPERTY_TIME]
        for algorithm in benchmark.algorithms:
            counter = 1
            for time in times:
                self.scatter_plot(benchmark, Measurements.STATES, time,None,True,True,str(counter)+"state_characteristic",algorithm)
                counter += 1


    def scatter_plot(self, benchmark, measurement_x, measurement_y, measurement_divider_y, log_x, log_y, name, algorithm):
        plot = ScatterPlot(benchmark,measurement_x,measurement_y,name)
        plot.measurement_divider_y = measurement_divider_y
        plot.log_x = log_x
        plot.log_y = log_y
        if algorithm is not None:
            plot.filter_results(result_is_from_algorithm(algorithm.name))
            plot.file_name = plot.file_name + "_" + algorithm.name
        plot.save_plot()