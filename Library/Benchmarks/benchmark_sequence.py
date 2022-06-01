
class BenchmarkSequence(object):

    def __init__(self, benchmark_model, property_name, parameters):
        self.benchmark_model = benchmark_model
        self.property_name = property_name
        self.parameters = parameters
        self.benchmark_instances = []
        self.index = len(self.benchmark_model.benchmark.benchmark_sequences)
        self.benchmark_model.benchmark.benchmark_sequences.append(self)

    def add_instance(self, benchmark_instance):
        self.benchmark_instances.append(benchmark_instance)