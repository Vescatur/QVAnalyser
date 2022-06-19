from Library.Plots.results_printer import ResultsPrinter
from Library.Plots.scatter_plot import ScatterPlot
from Library.Results.measurements import Measurements
from Library.setup_environment import Setup
from Library.storage import Storage
import matplotlib.pyplot as plt
import numpy as np


class PlotSprint3(object):

    def CreatePlots(self):
        storage = Storage()
        benchmark = storage.load_latest_benchmark()
        results_printer = ResultsPrinter()
        #results_printer.print_error_information(benchmark)
        # results_printer.print_characteristics(benchmark)
        self.characteristic_versus_characteristic(benchmark)
        # self.time_versus_characteristic(benchmark)
        # self.modest_versus_storm(benchmark)



    def characteristic_versus_characteristic(self, benchmark):
        #self.characteristic_versus_characteristic_plot(benchmark, Measurements.STATES, Measurements.TRANSITIONS,True,True,"plot_states_transitions")
        #self.characteristic_versus_characteristic_plot(benchmark, Measurements.STATES, Measurements.BRANCHES,True,True,"plot_states_branches")
        self.characteristic_versus_characteristic_plot_with_divider2(benchmark, Measurements.STATES, Measurements.TRANSITIONS, Measurements.STATES,True,True,"plot_states_transition_ratio")
        self.characteristic_versus_characteristic_plot_with_divider2(benchmark, Measurements.STATES, Measurements.BRANCHES, Measurements.STATES,True,True,"plot_states_branches_ratio")
        pass


    def characteristic_versus_characteristic_plot(self, benchmark, statisticX, statisticY,logX,logY,name):



        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if len(benchmark_instance.results) >= 2:
                    result = benchmark_instance.results[1]
                    if not result.threw_error:
                        if statisticX in result.measurements and statisticY in result.measurements:
                            dataX.append(result.measurements[statisticX])
                            dataY.append(result.measurements[statisticY])

        plt.grid(True)
        plt.scatter(dataX, dataY, c="b", alpha=0.5)
        if logX:
            plt.xscale("log")
        if logY:
            plt.yscale("log")

        plt.ylabel(self.measurement_to_label(statisticY))
        plt.xlabel(self.measurement_to_label(statisticX))
        plt.savefig("./../Resources/Plots/"+name+".png")
        plt.close()


    def characteristic_versus_characteristic_plot_with_divider2(self, benchmark, measurement_x, measurement_y, measurement_divider_y, log_x, log_y, name):
        plot = ScatterPlot(benchmark,measurement_x,measurement_y,name)
        plot.measurement_divider_y = measurement_divider_y
        plot.log_x = log_x
        plot.log_y = log_y
        plot.save_plot()

    def characteristic_versus_characteristic_plot_with_divider(self, benchmark, statisticX, statisticY, statisticYDivider,logX,logY,name):
        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if len(benchmark_instance.results) >= 2:
                    result = benchmark_instance.results[1]
                    if not result.threw_error:
                        if statisticX in result.measurements and statisticY in result.measurements:
                            dataX.append(result.measurements[statisticX])
                            dataY.append(result.measurements[statisticY]/result.measurements[statisticYDivider])

        labelY = self.measurement_to_label(statisticY) + " divided by " + self.measurement_to_label(statisticYDivider)
        labelX = self.measurement_to_label(statisticX)
        self.create_plot(dataX, dataY, logX, logY, name, labelX, labelY)


    def create_plot(self, dataX, dataY, logX, logY, name, labelX, labelY):
        plt.grid(True)
        plt.scatter(dataX, dataY, c="b", alpha=0.5)
        if logX:
            plt.xscale("log")
        if logY:
            plt.yscale("log")
        plt.ylabel(labelX)
        plt.xlabel(labelY)
        plt.savefig(Setup().plots_path + name + ".png")
        plt.close()



    def time_versus_characteristic(self, benchmark):
        # Should be a line per sequence
        pass

    def modest_versus_storm(self, benchmark):
        pass


"""
    def create_scatter_plot(self, benchmark, statisticX, statisticY):

        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if len(benchmark_instance.results) >= 2:
                    result = benchmark_instance.results[1]
                    if not result.threw_error:
                        if Measurements.BRANCHES in result.measurements and Measurements.STATES in result.measurements and Measurements.TRANSITIONS in result.measurements:
                            # print(str(result.measurements[statisticX]) + " "+ str(result.measurements[statisticY]))
                            dataX.append(result.measurements[Measurements.STATES])
                            dataY.append(result.measurements[Measurements.BRANCHES]/result.measurements[Measurements.TRANSITIONS])

        plt.scatter(dataX, dataY, c="r", alpha=0.1)
        # plt.scatter(dataX, dataY,s=s , c="b", alpha=0.5)

        #plt.title(measurements)
        plt.ylabel("Number of transitions")
        plt.xlabel("Number of choices")
        #plt.grid(True)
        #plt.yscale("log")
        plt.xscale("log")
        #plt.axis([1, 40000000 , 0,  2])
        plt.savefig("./../Resources/Plots/test_plot.png")
"""