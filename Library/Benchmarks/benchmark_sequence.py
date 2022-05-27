
class BenchmarkSequence(object):

    def __init__(self,benchmark_model, property, parameters):
        self.benchmark_model = benchmark_model
        self.property = property
        self.parameters = parameters
        self.benchmark_instances = []
        self.benchmark_model.benchmark.benchmark_sequences.append(self)

    def add_instance(self,benchmark_instance):
        self.benchmark_instances.append(benchmark_instance)