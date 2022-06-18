import json
import os
import shutil

from Library.Tools.execution import Execution
from Library.Results.measurements import Measurements
from Specific.Helpers.modest import Modest


class ModestIntervalIteration(Execution):

    def run(self):
        command = self.generate_command_text()
        self.run_command(command)
        self.read_json()

    def generate_command_text(self):
        parametersText = self.generate_parameter_text(self.benchmark_instance.all_parameters)
        benchmark_sequence = self.benchmark_instance.benchmark_sequence
        file_path = benchmark_sequence.benchmark_model.file_path
        property_name = benchmark_sequence.property_name
        command = "{} check {} --alg IntervalIteration --epsilon 1e-6 --props {} {} -O {} Json" \
            .format(Modest().tool_path, file_path, property_name, parametersText, Modest().temp_file_path)
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
        if os.path.exists(Modest().temp_file_path):
            file = open(Modest().temp_file_path, "r", encoding='utf-8-sig')
            json_output = json.load(file)
            self.result.json_output = json_output
            file.close()
            os.remove(Modest().temp_file_path)

