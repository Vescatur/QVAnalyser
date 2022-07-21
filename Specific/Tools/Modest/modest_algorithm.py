from Library.Benchmarks.benchmark_instance import BenchmarkInstance
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
            case ModestAlgorithmType.LinearProgramming | ModestAlgorithmType.SequentialIntervalIteration:
                if property_type == "prob-reach":
                    return True
                else:
                    return False
            case ModestAlgorithmType.ValueIteration | ModestAlgorithmType.IntervalIteration | ModestAlgorithmType.SoundValueIteration | ModestAlgorithmType.OptimisticValueIteration:
                return True
            case ModestAlgorithmType.GeneralLabeledRealTimeDynamicProgramming:
                if model_type == "mdp":
                    return True
                else:
                    return False
            case ModestAlgorithmType.ConfidenceInterval:
                if model_type == "dtmc" or model_type == "ctmc":
                    return True
                else:
                    return False
            case ModestAlgorithmType.Adaptive | ModestAlgorithmType.APMC:
                if model_type == "dtmc" or model_type == "ctmc":
                    if property_type == "prob-reach":
                        return True
                return False
            case _:
                raise Exception("Incomplete match statement")

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        ModestExecution(instance, result, self.algorithm_type)
        return result

