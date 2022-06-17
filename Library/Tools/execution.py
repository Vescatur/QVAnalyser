from Library.Tools.command_execution import CommandExecution
from Library.Results.measurements import Measurements


class Execution(object):

    def __init__(self, instance, result):
        self.result = result
        self.benchmark_instance = instance
        self.result.measurements[Measurements.WALL_TIME] = 0
        self.run()

    def run(self):
        raise Exception("Unimplemented method Algorithm.run()")

    def run_command(self, command):
        benchmark = self.benchmark_instance.benchmark_sequence.benchmark_model.benchmark
        command_result = CommandExecution(command, benchmark).result
        self.result.command_results.append(command_result)
        if command_result.timed_out:
            self.result.timed_out = True
        if command_result.exception is not None:
            self.result.threw_error = True
        self.result.measurements[Measurements.WALL_TIME] = self.result.measurements[Measurements.WALL_TIME] + command_result.wall_time
        return command_result
