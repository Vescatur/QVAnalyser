from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.measurements import Measurements


class ResultsPrinter(object):

    def print_characteristics(self, benchmark: Benchmark):
        different_states = 0
        different_transitions = 0
        different_branches = 0
        modest_results = 0
        modest_has_states = 0
        modest_has_transitions = 0
        modest_has_branches = 0
        storm_results = 0
        storm_has_states = 0
        storm_has_transitions = 0
        storm_has_branches = 0
        not_overlap = 1
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if not instance.results[0].threw_error and not instance.results[0].timed_out:
                    storm_results += 1
                if not instance.results[1].threw_error and not instance.results[1].timed_out:
                    modest_results += 1
                if (Measurements.STATES in instance.results[0].measurements) != (Measurements.STATES in instance.results[1].measurements):
                    not_overlap += 1
                if Measurements.STATES in instance.results[0].measurements:
                    storm_has_states += 1
                if Measurements.TRANSITIONS in instance.results[0].measurements:
                    storm_has_transitions += 1
                if Measurements.BRANCHES in instance.results[0].measurements:
                    storm_has_branches += 1
                if Measurements.STATES in instance.results[1].measurements:
                    modest_has_states += 1
                if Measurements.TRANSITIONS in instance.results[1].measurements:
                    modest_has_transitions += 1
                if Measurements.BRANCHES in instance.results[1].measurements:
                    modest_has_branches += 1
                if Measurements.STATES in instance.results[0].measurements and Measurements.STATES in instance.results[
                    1].measurements:
                    if int(instance.results[0].measurements[Measurements.STATES]) != instance.results[1].measurements[
                        Measurements.STATES]:
                        different_states += 1
                if Measurements.TRANSITIONS in instance.results[0].measurements and Measurements.TRANSITIONS in \
                        instance.results[1].measurements:
                    if int(instance.results[0].measurements[Measurements.TRANSITIONS]) != \
                            instance.results[1].measurements[Measurements.TRANSITIONS]:
                        different_transitions += 1
                if Measurements.BRANCHES in instance.results[0].measurements and Measurements.BRANCHES in \
                        instance.results[1].measurements:
                    if int(instance.results[0].measurements[Measurements.BRANCHES]) != instance.results[1].measurements[
                        Measurements.BRANCHES]:
                        different_branches += 1
        print("results")
        print(different_states)
        print(different_transitions)
        print(different_branches)
        print("not overlap " + str(not_overlap))
        print("modest " + str(modest_results))
        print("States: " + str(modest_has_states))
        print("Transitions: " + str(modest_has_transitions))
        print("Branches: " + str(modest_has_branches))
        print("storm " + str(storm_results))
        print("States: " + str(storm_has_states))
        print("Transitions: " + str(storm_has_transitions))
        print("Branches: " + str(storm_has_branches))

        states_is_one = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if Measurements.STATES in instance.results[1].measurements and Measurements.TRANSITIONS in \
                        instance.results[1].measurements:
                    # print(str(instance.results[1].measurements[Measurements.STATES]) + " " + str(instance.results[1].measurements[Measurements.TRANSITIONS]))
                    if instance.results[1].measurements[Measurements.STATES] == 1:
                        states_is_one += 1
        print(states_is_one)

    def print_error_information(self, benchmark: Benchmark):
        for algorithm in benchmark.algorithms:
             pass # self.print_error_information_for_algorithm(benchmark,algorithm)
        self.print_error_per_instance(benchmark)

    def print_error_information_for_algorithm(self, benchmark,algorithm):
        print()
        print(algorithm.name)
        threw_error_with_exception = 0
        threw_error = 0
        not_supported = 0
        qva_error = 0
        timed_out = 0
        both = 0
        missing_results = 0
        sequence_number = 0
        total = 0
        for sequence in benchmark.benchmark_sequences:
            sequence_number += 1
            complete_sequence = True
            for instance in sequence.benchmark_instances:
                complete_instance = True
                for result in instance.results:
                    if result.algorithm_name == algorithm.name:
                        if result.not_supported:
                            not_supported += 1
                        else:
                            total += 1
                            if result.threw_error:
                                threw_error += 1
                                #print(sequence_number)
                                print(result.error_text)
                                if len(result.command_results) >= 1 and result.command_results[0].exception is not None:
                                    threw_error_with_exception += 1
                                    print(result.command_results[0].output_log)
                                    print(result.command_results[0].error_log)
                            if result.qva_error:
                                qva_error += 1
                            if result.timed_out:
                                timed_out += 1
                            if result.threw_error and result.timed_out:
                                both += 1
                            if Measurements.PROPERTY_TIME not in result.measurements:
                                if not result.timed_out and not result.threw_error:
                                    missing_results += 1
        print("executed " + str(total) + " not supported " + str(not_supported))
        print("threw error " + str(threw_error))
        print("threw error with exception " + str(threw_error_with_exception))
        print("qva exception " + str(qva_error))
        print("timed out " + str(timed_out))
        print("both " + str(both))
        print("missing results " + str(missing_results))

    def print_error_per_instance(self, benchmark):
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                self.print_error_for_instance(instance)

    def print_error_for_instance(self, instance: BenchmarkInstance):
        print()
        print(instance.benchmark_sequence.benchmark_model.name + " " + instance.benchmark_sequence.property_name + " " + str(instance.benchmark_sequence.index))
        print(instance.benchmark_sequence.benchmark_model.file_name_jani)
        threw_error_with_exception = 0
        threw_error = 0
        not_supported = 0
        qva_error = 0
        timed_out = 0
        both = 0
        missing_results = 0
        total = 0
        for result in instance.results:
            if result.not_supported:
                not_supported += 1
            else:
                total += 1
                if result.threw_error:
                    threw_error += 1
                    print(result.error_text + " | " + result.algorithm_name )
                    if len(result.command_results) >= 1 and result.command_results[0].exception is not None:
                        threw_error_with_exception += 1
                if result.qva_error:
                    qva_error += 1
                if result.timed_out:
                    timed_out += 1
                if result.threw_error and result.timed_out:
                    both += 1
                if Measurements.PROPERTY_TIME not in result.measurements:
                    if not result.timed_out and not result.threw_error:
                        missing_results += 1
                        # print(sequence_number)
                        # print(result.command_results[0].output_log)
                        # print(result.command_results[0].error_log)
        print("executed " + str(total) + " not supported " + str(not_supported))
        print("threw error " + str(threw_error))
        print("threw error with exception " + str(threw_error_with_exception))
        print("qva exception " + str(qva_error))
        print("timed out " + str(timed_out))
        print("both " + str(both))
        print("missing results " + str(missing_results))

    def print_all_logs(self):
        pass

    def print_tool_errors(self, benchmark):
        print("per algorithm")
        self.tool_per_algorithm(benchmark)
        print("per file")
        self.tool_per_file(benchmark)

    def tool_per_algorithm(self, benchmark):
        for algorithm in benchmark.algorithms:
            for sequence in benchmark.benchmark_sequences:
                for instance in sequence.benchmark_instances:
                    for result in instance.results:
                        if result.algorithm_name == algorithm.name:
                            self.print_tool_error_from_result(result)

    def tool_per_file(self,benchmark):
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    self.print_tool_error_from_result(result)

    def print_tool_error_from_result(self,result):
        if result.threw_error:
            if self.should_display_error(result.error_text):
                print("Found error: " + result.error_text)
                if len(result.command_results) >= 1:
                    pass
                    print(result.command_results[0].command)
                    print(result.command_results[0].output_log)
                    print(result.command_results[0].error_log)

    def should_display_error(self, error_text):
        if "No suitable input formalism found for the given file names" in error_text:
            return False # fixed by unzipping
        if "parse error - unexpected ''" in error_text:
            return False # fixed by unzipping
        if "The probabilities for a transition do not sum up to the expected value of" in error_text:
            return False # not a tool error

        # These are serious errors
        display_serious_errors = True
        if "The program received signal 6 and will be aborted in 3s" in error_text:
            return display_serious_errors
        if "The message of this exception is: std::bad_alloc" in error_text:
            return display_serious_errors
        if "The linear programming solver did not find an optimal solution for property" in error_text:
            return display_serious_errors # Looks like other algorithms can solve it
        if "KeyNotFoundException: The given key '1' was not present in the dictionary" in error_text:
            return display_serious_errors

        return False