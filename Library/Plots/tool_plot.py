import matplotlib.pyplot as plt

from Library.Benchmarks.benchmark import Benchmark
from Library.Plots.plot import Plot
from Library.Plots.plot_filters import result_contains_measurement, result_not_threw_error, result_not_timeout, \
    get_result_with_algorithm, instance_contains_algorithms
from Library.Results.measurements import Measurements
from Library.Tools.algorithm import Algorithm


class ToolPlot(Plot):

    def __init__(self, benchmark: Benchmark, measurement: Measurements, algorithm_x: Algorithm, algorithm_y: Algorithm, file_name: str):
        super().__init__(benchmark, file_name)
        self.measurement = measurement
        self.algorithm_x = algorithm_x
        self.algorithm_y = algorithm_y
        self.filter_results(result_not_threw_error())
        self.filter_results(result_not_timeout())
        self.axis = [0.01, 60, 0.01, 60]

    def results_to_data(self):
        for benchmark_sequence in self.current_benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                result_x = get_result_with_algorithm(benchmark_instance, self.algorithm_x)
                result_y = get_result_with_algorithm(benchmark_instance, self.algorithm_y)
                self.data_x.append(result_x.measurements[self.measurement])
                self.data_y.append(result_y.measurements[self.measurement])

    def generate_x_label(self):
        return self.algorithm_x.name + " " + self.measurement.to_label_text()

    def generate_y_label(self):
        return self.algorithm_y.name

    def save_plot(self):
        self.filter_results(result_contains_measurement(self.measurement))
        self.filter_instances(instance_contains_algorithms(self.algorithm_x, self.algorithm_y))

        super().save_plot()


