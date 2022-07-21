from Library.Benchmarks.benchmark import Benchmark
from Library.Results.result import Result
from Library.storage import Storage


class BenchmarkResultParser(object):

    def __init__(self, benchmark: Benchmark):
        self.benchmark = benchmark
        self.parse_benchmark()

    def parse_benchmark(self):
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    self.parse_result(result)

    def parse_result(self, result: Result):
        tool_for_result = None
        for tool in self.benchmark.tools:
            if tool.name() == result.tool_name:
                tool_for_result = tool
                break
        if tool_for_result is not None:
            tool_for_result.result_parser.parse_result(result)
        else:
            raise Exception("Could not find tool of result. The tool name is " + str(result.tool_name))