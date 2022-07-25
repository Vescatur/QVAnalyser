from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.tool import Tool


class Algorithm(object):

    def __init__(self, tool: Tool, name: str):
        self.tool = tool
        self.name = name

    def create_not_supported_result(self, result: Result) -> Result:
        result.not_supported = True
        return result

    def run(self, instance: BenchmarkInstance, result: Result) -> Result:
        result.algorithm_name = self.name
        result.tool_name = self.tool.name()
        if self.is_supported(instance):
            return self.protected_run(instance, result)
        else:
            return self.create_not_supported_result(result)

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        raise Exception("Unimplemented method Algorithm.protected_run()")

    def is_supported(self, instance: BenchmarkInstance):
        raise Exception("Unimplemented method Algorithm.is_supported()")

