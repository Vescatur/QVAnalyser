import copy

import matplotlib.pyplot as plt

from Library.setup_environment import Setup


class Plot(object):

    def __init__(self, benchmark, file_name):
        self.benchmarks = []
        self.current_benchmark = None
        self.set_current_benchmark(benchmark)
        self.log_x = False
        self.log_y = False
        self.file_name = file_name
        self.data_x = []
        self.data_y = []
        self.axis = None

    def set_current_benchmark(self,benchmark):
        self.benchmarks.append(benchmark)
        self.current_benchmark = benchmark

    def new_current_benchmark(self):
        self.set_current_benchmark(copy.deepcopy(self.current_benchmark))

    def filter_results(self, filter_func):
        self.new_current_benchmark()
        for benchmark_sequence in self.current_benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                new_results = []
                for result in benchmark_instance.results:
                    if filter_func(result):
                        new_results.append(result)
                benchmark_instance.results = new_results

    def filter_instances(self, filter_func):
        self.new_current_benchmark()
        for benchmark_sequence in self.current_benchmark.benchmark_sequences:
            new_instances = []
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if filter_func(benchmark_instance):
                    new_instances.append(benchmark_instance)
            benchmark_sequence.benchmark_instances = new_instances

    def filter_sequences(self, filter_func):
        self.new_current_benchmark()
        new_sequences = []
        for benchmark_sequence in self.current_benchmark.benchmark_sequences:
            if filter_func(benchmark_sequence):
                new_sequences.append(benchmark_sequence)
        self.current_benchmark.benchmark_sequences = new_sequences

    def results_to_data(self):
        raise Exception("Unimplemented method Plot.results_to_data()")

    def generate_x_label(self):
        raise Exception("Unimplemented method Plot.generate_x_label()")

    def generate_y_label(self):
        raise Exception("Unimplemented method Plot.generate_y_label()")

    def save_plot(self):
        self.results_to_data()
        if len(self.data_x) == 0:
            self.data_x = [1]
            self.data_y = [1]

        plt.scatter(self.data_x, self.data_y, c="b", alpha=0.5)
        plt.title(str(len(self.data_x)) + " results")
        plt.grid(True)

        if self.axis is not None:
            plt.axis(self.axis)

        if self.log_x:
            plt.xscale("log")
        if self.log_y:
            plt.yscale("log")

        plt.xlabel(self.generate_x_label())
        plt.ylabel(self.generate_y_label())

        print("finished plot " + self.file_name)
        print(Setup().plots_path+self.file_name+".png")
        plt.savefig(Setup().plots_path+self.file_name+".png")
        plt.close()
