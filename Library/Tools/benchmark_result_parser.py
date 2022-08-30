from Library.Benchmarks.benchmark import Benchmark
from Library.Results.result import Result
from Library.storage import Storage


class BenchmarkResultParser(object):

    def __init__(self, benchmark: Benchmark, remove_output_log):
        self.benchmark = benchmark
        self.remove_duplicates()
        self.parse_benchmark()
        if remove_output_log:
            self.remove_output_log()

    # This allows for smaller file sizes which increases performance
    def remove_output_log(self):
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    if len(result.command_results) >= 1:
                        result.command_results[0].output_log = ""


    # A save had multiple entries from the same result because of a bug. This removes these entries
    def remove_duplicates(self):
        print("removing duplicates")
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                no_duplicate_results = []
                for result in instance.results:
                    if self.result_is_not_in_array(result, no_duplicate_results):
                        no_duplicate_results.append(result)

                instance.results = no_duplicate_results

    def result_is_not_in_array(self, result, no_duplicate_results):
        for result2 in no_duplicate_results:
            if result.index == result2.index:
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