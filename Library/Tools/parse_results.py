from Library.storage import Storage


class ResultParser(object):

    # Storage save the benchmark as a hole at the end of the benchmark.
    # Storage save the benchmark after parsing results.

    def __init__(self, benchmark):
        self.benchmark = benchmark
        self.parse_benchmark()

    def parse_benchmark(self):
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    self.parse_result(result)

    def parse_result(self, result):
        result.measurements = []
        for algorithm in self.benchmark.algorithms:
            algorithm.pa