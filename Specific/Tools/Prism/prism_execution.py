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

        command = "{} {} {} --property {} {}" \
            .format(PrismHelper().tool_path, model_path, props_path, property_name, parameters_argument)
        return command

    def generate_parameter_text(self, parameters):
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, str(parameters[key]).lower())
        parametersText = parametersText[:-1]  # Removes last comma.
        if parametersText == "":
            return ""
        else:
            return "--const " + parametersText