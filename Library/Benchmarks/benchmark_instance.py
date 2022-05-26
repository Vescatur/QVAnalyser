
class BenchmarkInstance(object):

    def __init__(self,benchmark_sequence, parameters):
        self.benchmark_sequence = benchmark_sequence
        self.parameters = parameters
        benchmark_sequence.add_instance(self)