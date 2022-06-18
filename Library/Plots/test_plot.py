from Library.Results.measurements import Measurements
from Library.storage import Storage
import matplotlib.pyplot as plt
import numpy as np




class TestPlot(object):

    def CreatePlots(self):
        storage = Storage()
        benchmark = storage.load_latest_benchmark()


        self.CreateScatterPlot(benchmark,Measurements.TRANSITIONS, Measurements.BRANCHES)

        self.print_error_information(benchmark)

        # plots are saved using an increasing number

        # I want the same setup were you can specify the plots in a piece of code.

    def print_error_information(self, benchmark):
        threw_error_with_exception = 0
        threw_error = 0
        qva_error = 0
        timed_out = 0
        both = 0
        missing_results = 0
        sequence_number = 0
        for sequence in benchmark.benchmark_sequences:
            sequence_number += 1
            complete_sequence = True
            for instance in sequence.benchmark_instances:
                complete_instance = True
                for result in instance.results:
                    if result.algorithm == "modest interval iteration":
                        if result.threw_error:
                            threw_error += 1
                            #print(sequence_number)
                            #print(result.command_results[0].output_log)
                            if result.command_results[0].exception is not None:
                                threw_error_with_exception += 1
                        if result.qva_error:
                            qva_error += 1
                        if result.timed_out:
                            timed_out += 1
                        if result.threw_error and result.timed_out:
                            both += 1
                        if Measurements.PROPERTY_TIME not in result.Measurements:
                            missing_results += 1
                            if not result.timed_out:
                                print(sequence_number)
                                print(result.command_results[0].output_log)
                                print(result.command_results[0].error_log)
        print(threw_error)
        print(threw_error_with_exception)
        print(qva_error)
        print(timed_out)
        print(both)
        print(missing_results)
        # modest
        # 0
        # 0
        # 0
        # 270
        # 0
        # 935

    def CreateScatterPlot(self, benchmark, statisticX, statisticY):

        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if len(benchmark_instance.results) >= 2:
                    result = benchmark_instance.results[1]
                    if not result.threw_error:
                        if Measurements.BRANCHES in result.Measurements and Measurements.STATES in result.Measurements and Measurements.TRANSITIONS in result.Measurements:
                            # print(str(result.Measurements[statisticX]) + " "+ str(result.Measurements[statisticY]))
                            dataX.append(result.Measurements[Measurements.STATES])
                            dataY.append(result.Measurements[Measurements.BRANCHES]/result.Measurements[Measurements.TRANSITIONS])

        # s = [10, 20, 610, 11]

        # plt.show()

        plt.scatter(dataX, dataY, c="r", alpha=0.1)
        # plt.scatter(dataX, dataY,s=s , c="b", alpha=0.5)

        #plt.title(Measurements)
        plt.ylabel("Number of transitions")
        plt.xlabel("Number of choices")
        #plt.grid(True)
        #plt.yscale("log")
        plt.xscale("log")
        #plt.axis([1, 40000000 , 0,  2])
        #plt.axis([1, 1000, 1, 1000])
        plt.savefig("./../Resources/Plots/test_plot.png")

