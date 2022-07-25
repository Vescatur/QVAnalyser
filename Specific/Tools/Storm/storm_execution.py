from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.execution import Execution
from Specific.Helpers.storm import Storm
from Specific.Tools.Storm.storm_algorithm_type import StormAlgorithmType
from Specific.Tools.Storm.storm_engine_type import StormEngineType


class StormExecution(Execution):

    def __init__(self, instance: BenchmarkInstance, result: Result, algorithm_type: StormAlgorithmType, engine_type: StormEngineType, use_topological: bool):
        self.algorithm_type = algorithm_type
        self.engine_type = engine_type
        self.use_topological = use_topological
        super().__init__(instance, result)

    def run(self):
        command = self.generate_command_text()
        self.run_command(command)

    def generate_command_text(self):
        benchmark_sequence = self.benchmark_instance.benchmark_sequence
        file_path = benchmark_sequence.benchmark_model.file_path_jani
        property_name = benchmark_sequence.property_name
        parameters_argument = self.generate_parameter_text(self.benchmark_instance.all_parameters)
        engine_argument = self.generate_engine_argument()
        eqsolver_argument = self.generate_eqsolver_argument()
        minmax_argument = self.generate_minmax_argument()
        native_argument = self.generate_native_argument()
        topological_minmax_argument = self.generate_topological_minmax_argument()
        topological_eqsolver_argument = self.generate_topological_eqsolver_argument()
        command = "{} --jani {} --janiproperty {} {} {} {} {} {} {} {} --verbose --precision 1e-6" \
            .format(Storm().tool_path, file_path, property_name, parameters_argument, engine_argument, eqsolver_argument, topological_eqsolver_argument, native_argument, minmax_argument, topological_minmax_argument)
        return command

    def generate_eqsolver_argument(self):
        if self.use_topological:
            return "--core:eqsolver topological"
        algorithm_name = self.algorithm_type_to_eqsolver()
        if algorithm_name is None:
            return ""
        return "--core:eqsolver " + algorithm_name

    def generate_topological_eqsolver_argument(self):
        if not self.use_topological:
            return ""
        algorithm_name = self.algorithm_type_to_eqsolver()
        if algorithm_name is None:
            return ""
        return "--topological:eqsolver " + algorithm_name

    def algorithm_type_to_eqsolver(self):
        match self.algorithm_type:
            case StormAlgorithmType.GMM_PLUS_PLUS:
                return "gmm++"
            case StormAlgorithmType.EIGEN:
                return "eigen"
            case StormAlgorithmType.ELIMINATION:
                return "elimination"
            case StormAlgorithmType.JACOBI | StormAlgorithmType.GAUSS_SEIDEL | StormAlgorithmType.SUCCESSIVE_OVER_RELAXATION | \
                StormAlgorithmType.WALKERCHAE | StormAlgorithmType.VALUE_ITERATION | StormAlgorithmType.SOUND_VALUE_ITERATION | \
                StormAlgorithmType.OPTIMISTIC_VALUE_ITERATION | StormAlgorithmType.OPTIMISTIC_VALUE_ITERATION | \
                StormAlgorithmType.INTERVAL_ITERATION | StormAlgorithmType.RATIONAL_SEARCH:
                return "native"


    def generate_minmax_argument(self):
        if self.use_topological:
            return "--minmax:method topological"
        algorithm_name = self.algorithm_type_to_minmax()
        if algorithm_name is None:
            return ""
        return "--minmax:method " + algorithm_name

    def generate_topological_minmax_argument(self):
        if not self.use_topological:
            return ""
        algorithm_name = self.algorithm_type_to_minmax()
        if algorithm_name is None:
            return ""
        return "--topological:minmax " + algorithm_name

    def algorithm_type_to_minmax(self):
        match self.algorithm_type:
            case StormAlgorithmType.VALUE_ITERATION:
                return "value-iteration"
            case StormAlgorithmType.POLICY_ITERATION:
                return "policy-iteration"
            case StormAlgorithmType.LINEAR_PROGRAMMING:
                return "linear-programming"
            case StormAlgorithmType.RATIONAL_SEARCH:
                return "ratsearch --exact"
            case StormAlgorithmType.INTERVAL_ITERATION:
                return "interval-iteration"
            case StormAlgorithmType.SOUND_VALUE_ITERATION:
                return "sound-value-iteration"
            case StormAlgorithmType.OPTIMISTIC_VALUE_ITERATION:
                return "ovi"
            case StormAlgorithmType.VALUE_ITERATION_TO_POLICY_ITERATION:
                return "vi-to-pi"
            case StormAlgorithmType.ACYCLIC:
                return "acyclic"

    def generate_native_argument(self):
        native_argument = "--native:method "
        match self.algorithm_type:
            case StormAlgorithmType.JACOBI:
                return native_argument + "jacobi"
            case StormAlgorithmType.GAUSS_SEIDEL:
                return native_argument + "gaussseidel"
            case StormAlgorithmType.SUCCESSIVE_OVER_RELAXATION:
                return native_argument + "sor"
            case StormAlgorithmType.WALKERCHAE:
                return native_argument + "walkerchae"
            case StormAlgorithmType.VALUE_ITERATION:
                return native_argument + "power"
            case StormAlgorithmType.SOUND_VALUE_ITERATION:
                return native_argument + "sound-value-iteration"
            case StormAlgorithmType.OPTIMISTIC_VALUE_ITERATION:
                return native_argument + "ovi"
            case StormAlgorithmType.INTERVAL_ITERATION:
                return native_argument + "interval-iteration"
            case StormAlgorithmType.RATIONAL_SEARCH:
                return native_argument + "ratsearch --exact"
        return ""


    def generate_engine_argument(self):
        engine_argument = "--core:engine "
        match self.engine_type:
            case StormEngineType.SPARSE_MATRICES:
                return engine_argument + "sparse"
            case StormEngineType.HYBRID:
                return engine_argument + "hybrid"
            case StormEngineType.DECISION_DIAGRAM:
                return engine_argument + "dd"
            case StormEngineType.DECISION_DIAGRAM_TO_SPARSE_MATRICES:
                return engine_argument + "dd-to-sparse"
            case StormEngineType.EXPLORATION:
                return engine_argument + "expl"
            case StormEngineType.ABSTRACTION_REFINEMENT:
                return engine_argument + "abs"
        return ""

    def generate_parameter_text(self, parameters):
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, str(parameters[key]).lower())
        parametersText = parametersText[:-1]  # Removes last comma.
        if parametersText == "":
            return ""
        else:
            return "--constants " + parametersText