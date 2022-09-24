import json
import os

from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.execution import Execution
from Specific.Tools.ModestBound.modest_bound_helper import ModestBoundHelper


class ModestBoundExecution(Execution):

    def __init__(self, instance: BenchmarkInstance, result: Result):
        super().__init__(instance, result)

    def run(self):
        command = self.generate_command_text()
        self.run_command(command)
        self.read_json()

    def generate_command_text(self):
        parameters_argument = self.generate_parameter_text(self.benchmark_instance.all_parameters)
        benchmark_sequence = self.benchmark_instance.benchmark_sequence
        file_path = benchmark_sequence.benchmark_model.file_path_jani
        property_name = benchmark_sequence.property_name
        algorithm_name = "IntervalIteration"

        command = "{} check {} --alg {} --epsilon 1e-6 --width 1e-3 --props {} {} -O {} Json" \
            .format(ModestBoundHelper().tool_path, file_path, algorithm_name, property_name, parameters_argument,
                    ModestBoundHelper().temp_file_path)
        return command

    def generate_parameter_text(self, parameters):
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, parameters[key])
        parametersText = parametersText[:-1]  # Removes last comma.
        if parametersText == "":
            return ""
        else:
            return "-E " + parametersText

    def read_json(self):
        if os.path.exists(ModestBoundHelper().temp_file_path):
            file = open(ModestBoundHelper().temp_file_path, "r", encoding='utf-8-sig')
            json_output = json.load(file)
            self.result.json_output = json_output
            file.close()
            os.remove(ModestBoundHelper().temp_file_path)

