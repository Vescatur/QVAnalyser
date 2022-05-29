class Algorithm(object):

    def __init__(self, execution_constructor, name):
        self.name = name
        self.execution_constructor = execution_constructor

    def run(self, benchmark_instance):
        return self.execution_constructor(benchmark_instance).result

