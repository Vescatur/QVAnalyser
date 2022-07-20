from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel


class BenchmarkSequence(object):

    def __init__(self, benchmark_model: BenchmarkModel, property_name: str, property_type: str, parameters):
        self.benchmark_model = benchmark_model
        self.property_name = property_name
        self.property_type = property_type
        self.parameters = parameters
        self.benchmark_instances = []
        self.index = len(self.benchmark_model.benchmark.benchmark_sequences)
        self.benchmark_model.benchmark.benchmark_sequences.append(self)

    def add_instance(self, benchmark_instance: BenchmarkInstance):
        self.benchmark_instances.append(benchmark_instance)