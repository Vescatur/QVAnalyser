class Algorithm(object):

    def __init__(self, execution_constructor, name):
        self.name = name
        self.execution_constructor = execution_constructor

    def run(self, benchmark_instance):
        result = self.execution_constructor(benchmark_instance).result
        result.algorithm = self.name
        return result

