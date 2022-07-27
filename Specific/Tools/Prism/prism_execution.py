from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.execution import Execution
from Specific.Tools.Prism.prism_algorithm_type import PrismAlgorithmType
from Specific.Tools.Prism.prism_engine_type import PrismEngineType
from Specific.Tools.Prism.prism_helper import PrismHelper


class PrismExecution(Execution):

    def __init__(self, instance: BenchmarkInstance, result: Result, algorithm_type: PrismAlgorithmType,
                 engine_type: PrismEngineType, use_topological: bool):
        self.algorithm_type = algorithm_type
        self.engine_type = engine_type
        self.use_topological = use_topological
        super().__init__(instance, result)

    def run(self):
        command = self.generate_command_text()
        self.run_command(command)

    def generate_command_text(self):
        benchmark_model = self.benchmark_instance.benchmark_sequence.benchmark_model
        model_path = benchmark_model.file_path_prism_model
        props_path = benchmark_model.file_path_prism_props
        property_name = self.benchmark_instance.benchmark_sequence.property_name
        parameters_argument = self.generate_parameter_text(self.benchmark_instance.all_parameters)

        method_linear_equations = self.generate_method_linear_equations()
        method_mdp = self.generate_method_mdp()
        pta = self.generate_pta()
        engine = self.generate_engine()
        method_simulator = self.generate_method_simulator()
        topological = ""
        if self.use_topological:
            topological = "-topological"

        match self.algorithm_type:
            case PrismAlgorithmType.CONFIDENCE_INTERVAL | PrismAlgorithmType.ASYMPTOTIC_CONFIDENCE_INTERVAL | \
                 PrismAlgorithmType.APPROXIMATE_PROBABILISTIC_MODEL_CHECKING:
                return "{} {} {} --property {} {} -javamaxmem 11g -cuddmaxmem 4g -simconf 0.95 -simwidth 1e-3 -sim {}" \
                    .format(PrismHelper().tool_path, model_path, props_path, property_name, parameters_argument, method_simulator)
            case _:
                return "{} {} {} --property {} {} -javamaxmem 11g -cuddmaxmem 4g -relative -epsilon 1e-6 -maxiters 1000000 {} {} {} {} {}" \
                    .format(PrismHelper().tool_path, model_path, props_path, property_name, parameters_argument,
                            method_linear_equations, method_mdp, topological, pta, engine)

    def generate_parameter_text(self, parameters):
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, str(parameters[key]).lower())
        parametersText = parametersText[:-1]  # Removes last comma.
        if parametersText == "":
            return ""
        else:
            return "--const " + parametersText

    def generate_method_linear_equations(self):
        match self.algorithm_type:
            case PrismAlgorithmType.VALUE_ITERATION:
                return "-power"
            case PrismAlgorithmType.JACOBI:
                return "-jacobi"
            case PrismAlgorithmType.GAUSS_SEIDEL:
                return "-gaussseidel"
            case PrismAlgorithmType.BACKWARDS_GAUSS_SEIDEL:
                return "-bgaussseidel"
            case PrismAlgorithmType.PSEUDO_GAUSS_SEIDEL:
                return "-pgaussseidel"
            case PrismAlgorithmType.BACKWARDS_PSEUDO_GAUSS_SEIDEL:
                return "-bpgaussseidel"
            case PrismAlgorithmType.JACOBI_WITH_OVER_RELAXATION:
                return "-jor"
            case PrismAlgorithmType.SUCCESSIVE_OVER_RELAXATION:
                return "-sor"
            case PrismAlgorithmType.BACKWARDS_SUCCESSIVE_OVER_RELAXATION:
                return "-bsor"
            case PrismAlgorithmType.PSEUDO_SUCCESSIVE_OVER_RELAXATION:
                return "-psor"
            case PrismAlgorithmType.BACKWARDS_PSEUDO_SUCCESSIVE_OVER_RELAXATION:
                return "-bpsor"
            case _:
                return ""

    def generate_method_mdp(self):
        match self.algorithm_type:
            case PrismAlgorithmType.VALUE_ITERATION:
                return "-valiter"
            case PrismAlgorithmType.GAUSS_SEIDEL:
                return "-gaussseidel"
            case PrismAlgorithmType.POLICY_ITERATION:
                return "-politer"
            case PrismAlgorithmType.MODIFIED_POLICY_ITERATION:
                return "-modpoliter"
            case PrismAlgorithmType.INTERVAL_ITERATION:
                return "-intervaliter"
            case _:
                return ""

    def generate_pta(self):
        match self.algorithm_type:
            case PrismAlgorithmType.STOCHASTIC_GAMES:
                return "-ptamethod games"
            case PrismAlgorithmType.DIGITAL_CLOCKS:
                return "-ptamethod digital"
            case PrismAlgorithmType.BACKWARDS_REACHABILITY:
                return "-ptamethod backwards"
            case _:
                return ""

    def generate_engine(self):
        match self.engine_type:
            case PrismEngineType.MT_BINARY_DECISION_DIAGRAM:
                return "-mtbdd"
            case PrismEngineType.SPARSE_MATRICES:
                return "-sparse"
            case PrismEngineType.HYBRID:
                return "-hybrid"
            case PrismEngineType.EXPLICIT:
                return "-explicit"
            case _:
                return ""

    def generate_method_simulator(self):
        match self.algorithm_type:
            case PrismAlgorithmType.CONFIDENCE_INTERVAL:
                return "-simmethod ci"
            case PrismAlgorithmType.ASYMPTOTIC_CONFIDENCE_INTERVAL:
                return "-simmethod aci"
            case PrismAlgorithmType.APPROXIMATE_PROBABILISTIC_MODEL_CHECKING:
                return "-simmethod apmc"
            case _:
                return ""
