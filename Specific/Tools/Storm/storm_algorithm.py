from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.Storm.storm_algorithm_type import StormAlgorithmType
from Specific.Tools.Storm.storm_engine_type import StormEngineType
from Specific.Tools.Storm.storm_execution import StormExecution


class StormAlgorithm(Algorithm):

    def __init__(self, tool: Tool, algorithm_type: StormAlgorithmType, engine_type: StormEngineType, use_topological: bool, use_bisimulation: bool):
        topological = ""
        if use_topological:
            topological = " topological"
        bisimulation = ""
        if use_bisimulation:
            bisimulation = " bisimulation"

        name = tool.name() + "{}{} ".format(topological, bisimulation) + algorithm_type.value + " " + engine_type.value

        super().__init__(tool, name)
        self.use_topological = use_topological
        self.use_bisimulation = use_bisimulation
        self.algorithm_type = algorithm_type
        self.engine_type = engine_type

    def is_supported(self, instance: BenchmarkInstance):
        model_type = instance.benchmark_sequence.benchmark_model.formal_model_type
        property_type = instance.benchmark_sequence.property_type
        if model_type == ModelType.PTA:
            return False

        if self.use_bisimulation and model_type == ModelType.MA:
            match self.engine_type:
                case StormEngineType.SPARSE_MATRICES:
                    return False
                case StormEngineType.DECISION_DIAGRAM_TO_SPARSE_MATRICES | StormEngineType.HYBRID | StormEngineType.DECISION_DIAGRAM:
                    pass

        match instance.benchmark_sequence.benchmark_model.name:
            case "ma/polling-system/polling-system" | "ma/reentrant-queues/reentrant-queues": # These models have the feature nondet-selection
                return False
            case "ma/breakdown-queues/breakdown-queues" | "ma/ftwc/ftwc" | "mdp/echoring/echoring":
                match self.engine_type:
                    case StormEngineType.HYBRID | StormEngineType.DECISION_DIAGRAM_TO_SPARSE_MATRICES | StormEngineType.DECISION_DIAGRAM | StormEngineType.ABSTRACTION_REFINEMENT:
                        return False # The symbolic JANI model builder currently does not support assignment levels"

        match self.engine_type:
            case StormEngineType.DECISION_DIAGRAM:
                match self.algorithm_type:
                    case StormAlgorithmType.VALUE_ITERATION | StormAlgorithmType.RATIONAL_SEARCH:
                        match model_type:
                            case ModelType.DTMC | ModelType.MDP:
                                return True
                    case StormAlgorithmType.JACOBI:
                        match model_type:
                            case ModelType.DTMC:
                                return True
                    case StormAlgorithmType.POLICY_ITERATION:
                        match model_type:
                            case ModelType.MDP:
                                return True
            case StormEngineType.SPARSE_MATRICES | StormEngineType.DECISION_DIAGRAM_TO_SPARSE_MATRICES | StormEngineType.HYBRID:
                match self.algorithm_type:
                    case StormAlgorithmType.VALUE_ITERATION | StormAlgorithmType.SOUND_VALUE_ITERATION | \
                         StormAlgorithmType.OPTIMISTIC_VALUE_ITERATION | StormAlgorithmType.INTERVAL_ITERATION | \
                         StormAlgorithmType.RATIONAL_SEARCH:
                            return True
                    case StormAlgorithmType.GMM_PLUS_PLUS | StormAlgorithmType.JACOBI | StormAlgorithmType.GAUSS_SEIDEL | \
                         StormAlgorithmType.SUCCESSIVE_OVER_RELAXATION | StormAlgorithmType.WALKERCHAE | \
                         StormAlgorithmType.EIGEN | StormAlgorithmType.ELIMINATION:
                        match model_type:
                            case ModelType.DTMC | ModelType.CTMC:
                                return True
                    case StormAlgorithmType.POLICY_ITERATION | StormAlgorithmType.LINEAR_PROGRAMMING | StormAlgorithmType.VALUE_ITERATION_TO_POLICY_ITERATION:
                        match model_type:
                            case ModelType.MDP | ModelType.MA:
                                return True
            case StormEngineType.EXPLORATION:
                match self.algorithm_type:
                    case StormAlgorithmType.EXPLORATION:
                        match model_type:
                            case ModelType.DTMC | ModelType.MDP:
                                match property_type:
                                    case PropertyType.REACHABILITY:
                                        return True
            case StormEngineType.ABSTRACTION_REFINEMENT:
                match self.algorithm_type:
                    case StormAlgorithmType.ABSTRACTION_REFINEMENT:
                        match model_type:
                            case ModelType.DTMC | ModelType.MDP:
                                match property_type:
                                    case PropertyType.REACHABILITY:
                                        return True
        return False

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        StormExecution(instance, result, self.algorithm_type, self.engine_type, self.use_topological, self.use_bisimulation)
        return result

