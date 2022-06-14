import traceback

from Library.Results.result import Result
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
        number_of_sequences = 0
        number_of_instances = 0
        number_of_algorithms = 0
        for sequence in self.benchmark_sequences:
            number_of_sequences += 1
            for _ in sequence.benchmark_instances:
                number_of_instances += 1

        for _ in self.algorithms:
            number_of_algorithms += 1
        print("Found "+str(number_of_sequences)+" sequence(s), " +
              str(number_of_instances)+" instance(s) and " +
              str(number_of_algorithms)+" algorithm(s). This requires " +
              str(number_of_instances * number_of_algorithms)+" executions.")

        self.setup.setup_tools(self)
        self.storage.save_benchmark(self)
        for sequence in self.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for algorithm in self.algorithms:
                    self.run_algorithm(algorithm, instance)

    def run_algorithm(self, algorithm, instance):
        result = Result()
        print("Run: {} on {}".format(algorithm.name, instance.benchmark_sequence.benchmark_model.name))
        try:
            algorithm.run(instance, result)
        except Exception as e:
            self.print_exception(e, instance, algorithm)
            result.qva_error = e
            result.threw_error = True

        result.index = len(instance.results)
        instance.results.append(result)
        self.print_result(algorithm, instance, result)
        self.storage.save_result(result, instance)

    def print_result(self, algorithm, instance, result):
        if len(result.command_results) == 0:
            print("No command results")
        else:
            print(result.command_results[0].output_log)
            print(result.command_results[0].error_log)
            if result.command_results[0].exception is not None:
                self.print_exception(result.command_results[0].exception, instance, algorithm)

    def print_exception(self, exception, instance, algorithm):
        model_name = instance.benchmark_sequence.benchmark_model.name
        sequence_index = instance.benchmark_sequence.index
        instance_index = instance.index
        print("Something went wrong with model {} with parameters {} and algorithm \"{}\". benchmark_sequence {} benchmark_instance {}. "
              .format(model_name, str(instance.all_parameters), algorithm.name, sequence_index, instance_index))
        print("".join(traceback.format_exception(type(exception), exception, exception.__traceback__)))
        print(exception)
