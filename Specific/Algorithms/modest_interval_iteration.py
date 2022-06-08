import json
import os

from Library.Algorithms.execution import Execution
from Library.Results.statistics import Statistics
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
        command = "{} check {} --alg IntervalIteration --props {} -E {} -O {} Json" \
            .format(Modest().tool_path, file_path, property_name, parametersText, Modest().temp_file_path)
        return command

    def generate_parameter_text(self, parameters):
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, parameters[key])
        parametersText = parametersText[:-1]  # Removes last comma.
        return parametersText

    def read_json(self):
        if os.path.exists(Modest().temp_file_path):
            file = open(Modest().temp_file_path, "r", encoding='utf-8-sig')
            json_output = json.load(file)
            self.result.json_output = json_output
            file.close()
            os.remove(Modest().temp_file_path)

            self.result.statistics[Statistics.TOOL_REPORTED_TIME] = json_output["time"]
            state_space_exploration_values = json_output["data"][0]["values"]
            self.result.statistics[Statistics.STATES] = state_space_exploration_values[1]["value"]
            self.result.statistics[Statistics.TRANSITIONS] = state_space_exploration_values[2]["value"]
            self.result.statistics[Statistics.BRANCHES] = state_space_exploration_values[3]["value"]
            self.result.statistics[Statistics.STATE_SPACE_TIME] = state_space_exploration_values[5]["value"]
            self.result.statistics[Statistics.PROPERTY_TIME] = json_output["property-times"][0]["time"]
            self.result.statistics[Statistics.PROPERTY_OUTPUT] = json_output["data"][1]["value"]