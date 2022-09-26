from Library.Benchmarks.benchmark import Benchmark
from Library.Results.measurements import Measurements
from Library.Results.result import Result
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Prism.prism_tool import PrismTool


class BenchmarkResultParser(object):

    def __init__(self, benchmark: Benchmark, remove_output_log,remove_duplicate_results):
        self.benchmark = benchmark
        if remove_duplicate_results:
            self.remove_duplicates()
        self.parse_benchmark()
        if remove_output_log:
            self.remove_output_log()
        self.add_characteristics_to_statistical_algorithms()

    # This allows for smaller file sizes which increases performance
    def remove_output_log(self):
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    if len(result.command_results) >= 1:
                        result.command_results[0].output_log = ""


    # A save had multiple entries from the same result because of a bug. This removes these entries
    def remove_duplicates(self):
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                no_duplicate_results = []
                for result in reversed(instance.results):
                    if self.result_is_not_in_array(result, no_duplicate_results):
                        no_duplicate_results.append(result)
                instance.results = no_duplicate_results

    def result_is_not_in_array(self, result, no_duplicate_results):
        for result2 in no_duplicate_results:
            if result.algorithm_name == result2.algorithm_name:
                return False
        return True

    def parse_benchmark(self):
        for sequence in self.benchmark.benchmark_sequences:
            print(sequence.index)
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    # print("result index" + str(result.index))
                    if not result.threw_error:
                        self.parse_result(result, self.benchmark)

    def parse_result(self, result: Result,benchmark: Benchmark):
        tool_for_result = None
        for tool in self.benchmark.tools:
            if tool.name() == result.tool_name:
                tool_for_result = tool
                break
        if tool_for_result is not None:
            tool_for_result.result_parser.parse_result(result, benchmark)
        else:
            raise Exception("Could not find tool of result. The tool name is " + str(result.tool_name))

    def add_characteristics_to_statistical_algorithms(self):
        measurements = [Measurements.STATES, Measurements.TRANSITIONS, Measurements.BRANCHES]
        algorithm_vi_modest = ModestTool().value_iteration
        algorithms_to_modest_ci = [ModestTool().glrtdp,ModestTool().confidence_interval,ModestTool().adaptive,ModestTool().okamoto]
        self.add_characteristics_to_algorithm(algorithm_vi_modest, algorithms_to_modest_ci, measurements)

        algorithm_vi_prism = PrismTool().value_iteration_mtbddd
        algorithms_to_prism_ci = [PrismTool().confidence_interval,PrismTool().asymptotic_confidence_interval,PrismTool().apmc]
        self.add_characteristics_to_algorithm(algorithm_vi_prism, algorithms_to_prism_ci, measurements)

        algorithm_vi_prism = PrismTool().digital_clocks
        algorithms_to_prism_ci = [PrismTool().backwards_reachability,PrismTool().stochastic_games]
        self.add_characteristics_to_algorithm(algorithm_vi_prism, algorithms_to_prism_ci, measurements)

    def add_characteristics_to_algorithm(self, algorithm_from, algorithms_to, measurements):
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                from_result = None
                for result in instance.results:
                    if result.algorithm_name == algorithm_from.name:
                        if not result.threw_error and not result.not_supported and not result.timed_out:
                            from_result = result
                            break
                if from_result is not None:
                    for to_result in instance.results:
                        for alg_to in algorithms_to:
                            if to_result.algorithm_name == alg_to.name:
                                for measurement in measurements:
                                    if measurement not in to_result.measurements:
                                        to_result.measurements[measurement] = from_result.measurements[measurement]

