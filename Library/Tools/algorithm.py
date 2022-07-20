from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.tool import Tool


class Algorithm(object):

    def __init__(self, tool: Tool, execution_constructor, name: str):
        self.tool = tool
        self.execution_constructor = execution_constructor
        self.name = name

    def run(self, instance: BenchmarkInstance, result: Result) -> Result:
        result.algorithm_name = self.name
        result.tool_name = self.tool.name()
        self.execution_constructor(instance, result)
        return result

