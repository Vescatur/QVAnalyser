from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.Modest.modest_algorithm_type import ModestAlgorithmType
from Specific.Tools.Modest.modest_execution import ModestExecution


class ModestAlgorithm(Algorithm):

    def __init__(self, tool: Tool, name: str, algorithm_type: ModestAlgorithmType):
        super().__init__(tool, name)
        self.algorithm_type = algorithm_type

    def is_supported(self, instance: BenchmarkInstance):
        model_type = instance.benchmark_sequence.benchmark_model.formal_model_type
        property_type = instance.benchmark_sequence.property_type
        match self.algorithm_type:
            case ModestAlgorithmType.LINEAR_PROGRAMMING | ModestAlgorithmType.SEQUENTIAL_INTERVAL_ITERATION:
                if property_type == PropertyType.REACHABILITY:
                    return True
                else:
                    return False
            case ModestAlgorithmType.VALUE_ITERATION | ModestAlgorithmType.INTERVAL_ITERATION | ModestAlgorithmType.SOUND_VALUE_ITERATION | ModestAlgorithmType.OPTIMISTIC_VALUE_ITERATION:
                return True
            case ModestAlgorithmType.GENERAL_LABELED_REAL_TIME_DYNAMIC_PROGRAMMING:
                if model_type == ModelType.MDP:
                    return True
                else:
                    return False
            case ModestAlgorithmType.CONFIDENCE_INTERVAL:
                if model_type == ModelType.DTMC or model_type == ModelType.CTMC:
                    return True
                else:
                    return False
            case ModestAlgorithmType.ADAPTIVE | ModestAlgorithmType.APMC:
                if model_type == ModelType.DTMC or model_type == ModelType.CTMC:
                    if property_type == PropertyType.REACHABILITY:
                        return True
                else:
                    return False
            case _:
                raise Exception("Incomplete match statement")

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        ModestExecution(instance, result, self.algorithm_type)
        return result

