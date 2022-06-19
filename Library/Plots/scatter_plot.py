import matplotlib.pyplot as plt

from Library.Results.measurements import Measurements
from Library.setup_environment import Setup


class ScatterPlot(object):

    def __init__(self, benchmark,measurement_x, measurement_y, file_name):
        self.benchmark = benchmark
        self.measurement_x = measurement_x
        self.measurement_y = measurement_y
        self.measurement_divider_y = None
        self.log_x = False
        self.log_y = False
        self.file_name = file_name
        self.results = []
        self.removed_results = []
        self.data_x = []
        self.data_y = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                for result in benchmark_instance.results:
                    self.results.append(result)

    def filter(self,filter_func):
        new_results = []
        removed_results = []
        for result in self.results:
            if filter_func(result):
                new_results.append(result)
            else:
                removed_results.append(result)
        self.results = new_results
        self.removed_results.append(removed_results)

    def results_to_data(self):
        for result in self.results:
            self.data_x.append(result.measurements[self.measurement_x])
            if self.measurement_divider_y is None:
                self.data_y.append(result.measurements[self.measurement_y])
            else:
                self.data_y.append(result.measurements[self.measurement_y]/result.measurements[self.measurement_divider_y])

    def save_plot(self):
        self.filter(self.result_contains_measurements)
        self.results_to_data()
        plt.grid(True)
        plt.scatter(self.data_x, self.data_y, c="b", alpha=0.5)
        if self.log_x:
            plt.xscale("log")
        if self.log_y:
            plt.yscale("log")

        plt.xlabel(self.measurement_x.to_label_text())

        if self.measurement_divider_y is None:
            plt.ylabel(self.measurement_y.to_label_text())
        else:
            plt.ylabel(self.measurement_y.to_label_text() + " divided by " + self.measurement_divider_y.to_label_text())

        plt.savefig(Setup().plots_path+self.file_name+".png")
        plt.close()

    def result_contains_measurements(self, result):
        if self.measurement_x not in result.measurements:
            return False
        if self.measurement_y not in result.measurements:
            return False
        if self.measurement_divider_y is not None:
            if self.measurement_divider_y not in result.measurements:
                return False
        return True
