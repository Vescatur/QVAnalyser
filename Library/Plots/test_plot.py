from Library.Results.measurements import Measurements
from Library.storage import Storage
# import matplotlib.pyplot as plt
# import numpy as np




class TestPlot(object):

    def CreatePlots(self):
        storage = Storage()
        benchmark = storage.load_latest_benchmark()

        self.print_error_information(benchmark)
        #self.print_characteristics(benchmark)
        self.characteristic_versus_characteristic(benchmark)
        #self.time_versus_characteristic(benchmark)
        #self.modest_versus_storm(benchmark)

    def print_characteristics(self, benchmark):
        different_states = 0
        different_transitions = 0
        different_branches = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if Measurements.STATES in instance.results[0].measurements and Measurements.STATES in instance.results[1].measurements:
                    if int(instance.results[0].measurements[Measurements.STATES]) != instance.results[1].measurements[Measurements.STATES]:
                        #print(sequence.benchmark_model.file_name + " " + str(sequence.parameters) + " Storm: "+ str(instance.results[0].measurements[Measurements.STATES]) + " Modest: " + str(instance.results[1].measurements[Measurements.STATES]))
                        #print(int(instance.results[0].measurements[Measurements.STATES]) - instance.results[1].measurements[Measurements.STATES])
                        different_states += 1
                if Measurements.TRANSITIONS in instance.results[0].measurements and Measurements.TRANSITIONS in instance.results[1].measurements:
                    if int(instance.results[0].measurements[Measurements.TRANSITIONS]) != instance.results[1].measurements[Measurements.TRANSITIONS]:
                        different_transitions += 1
                if Measurements.BRANCHES in instance.results[0].measurements and Measurements.BRANCHES in instance.results[1].measurements:
                    if int(instance.results[0].measurements[Measurements.BRANCHES]) != instance.results[1].measurements[Measurements.BRANCHES]:
                        different_branches += 1
        print("results")
        print(different_states)
        print(different_transitions)
        print(different_branches)
        states_is_one = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if Measurements.STATES in instance.results[1].measurements and Measurements.TRANSITIONS in instance.results[1].measurements:
                    #print(str(instance.results[1].measurements[Measurements.STATES]) + " " + str(instance.results[1].measurements[Measurements.TRANSITIONS]))
                    if instance.results[1].measurements[Measurements.STATES] == 1:
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
                    if result.algorithm_name != "modest interval iteration":
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
                        if Measurements.PROPERTY_TIME not in result.measurements:
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
        #self.characteristic_versus_characteristic_plot(benchmark, Measurements.STATES, Measurements.TRANSITIONS,True,True,"plot_states_transitions")
        #self.characteristic_versus_characteristic_plot(benchmark, Measurements.STATES, Measurements.BRANCHES,True,True,"plot_states_branches")
        #self.characteristic_versus_characteristic_plot_with_divider(benchmark, Measurements.STATES, Measurements.TRANSITIONS, Measurements.STATES,True,False,"plot_states_transition_ratio")
        #self.characteristic_versus_characteristic_plot_with_divider(benchmark, Measurements.STATES, Measurements.BRANCHES, Measurements.STATES,True,False,"plot_states_branches_ratio")
        pass
""""
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
                        if statisticX in result.measurements and statisticY in result.measurements:
                            dataX.append(result.measurements[statisticX])
                            dataY.append(result.measurements[statisticY]/result.measurements[statisticYDivider])

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
        if statistic == Measurements.TRANSITIONS:
            return "Number of transitions"
        if statistic == Measurements.BRANCHES:
            return "Number of branches"
        if statistic == Measurements.STATES:
            return "Number of states"
        if statistic == Measurements.PARSING_TIME:
            return "Time to parse file"
        if statistic == Measurements.STATE_SPACE_TIME:
            return "Time to generate state space"
        if statistic == Measurements.PROPERTY_TIME:
            return "Time to calculate result"
        if statistic == Measurements.TOOL_REPORTED_TIME:
            return "Time reported by tool"
        if statistic == Measurements.WALL_TIME:
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
        plt.savefig("./../Resources/Plots/test_plot.png") """
