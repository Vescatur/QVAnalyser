from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.Prism.prism_algorithm_type import PrismAlgorithmType
from Specific.Tools.Prism.prism_engine_type import PrismEngineType
from Specific.Tools.Prism.prism_execution import PrismExecution


class PrismAlgorithm(Algorithm):

    def __init__(self, tool: Tool, algorithm_type: PrismAlgorithmType, engine_type: PrismEngineType, use_topological: bool):
        name = ""
        if use_topological:
            name = tool.name() + " topological " + algorithm_type.value + " " + engine_type.value
        else:
            name = tool.name() + " " + algorithm_type.value + " " + engine_type.value
        super().__init__(tool, name)
        self.use_topological = use_topological
        self.algorithm_type = algorithm_type
        self.engine_type = engine_type

    def is_supported(self, instance: BenchmarkInstance):
        model = instance.benchmark_sequence.benchmark_model
        if model.file_path_prism_model is None:
            return False
        if model.file_path_prism_props is None:
            return False
        return True

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        PrismExecution(instance, result, self.algorithm_type, self.engine_type, self.use_topological)
        return result

