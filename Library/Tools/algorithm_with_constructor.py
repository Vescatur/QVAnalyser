from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool


class AlgorithmWithConstructor(Algorithm):

    def __init__(self, tool: Tool, execution_constructor, name: str):
        super().__init__(tool, name)
        self.execution_constructor = execution_constructor

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        self.execution_constructor(instance, result)
        return result

