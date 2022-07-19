from Library.Plots.plot_filters import result_not_threw_error, result_not_timeout, result_is_from_algorithm, \
    only_dtmc_and_mdp
from Library.Plots.results_printer import ResultsPrinter
from Library.Plots.scatter_plot import ScatterPlot
from Library.Plots.tool_plot import ToolPlot
from Library.Results.measurements import Measurements
from Library.setup_environment import Setup
from Library.storage import Storage
import matplotlib.pyplot as plt
import numpy as np

from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Storm.storm_tool import StormTool


class PlotSprint3(object):

    def CreatePlots(self):
        storage = Storage()
        benchmark = storage.load_latest_benchmark()
        results_printer = ResultsPrinter()
        # results_printer.print_error_information(benchmark)
        # results_printer.print_characteristics(benchmark)
        self.modest_versus_storm(benchmark)
        # self.characteristic_versus_characteristic(benchmark)
        #self.time_versus_characteristic(benchmark)

    def characteristic_versus_characteristic(self, benchmark):
        self.scatter_plot(benchmark, Measurements.STATES, Measurements.TRANSITIONS, Measurements.STATES, True, True, "plot_states_transition_ratio",None)
        self.scatter_plot(benchmark, Measurements.STATES, Measurements.BRANCHES, Measurements.STATES, True, True, "plot_states_branches_ratio",None)
        self.scatter_plot(benchmark, Measurements.TRANSITIONS, Measurements.BRANCHES, Measurements.TRANSITIONS, True, True, "plot_branches_transition_ratio",None)

    def time_versus_characteristic(self, benchmark):
        times = [Measurements.PARSING_TIME,Measurements.STATE_SPACE_TIME,Measurements.PROPERTY_TIME,Measurements.WALL_TIME,Measurements.TOOL_REPORTED_TIME]
        for algorithm in benchmark.algorithms:
            counter = 0
            for time in times:
                self.scatter_plot(benchmark, Measurements.STATES, time,None,True,True,str(counter)+"state_characteristic",algorithm)
                counter += 1

            self.scatter_plot(benchmark, Measurements.WALL_TIME, Measurements.TOOL_REPORTED_TIME,None,True,True, str(counter) + "check_for_tool_reported_time",algorithm)
            counter += 1

            for time in times:
                self.scatter_plot(benchmark, Measurements.STATES, time, Measurements.WALL_TIME,True,False,str(counter)+"percentage_of_wall_time_against_states",algorithm)
                counter += 1

            for time in times:
                self.scatter_plot(benchmark, Measurements.WALL_TIME, time,Measurements.WALL_TIME,True,False,str(counter)+"percentage_of_wall_time_against_wall_time",algorithm)
                counter += 1

    def modest_versus_storm(self, benchmark):
        times = [Measurements.STATE_SPACE_TIME,Measurements.PROPERTY_TIME,Measurements.WALL_TIME]
        counter = 100
        for time in times:
            self.tool_plot(benchmark,time,ModestTool().interval_iteration,StormTool().interval_iteration,True,True,str(counter)+"storm_modest")
            counter += 1

        for time in times:
            self.tool_plot_dtmc_mdp(benchmark,time,ModestTool().interval_iteration,StormTool().interval_iteration,True,True,str(counter)+"storm_modest_dtmc_mdp")
            counter += 1

    def tool_plot(self, benchmark, measurement, algorithm_x, algorithm_y, log_x, log_y, name):
        plot = ToolPlot(benchmark,measurement,algorithm_x,algorithm_y,name)
        plot.log_x = log_x
        plot.log_y = log_y
        plot.save_plot()

    def tool_plot_dtmc_mdp(self, benchmark, measurement, algorithm_x, algorithm_y, log_x, log_y, name):
        plot = ToolPlot(benchmark,measurement,algorithm_x,algorithm_y,name)
        plot.filter_sequences(only_dtmc_and_mdp())
        plot.log_x = log_x
        plot.log_y = log_y
        plot.save_plot()


    def scatter_plot(self, benchmark, measurement_x, measurement_y, measurement_divider_y, log_x, log_y, name, algorithm):
        plot = ScatterPlot(benchmark,measurement_x,measurement_y,name)
        plot.measurement_divider_y = measurement_divider_y
        plot.log_x = log_x
        plot.log_y = log_y
        if algorithm is not None:
            plot.filter_results(result_is_from_algorithm(algorithm.name))
            plot.file_name = plot.file_name + "_" + algorithm.name
        plot.save_plot()