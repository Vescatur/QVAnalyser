from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.ModestBound.modest_bound_execution import ModestBoundExecution


class ModestBoundAlgorithm(Algorithm):

    def __init__(self, tool: Tool, name: str):
        super().__init__(tool, name)

    def is_supported(self, instance: BenchmarkInstance):

        match instance.benchmark_sequence.benchmark_model.name:
            case "dtmc/bluetooth/bluetooth" | "dtmc/herman/herman": # Complex initial states specifications are not yet supported
                return False
            case "pta/csma-pta/csma-pta":
                return False # Incompatible expression type: Expected int, found real
            case "pta/csma_abst-pta/csma_abst-pta" | "pta/repudiation_honest/repudiation_honest" | "pta/repudiation_malicious/repudiation_malicious":
                return False # Open clock constraints are not allowed.

        return True

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        ModestBoundExecution(instance, result)
        return result

