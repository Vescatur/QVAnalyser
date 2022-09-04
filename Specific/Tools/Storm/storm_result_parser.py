from Library.Results.measurements import Measurements
from Library.Results.result import Result
from Library.Tools.result_parser import ResultParser
import re


class StormResultParser(ResultParser):

    def __init__(self):
        self.result_in_next_line = False

    def parse_result(self, result: Result, benchmark):
        if result.not_supported:
            return
        if result.timed_out:
            return
        if result.command_results[0].return_code == -9:
            result.threw_error = True
            result.error_text = "Returned with code -9"
            return
        if result.command_results[0].return_code == -8:
            result.threw_error = True
            result.error_text = "Returned with code -8"
            return
        self.result_in_next_line = False
        log = result.command_results[0].output_log
        status = "start"
        for line in log.splitlines():
            status = self.parse_log_line(line, result, status)
        log = result.command_results[0].error_log
        status = "error"
        for line in log.splitlines():
            status = self.parse_log_line(line, result, status)
        if Measurements.TRANSITIONS not in result.measurements and Measurements.STATES in result.measurements:
            result.measurements[Measurements.TRANSITIONS] = result.measurements[Measurements.STATES]
        if Measurements.BISIMULATION_TIME in result.measurements:
            result.measurements[Measurements.STATE_SPACE_TIME] += result.measurements[Measurements.BISIMULATION_TIME]


    def parse_log_line(self, line, result, status):
        match = re.search(r"Time for model construction", line)
        if match:
            status = "build"
        match = re.search(r"Time for model preprocessing", line)
        if match:
            status = "bisim"
        match = re.search(r"Model checking property", line)
        if match:
            status = "modelchecking"
        self.parse_line_with_status(status, line, "build", r"States:\s*(\d+)", result, Measurements.STATES)
        self.parse_line_with_status(status, line, "build", r"Transitions:\s*(\d+)", result, Measurements.BRANCHES)
        self.parse_line_with_status(status, line, "build", r"Choices:\s*(\d+)", result, Measurements.TRANSITIONS)
        self.parse_line_with_status(status, line, "bisim", r"States:\s*(\d+)", result,
                                    Measurements.STATES_AFTER_BISIMULATION)
        self.parse_line_with_status(status, line, "bisim", r"Transitions:\s*(\d+)", result,
                                    Measurements.BRANCHES_AFTER_BISIMULATION)
        self.parse_line_with_status(status, line, "bisim", r"Choices:\s*(\d+)", result,
                                    Measurements.TRANSITIONS_AFTER_BISIMULATION)
        self.parse_line(line, r"Time for model input parsing: (.*)s", result, Measurements.PARSING_TIME)
        self.parse_line(line, r"Time for model construction: (.*)s", result, Measurements.STATE_SPACE_TIME)
        self.parse_line(line, r"Time for model preprocessing: (.*)s", result, Measurements.BISIMULATION_TIME)
        self.parse_line(line, r"Time for model checking: (.*)s", result, Measurements.PROPERTY_TIME)
        self.parse_line(line, r"Time for model checking: (.*)s", result, Measurements.PROPERTY_TIME)
        self.parse_line(line, r"Time for model checking: (.*)s", result, Measurements.PROPERTY_TIME)
        self.parse_output_property(line, result, Measurements.PROPERTY_OUTPUT)
        self.parse_error(line, result)
        return status

    def parse_error(self, line, result):
        error = None
        if "BDD Unique table full" in line:
            error = "BDD Unique table full"

        match = re.search(r"ERROR (.*)", line)
        if match:
            error = match.group(1)
        match = re.search(r"ERROR: (.*)", line)
        if match:
            error = match.group(1)
        if error is not None:
            if "The selected engine abs is not considered." in error:
                return # Bug in Storm. abs is used.
            if "The selected combination of engine (abs) and model type (" in error:
                return # Bug in Storm. abs is used.

            result.threw_error = True
            result.error_text = error

    def parse_output_property(self, line, result, measurement):
        if self.result_in_next_line:
            self.result_in_next_line = False
            result.measurements[measurement] = line.strip()

        if "Result" in line:
            match = re.search(r"Result (.*): ([0123456789.,]*)", line)
            if match:
                if match.group(2) == "":
                    # Workaround if the result is in the next line
                    self.result_in_next_line = True
                    return

                # Check for exact result
                match_exact = re.search(r"(.*)\/(.*) \(approx. .*\)", match.group(2))
                if match_exact:
                    numerator = float(match_exact.group(1))
                    denominator = float(match_exact.group(2))
                    result.measurements[measurement] = numerator/denominator
                else:
                    result.measurements[measurement] = float(match.group(2))

    def parse_line_with_status(self, status, line, expected_status, regex, result, measurement):
        if status == expected_status:
            match = re.search(regex, line)
            if match:
                result.measurements[measurement] = float(match.group(1))

    def parse_line(self, line, regex, result, measurement):
        match = re.search(regex, line)
        if match:
            result.measurements[measurement] = float(match.group(1))

