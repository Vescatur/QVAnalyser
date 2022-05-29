from Library.setup_environment import Setup
from Library.storage import Storage


class Benchmark(object):

    def __init__(self):
        self.benchmark_models = []
        self.benchmark_sequences = []
        self.algorithms = []
        self.time_limit = 600

        self.setup = Setup()
        self.setup.setup_resource_folders()
        self.storage = Storage()
        self.tools = []
        self.benchmark_path = Setup().benchmark_models_path

    def run(self):
        self.setup.setup_tools(self)
        for sequence in self.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for algorithm in self.algorithms:
                    self.run_algorithm(algorithm, instance, sequence)

    def run_algorithm(self, algorithm, instance, sequence):
        #try:
            print("Run: {} on {}".format(algorithm.name, sequence.benchmark_model.name))
            result = algorithm.run(instance)
            # self.storage.save_execution(execution, execution_sequence)
            # print(execution.command_executions[0].output)
            print(result.command_results[0].output_log)
            print(result.command_results[0].error_log)
            print(result.command_results[0].exception)
        #except Exception:
        #    print("Something went wrong with execution sequence {}".format(sequence.benchmark_model.name))
