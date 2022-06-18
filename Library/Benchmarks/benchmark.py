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
        self.save_index = None

        self.setup = Setup()
        self.setup.setup_resource_folders()
        self.storage = Storage()
        self.tools = []
        self.benchmark_path = Setup().benchmark_models_path

    def run(self):
        self.print_start_information(self.benchmark_sequences, self.algorithms)
        self.run_algorithms()
        self.storage.save_finished_benchmark(self)

    def run_algorithms(self):
        self.setup.setup_tools(self)
        self.storage.save_unfinished_benchmark(self)
        for sequence in self.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for algorithm in self.algorithms:
                    if not self.has_algorithm_run_on_instance(algorithm, instance):
                        self.run_algorithm(algorithm, instance)


    def has_algorithm_run_on_instance(self, algorithm, instance):
        for result in instance.results:
            if algorithm.name == result.algorithm_name:
                return True
        return False

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

    def print_start_information(self, benchmark_sequences, algorithms):
        number_of_sequences = 0
        number_of_complete_sequences = 0
        number_of_instances = 0
        number_of_complete_instances = 0
        number_of_executions = 0
        number_of_complete_executions = 0
        number_of_algorithms = 0
        for sequence in benchmark_sequences:
            complete_sequence = True
            for instance in sequence.benchmark_instances:
                complete_instance = True
                for algorithm in self.algorithms:
                    number_of_executions += 1
                    if self.has_algorithm_run_on_instance(algorithm, instance):
                        number_of_complete_executions += 1
                    else:
                        complete_sequence = False
                        complete_instance = False
                number_of_instances += 1
                if complete_instance:
                    number_of_complete_instances += 1
            number_of_sequences += 1
            if complete_sequence:
                number_of_complete_sequences += 1

        for _ in algorithms:
            number_of_algorithms += 1

        print("Found " + str(number_of_sequences) + " sequence(s), " +
              str(number_of_instances) + " instance(s) and " +
              str(number_of_algorithms) + " algorithm(s). This requires " +
              str(number_of_executions) + " executions.")

        if number_of_complete_executions != 0:
            print(str(number_of_complete_sequences)+"/"+str(number_of_sequences)+" sequence(s) completed. " +
                  str(number_of_complete_instances)+"/"+str(number_of_instances)+" instance(s) completed. " +
                  str(number_of_complete_executions)+"/"+str(number_of_executions)+" execution(s) completed.")
