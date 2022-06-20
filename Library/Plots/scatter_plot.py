import matplotlib.pyplot as plt

from Library.Plots.plot import Plot
from Library.Plots.plot_filters import result_contains_measurement, result_not_threw_error, result_not_timeout
from Library.Results.measurements import Measurements
from Library.setup_environment import Setup


class ScatterPlot(Plot):

    def __init__(self, benchmark, measurement_x, measurement_y, file_name):
        super().__init__(benchmark, file_name)
        self.measurement_x = measurement_x
        self.measurement_y = measurement_y
        self.measurement_divider_y = None
        self.filter_results(result_not_threw_error())
        self.filter_results(result_not_timeout())
        self.use_highest_characteristic()

    def use_highest_characteristic(self):
        characteristics = []
        if self.measurement_x.is_characteristic():
            characteristics.append(self.measurement_x)
        if self.measurement_y.is_characteristic():
            characteristics.append(self.measurement_y)
        if self.measurement_divider_y is not None:
            if self.measurement_divider_y.is_characteristic():
                characteristics.append(self.measurement_divider_y)

        for benchmark_sequence in self.current_benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                for characteristic in characteristics:
                    highest_value = -1
                    for result in benchmark_instance.results:
                        if characteristic in result.measurements:
                            if result.measurements[characteristic] > highest_value:
                                highest_value = result.measurements[characteristic]
                    if highest_value != -1:
                        for result in benchmark_instance.results:
                            result.measurements[characteristic] = highest_value

    def results_to_data(self):
        unique_result_per_instance = True
        if not self.measurement_x.is_characteristic():
            unique_result_per_instance = False
        if not self.measurement_y.is_characteristic():
            unique_result_per_instance = False
        if self.measurement_divider_y is not None and not self.measurement_divider_y.is_characteristic():
            unique_result_per_instance = False

        for benchmark_sequence in self.current_benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                if unique_result_per_instance:
                    if len(benchmark_instance.results) >= 1:
                        self.result_to_data(benchmark_instance.results[0])
                else:
                    for result in benchmark_instance.results:
                        self.result_to_data(result)

    def result_to_data(self,result):
        self.data_x.append(result.measurements[self.measurement_x])
        if self.measurement_divider_y is None:
            self.data_y.append(result.measurements[self.measurement_y])
        else:
            self.data_y.append(result.measurements[self.measurement_y]/result.measurements[self.measurement_divider_y])

    def generate_x_label(self):
        return self.measurement_x.to_label_text()

    def generate_y_label(self):
        if self.measurement_divider_y is None:
            return self.measurement_y.to_label_text()
        else:
            return self.measurement_y.to_label_text() + " divided by " + self.measurement_divider_y.to_label_text()

    def save_plot(self):
        self.filter_results(result_contains_measurement(self.measurement_x))
        self.filter_results(result_contains_measurement(self.measurement_y))
        if self.measurement_divider_y is not None:
            self.filter_results(result_contains_measurement(self.measurement_divider_y))
        super().save_plot()

