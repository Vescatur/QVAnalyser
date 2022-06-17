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
        file_path = benchmark_sequence.benchmark_model.file_path
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

    def parse_statistics(self):
        log = self.result.command_results[0].output_log

        for line in log.splitlines():
            match = re.search(r"Time for model construction", line)
            if match:
                self.status = "build"
            match = re.search(r"Time for model preprocessing", line)
            if match:
                self.status = "bisim"
            match = re.search(r"Model checking property", line)
            if match:
                self.status = "modelchecking"

            states = self.parse_states(line)
            if states is not None:
                self.result.measurements[Measurements.STATES] = states
            branches = self.parse_branches(line)
            if branches is not None:
                self.result.measurements[Measurements.BRANCHES] = branches
            transitions = self.parse_transitions(line)
            if transitions is not None:
                self.result.measurements[Measurements.TRANSITIONS] = transitions

            states_after_bisimulation = self.parse_states_bisimulation(line)
            if states_after_bisimulation is not None:
                self.result.measurements[Measurements.STATES_AFTER_BISIMULATION] = states_after_bisimulation
            branches_after_bisimulation = self.parse_branches_bisimulation(line)
            if branches_after_bisimulation is not None:
                self.result.measurements[Measurements.BRANCHES] = branches_after_bisimulation
            transitions_after_bisimulation = self.parse_transitions_bisimulation(line)
            if transitions_after_bisimulation is not None:
                self.result.measurements[Measurements.TRANSITIONS] = transitions_after_bisimulation

            result = self.parse_result(line)
            if result is not None:
                self.result.measurements[Measurements.PROPERTY_OUTPUT] = result

            parsing_time = self.parse_parsing_time(line)
            if parsing_time is not None:
                self.result.measurements[Measurements.PARSING_TIME] = parsing_time

            building_time = self.parse_building_time(line)
            if building_time is not None:
                self.result.measurements[Measurements.STATE_SPACE_TIME] = building_time

            bisimulation_time = self.parse_bisimulation_time(line)
            if bisimulation_time is not None:
                self.result.measurements[Measurements.BISIMULATION_TIME] = bisimulation_time

            property_time = self.parse_modelchecking_time(line)
            if property_time is not None:
                self.result.measurements[Measurements.PROPERTY_TIME] = property_time

            error = self.parse_error(line)
            if error is not None:
                self.result.threw_error = True


    def parse_error(self, line):
        match = re.search(r"ERROR (.*)", line)
        if match:
            return match.group(1)
        match = re.search(r"ERROR: (.*)", line)
        if match:
            return match.group(1)
        return None

    def parse_result(self, line):
        if self.result_in_next_line:
            self.result_in_next_line = False
            return line.strip()

        match = re.search(r"Result (.*): (.*)", line)
        if match:
            if match.group(2) == "":
                # Workaround if the result is in the next line
                self.result_in_next_line = True
                return None

            # Check for exact result
            match_exact = re.search(r"(.*) \(approx. .*\)", match.group(2))
            if match_exact:
                return match_exact.group(1)
            else:
                return match.group(2)
        return None

    def parse_parsing_time(self, line):
        match = re.search(r"Time for model input parsing: (.*)s", line)
        if match:
            return match.group(1)
        return None

    def parse_building_time(self, line):
        match = re.search(r"Time for model construction: (.*)s", line)
        if match:
            return match.group(1)
        return None

    def parse_bisimulation_time(self, line):
        match = re.search(r"Time for model preprocessing: (.*)s", line)
        if match:
            return match.group(1)
        return None

    def parse_modelchecking_time(self, line):
        match = re.search(r"Time for model checking: (.*)s", line)
        if match:
            return match.group(1)
        return None


    def parse_states(self, line):
        if self.status == "build":
            match = re.search(r"States:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_branches(self, line):
        if self.status == "build":
            match = re.search(r"Transitions:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_transitions(self, line):
        if self.status == "build":
            match = re.search(r"Choices:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_states_bisimulation(self, line):
        if self.status == "bisim":
            match = re.search(r"States:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_branches_bisimulation(self, line):
        if self.status == "bisim":
            match = re.search(r"Transitions:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_transitions_bisimulation(self, line):
        if self.status == "bisim":
            match = re.search(r"Choices:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None
