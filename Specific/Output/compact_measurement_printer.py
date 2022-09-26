from Library.Benchmarks.benchmark import Benchmark
from Library.Results.measurements import Measurements


class CompactMeasurementPrinter(object):

    def print_measurements(self, benchmark: Benchmark, measurements, tool_name):
        for algorithm in benchmark.algorithms:
            if algorithm.tool.name() == tool_name:
                self.print_measuremnts_for_algorithm(benchmark,measurements,algorithm)

    def print_measuremnts_for_algorithm(self, benchmark, measurements, algorithm):
        error = 0
        not_supported = 0
        timed_out = 0
        finished = 0
        has_measurement = {}
        results = []
        for measurement in measurements:
            has_measurement[measurement] = 0

        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    if result.algorithm_name == algorithm.name:
                        if result.threw_error:
                            error += 1
                        elif result.timed_out:
                            timed_out += 1
                        elif result.not_supported:
                            not_supported += 1
                        else:
                            results.append(result)
                            finished = finished + 1
                            for measurement in measurements:
                                if measurement in result.measurements:
                                    has_measurement[measurement] += 1
                                else:
                                    i = 1

        print(algorithm.name)
        print("Error "+str(error))
        print("Timed out "+str(timed_out))
        print("Not supported "+str(not_supported))
        print("Finished "+str(finished))
        for measurement in measurements:
            print("Missing " + str(measurement) + " " + str(finished-has_measurement[measurement]))
        print()





    def print_measurements2(self, benchmark: Benchmark, measurements):
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
