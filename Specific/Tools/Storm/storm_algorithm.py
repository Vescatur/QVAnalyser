from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.Storm.storm_algorithm_type import StormAlgorithmType
from Specific.Tools.Storm.storm_engine_type import StormEngineType
from Specific.Tools.Storm.storm_execution import StormExecution


class StormAlgorithm(Algorithm):

    def __init__(self, tool: Tool, name: str, algorithm_type: StormAlgorithmType, engine_type: StormEngineType, use_topological: bool):
        super().__init__(tool, name)
        self.use_topological = use_topological
        self.algorithm_type = algorithm_type
        self.engine_type = engine_type

    def is_supported(self, instance: BenchmarkInstance):
        model_type = instance.benchmark_sequence.benchmark_model.formal_model_type
        property_type = instance.benchmark_sequence.property_type
        return True

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        StormExecution(instance, result, self.algorithm_type, self.engine_type, self.use_topological)
        return result

