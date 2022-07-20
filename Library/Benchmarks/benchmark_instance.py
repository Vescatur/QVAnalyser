from Library.Benchmarks.benchmark_sequence import BenchmarkSequence


class BenchmarkInstance(object):

    def __init__(self, benchmark_sequence: BenchmarkSequence, parameters):
        self.benchmark_sequence = benchmark_sequence
        self.parameters = parameters
        self.all_parameters = self.parameters | benchmark_sequence.parameters
        self.results = []
        self.index = len(benchmark_sequence.benchmark_instances)
        benchmark_sequence.add_instance(self)