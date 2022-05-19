from Library.storage import Storage


class Benchmark(object):

    def __init__(self):
        self.execution_sequences = []
        self.storage = Storage()

    def run(self):
        for execution_sequence in self.execution_sequences:
            for execution in execution_sequence.executions:
                execution.run()
                self.storage.save_execution(execution, execution_sequence)
                print(execution.command_executions[0].output)
