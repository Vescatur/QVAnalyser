from Library.Algorithms.command_execution import CommandExecution
from Library.Results.result import Result


class Execution(object):

    def __init__(self, benchmark_instance):
        self.result = Result()
        self.benchmark_instance = benchmark_instance
        self.run()

    def run(self):
        raise Exception("Unimplemented method Algorithm.run_child()")

    def run_command(self, command):
        benchmark = self.benchmark_instance.benchmark_sequence.benchmark_model.benchmark
        result = CommandExecution(command, benchmark).result
        self.result.command_results.append(result)
        return result
