from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.Prism.prism_algorithm_type import PrismAlgorithmType
from Specific.Tools.Prism.prism_engine_type import PrismEngineType
from Specific.Tools.Prism.prism_execution import PrismExecution
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType


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
        model_type = model.formal_model_type
        property_type = instance.benchmark_sequence.property_type
        if model.file_path_prism_model is None:
            return False
        if model.file_path_prism_props is None:
            return False
        if model.file_path_prism_props[-6:] == ".prctl":
            return False

        match model_type:
            case ModelType.PTA:
                match self.algorithm_type:
                    case PrismAlgorithmType.STOCHASTIC_GAMES | PrismAlgorithmType.BACKWARDS_REACHABILITY:
                        match property_type:
                            case PropertyType.REACHABILITY:
                                return True
                            case _:
                                return False
                    case PrismAlgorithmType.DIGITAL_CLOCKS:
                        return True
                    case _:
                        return False
            case ModelType.CTMC | ModelType.DTMC:
                match self.algorithm_type:
                    case PrismAlgorithmType.APPROXIMATE_PROBABILISTIC_MODEL_CHECKING:
                        match property_type:
                            case PropertyType.REACHABILITY:
                                return True
                            case _:
                                return False
                    case PrismAlgorithmType.ASYMPTOTIC_CONFIDENCE_INTERVAL | PrismAlgorithmType.CONFIDENCE_INTERVAL:
                        return True
                    case PrismAlgorithmType.VALUE_ITERATION | PrismAlgorithmType.JACOBI | PrismAlgorithmType.GAUSS_SEIDEL | \
                         PrismAlgorithmType.BACKWARDS_GAUSS_SEIDEL | PrismAlgorithmType.JACOBI_WITH_OVER_RELAXATION | \
                         PrismAlgorithmType.SUCCESSIVE_OVER_RELAXATION | PrismAlgorithmType.BACKWARDS_SUCCESSIVE_OVER_RELAXATION | \
                         PrismAlgorithmType.PSEUDO_GAUSS_SEIDEL | PrismAlgorithmType.BACKWARDS_PSEUDO_GAUSS_SEIDEL | \
                         PrismAlgorithmType.PSEUDO_SUCCESSIVE_OVER_RELAXATION | PrismAlgorithmType.BACKWARDS_PSEUDO_SUCCESSIVE_OVER_RELAXATION:
                        return True
                    case _:
                        return False
            case ModelType.MDP:
                match self.algorithm_type:
                    case PrismAlgorithmType.VALUE_ITERATION:
                        return True
                    case _:
                        match self.engine_type:
                            case PrismEngineType.EXPLICIT:
                                match self.algorithm_type:
                                    case PrismAlgorithmType.MODIFIED_POLICY_ITERATION:
                                        match property_type:
                                            case PropertyType.REACHABILITY:
                                                return True
                                            case _:
                                                return False
                                    case PrismAlgorithmType.GAUSS_SEIDEL | PrismAlgorithmType.POLICY_ITERATION:
                                        return True
                                    case _:
                                        return False
                            case _:
                                return False
            case ModelType.MA:
                return False





        return True

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        PrismExecution(instance, result, self.algorithm_type, self.engine_type, self.use_topological)
        return result

