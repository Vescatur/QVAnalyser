
class Benchmark(object):

    def __init__(self):
        self.executions = []

    def run(self):
        for execution in self.executions:
            execution.run()
            print(execution.command_executions[0].output)