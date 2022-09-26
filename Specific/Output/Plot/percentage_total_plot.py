from Library.Benchmarks.benchmark import Benchmark
from Specific.Output.Plot.plot import Plot
from Library.Output.plot_filters import result_contains_measurement, result_not_threw_error, result_not_timeout
from Library.Results.measurements import Measurements


class PercentageTotalPlot(Plot):

    def __init__(self, benchmark: Benchmark, state_space_time, property_time, file_name: str):
        super().__init__(benchmark, file_name)
        self.state_space_time = state_space_time
        self.property_time = property_time
        self.measurement_x = Measurements.WALL_TIME
        self.measurement_y1 = Measurements.STATE_SPACE_TIME
        self.measurement_y2 = Measurements.PROPERTY_TIME
        self.measurement_divider_y = Measurements.WALL_TIME
        self.filter_results(result_not_threw_error())
        self.filter_results(result_not_timeout())

    def results_to_data(self):
        for benchmark_sequence in self.current_benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                for result in benchmark_instance.results:
                    self.result_to_data(result)

    def result_to_data(self,result):
        self.data_x.append(result.measurements[self.measurement_x])
        measurement1 = 0
        if self.measurement_y1 in result.measurements:
            measurement1 = result.measurements[self.measurement_y1]
        measurement2 = 0
        if self.measurement_y2 in result.measurements:
            measurement2 = result.measurements[self.measurement_y2]
        total = 0
        if self.state_space_time:
            total += measurement1
        if self.property_time:
            total += measurement2
        divider = result.measurements[self.measurement_divider_y]
        self.data_y.append(total/divider)

    def generate_x_label(self) -> str:
        return "Total time"

    def generate_y_label(self) -> str:
        return "Percentage building and iterating time attribute to the total"

    def save_plot(self):
        self.filter_results(result_contains_measurement(self.measurement_x))
        self.filter_results(result_contains_measurement(self.measurement_y1))
        self.filter_results(result_contains_measurement(self.measurement_y2))
        self.filter_results(result_contains_measurement(self.measurement_divider_y))
        super().save_plot()

