from Library.Benchmarks.benchmark import Benchmark
from Library.Results.measurements import Measurements


class OverviewMeasurementPrinter(object):

    def print_overview_measurements(self,benchmark, algorithms,instance_filter, measurements):
        for measurement in measurements:
            self.print_overview_for_one_measurement(benchmark, algorithms, instance_filter, measurement)

    def print_overview_for_one_measurement(self, benchmark, algorithms, instance_filter, measurement):
        print()
        print(measurement)
        self.print_top_row(algorithms)
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if instance_filter(instance):
                    self.print_row(algorithms,instance,measurement)

    def print_top_row(self, algorithms):
        line = "\t"
        for alg in algorithms:
            line += alg.name + "\t"
        print(line)

    def print_row(self, algorithms, instance, measurement):
        line = ""
        line += instance.benchmark_sequence.benchmark_model.name + "\t"
        for alg in algorithms:
            line += self.print_cell(alg, instance, measurement)
        print(line.replace(".",","))

    def print_cell(self, alg, instance, measurement):
        for result in instance.results:
            if result.algorithm_name == alg.name:
                if result.threw_error:
                    return "error\t"
                elif result.timed_out:
                    return "timed out\t"
                elif result.not_supported:
                    return "not supported\t"
                elif measurement in result.measurements:
                    return str(result.measurements[measurement]) + "\t"
                else:
                    return "\t"
        return "\t"



