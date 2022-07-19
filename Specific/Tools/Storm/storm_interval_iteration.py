import re

from Library.Tools.execution import Execution
from Library.Results.measurements import Measurements
from Specific.Helpers.storm import Storm


class StormIntervalIteration(Execution):

    def run(self):
        self.result_in_next_line = False
        self.status = "start"
        command = self.generate_command_text()
        self.run_command(command)
        #self.parse_statistics()

    def generate_command_text(self):
        parametersText = self.generate_parameter_text(self.benchmark_instance.all_parameters)
        benchmark_sequence = self.benchmark_instance.benchmark_sequence
        file_path = benchmark_sequence.benchmark_model.file_path_jani
        property_name = benchmark_sequence.property_name
        command = "{} --jani {} --janiproperty {} {} --minmax:method ii --topological:minmax ii --native:method ii --sound --verbose --precision 1e-6" \
            .format(Storm().tool_path, file_path, property_name, parametersText)
        return command

    def generate_parameter_text(self, parameters):
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, str(parameters[key]).lower())
        parametersText = parametersText[:-1]  # Removes last comma.
        if parametersText == "":
            return ""
        else:
            return "--constants " + parametersText
