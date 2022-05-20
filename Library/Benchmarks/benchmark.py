from Library.setup_environment import Setup
from Library.storage import Storage


class Benchmark(object):

    def __init__(self):
        self.execution_sequences = []
        self.setup = Setup()
        self.setup.setup_resource_folders()
        self.storage = Storage()
        self.tools = []
        self.benchmark_path = Setup().benchmark_models_path

    def run(self):
        self.setup.setup_tools(self)
        for execution_sequence in self.execution_sequences:
            for execution in execution_sequence.executions:
                execution.run()
                self.storage.save_execution(execution, execution_sequence)
                print(execution.command_executions[0].output)
