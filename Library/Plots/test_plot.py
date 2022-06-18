from Library.Results.statistics import Statistics
from Library.storage import Storage
import matplotlib.pyplot as plt
import numpy as np




class TestPlot(object):

    def CreatePlots(self):
        storage = Storage()
        benchmark = storage.load_latest_benchmark()

        # self.print_error_information(benchmark)
        self.print_characteristics(benchmark)
        self.characteristic_versus_characteristic(benchmark)
        self.time_versus_characteristic(benchmark)
        self.modest_versus_storm(benchmark)

    def print_characteristics(self, benchmark):
        different_states = 0
        different_transitions = 0
        different_branches = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if Statistics.STATES in instance.results[0].statistics and Statistics.STATES in instance.results[1].statistics:
                    if int(instance.results[0].statistics[Statistics.STATES]) != instance.results[1].statistics[Statistics.STATES]:
                        #print(sequence.benchmark_model.file_name + " " + str(sequence.parameters) + " Storm: "+ str(instance.results[0].statistics[Statistics.STATES]) + " Modest: " + str(instance.results[1].statistics[Statistics.STATES]))
                        #print(int(instance.results[0].statistics[Statistics.STATES]) - instance.results[1].statistics[Statistics.STATES])
                        different_states += 1
                if Statistics.TRANSITIONS in instance.results[0].statistics and Statistics.TRANSITIONS in instance.results[1].statistics:
                    if int(instance.results[0].statistics[Statistics.TRANSITIONS]) != instance.results[1].statistics[Statistics.TRANSITIONS]:
                        different_transitions += 1
                if Statistics.BRANCHES in instance.results[0].statistics and Statistics.BRANCHES in instance.results[1].statistics:
                    if int(instance.results[0].statistics[Statistics.BRANCHES]) != instance.results[1].statistics[Statistics.BRANCHES]:
                        different_branches += 1
        print("results")
        print(different_states)
        print(different_transitions)
        print(different_branches)
        states_is_one = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if Statistics.STATES in instance.results[1].statistics and Statistics.TRANSITIONS in instance.results[1].statistics:
                    #print(str(instance.results[1].statistics[Statistics.STATES]) + " " + str(instance.results[1].statistics[Statistics.TRANSITIONS]))
                    if instance.results[1].statistics[Statistics.STATES] == 1:
                        print(sequence.benchmark_model.file_name + " " + str(sequence.parameters) + " " + sequence.property_name)
                        print(instance.results[0].statistics[Statistics.STATES])
                        states_is_one += 1
        print(states_is_one)

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
                    #if result.algorithm == "modest interval iteration":
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
                    if Statistics.PROPERTY_TIME not in result.statistics:
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

    def characteristic_versus_characteristic(self, benchmark):
        self.characteristic_versus_characteristic_plot(benchmark, Statistics.STATES, Statistics.TRANSITIONS,True,True,"plot_states_transitions")
        self.characteristic_versus_characteristic_plot(benchmark, Statistics.STATES, Statistics.BRANCHES,True,True,"plot_states_branches")
        self.characteristic_versus_characteristic_plot_with_divider(benchmark, Statistics.STATES, Statistics.TRANSITIONS, Statistics.STATES,True,False,"plot_states_transition_ratio")
        self.characteristic_versus_characteristic_plot_with_divider(benchmark, Statistics.STATES, Statistics.BRANCHES, Statistics.STATES,True,False,"plot_states_branches_ratio")

    def characteristic_versus_characteristic_plot(self, benchmark, statisticX, statisticY,logX,logY,name):
        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if len(benchmark_instance.results) >= 2:
                    result = benchmark_instance.results[1]
                    if not result.threw_error:
                        if statisticX in result.statistics and statisticY in result.statistics:
                            dataX.append(result.statistics[statisticX])
                            dataY.append(result.statistics[statisticY])

        plt.grid(True)
        plt.scatter(dataX, dataY, c="b", alpha=0.5)
        if logX:
            plt.xscale("log")
        if logY:
            plt.yscale("log")

        plt.ylabel(self.statistic_to_label(statisticY))
        plt.xlabel(self.statistic_to_label(statisticX))
        plt.savefig("./../Resources/Plots/"+name+".png")
        plt.close()


    def characteristic_versus_characteristic_plot_with_divider(self, benchmark, statisticX, statisticY, statisticYDivider,logX,logY,name):
        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if len(benchmark_instance.results) >= 2:
                    result = benchmark_instance.results[1]
                    if not result.threw_error:
                        if statisticX in result.statistics and statisticY in result.statistics:
                            dataX.append(result.statistics[statisticX])
                            dataY.append(result.statistics[statisticY]/result.statistics[statisticYDivider])

        plt.grid(True)
        plt.scatter(dataX, dataY, c="b", alpha=0.5)
        if logX:
            plt.xscale("log")
        if logY:
            plt.yscale("log")

        plt.ylabel(self.statistic_to_label(statisticY))
        plt.xlabel(self.statistic_to_label(statisticX)+" divided by "+self.statistic_to_label(statisticYDivider))
        plt.savefig("./../Resources/Plots/"+name+".png")
        plt.close()

    def statistic_to_label(self, statistic):
        if statistic == Statistics.TRANSITIONS:
            return "Number of transitions"
        if statistic == Statistics.BRANCHES:
            return "Number of branches"
        if statistic == Statistics.STATES:
            return "Number of states"
        if statistic == Statistics.PARSING_TIME:
            return "Time to parse file"
        if statistic == Statistics.STATE_SPACE_TIME:
            return "Time to generate state space"
        if statistic == Statistics.PROPERTY_TIME:
            return "Time to calculate result"
        if statistic == Statistics.TOOL_REPORTED_TIME:
            return "Time reported by tool"
        if statistic == Statistics.WALL_TIME:
            return "Wall time"

    def time_versus_characteristic(self, benchmark):
        # Should be a line per sequence
        pass

    def modest_versus_storm(self, benchmark):
        pass



    def create_scatter_plot(self, benchmark, statisticX, statisticY):

        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if len(benchmark_instance.results) >= 2:
                    result = benchmark_instance.results[1]
                    if not result.threw_error:
                        if Statistics.BRANCHES in result.statistics and Statistics.STATES in result.statistics and Statistics.TRANSITIONS in result.statistics:
                            # print(str(result.statistics[statisticX]) + " "+ str(result.statistics[statisticY]))
                            dataX.append(result.statistics[Statistics.STATES])
                            dataY.append(result.statistics[Statistics.BRANCHES]/result.statistics[Statistics.TRANSITIONS])

        plt.scatter(dataX, dataY, c="r", alpha=0.1)
        # plt.scatter(dataX, dataY,s=s , c="b", alpha=0.5)

        #plt.title(statistics)
        plt.ylabel("Number of transitions")
        plt.xlabel("Number of choices")
        #plt.grid(True)
        #plt.yscale("log")
        plt.xscale("log")
        #plt.axis([1, 40000000 , 0,  2])
        plt.savefig("./../Resources/Plots/test_plot.png")
