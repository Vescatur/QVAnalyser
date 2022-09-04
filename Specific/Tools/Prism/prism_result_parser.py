import re

from Library.Results.measurements import Measurements
from Library.Results.result import Result
from Library.Tools.result_parser import ResultParser


class PrismResultParser(ResultParser):

    def __init__(self):
        pass

    def parse_result(self, result: Result, benchmark):
        if result.not_supported:
            return
        if result.command_results[0].return_code == -9:
            result.threw_error = True
            return
        self.result_in_next_line = False
        self.parse_log(result.command_results[0].output_log, result)
        self.parse_log(result.command_results[0].error_log, result)
        if Measurements.PROPERTY_OUTPUT not in result.measurements:
            if not result.threw_error:
                i = 1
        if Measurements.TRANSITIONS not in result.measurements and Measurements.STATES in result.measurements:
            result.measurements[Measurements.TRANSITIONS] = result.measurements[Measurements.STATES]
        if result.algorithm_name == "Prism confidence interval simulator" \
                or result.algorithm_name == 'Prism asymptotic confidence interval simulator'\
                or result.algorithm_name == 'Prism approximate probabilistic model checking simulator':
            result.measurements[Measurements.STATE_SPACE_TIME] = 0
            result.measurements[Measurements.PROPERTY_TIME] = result.measurements[Measurements.WALL_TIME]
        if result.algorithm_name == 'Prism stochastic games pta' or result.algorithm_name == 'Prism backwards reachability pta':
            result.measurements[Measurements.STATE_SPACE_TIME] = 0

    def parse_log(self,log:str,result):
        for line in log.splitlines():
            self.parse_log_line(line,result)

    def parse_log_line(self, line, result):
        self.parse_line(line, r"Result: (.*) \((.*)\)", result, Measurements.PROPERTY_OUTPUT)
        self.parse_line(line, r"Result \(.*\): (.*)", result, Measurements.PROPERTY_OUTPUT)
        self.parse_line(line, r"Result: ([0123456789.,]+)\s", result, Measurements.PROPERTY_OUTPUT)
        self.parse_line(line, r"Result: ([0123456789.,]+)", result, Measurements.PROPERTY_OUTPUT)
        self.parse_line(line, r"Time for model construction: (.*) seconds", result, Measurements.STATE_SPACE_TIME)
        self.parse_line(line, r"Time for model checking: (.*) seconds", result, Measurements.PROPERTY_TIME)
        self.parse_line(line, r"Model checking completed in (.*) secs.", result, Measurements.PROPERTY_TIME)
        self.parse_line(line, r"States:\s*(\d+)", result, Measurements.STATES)
        self.parse_line(line, r"Transitions:\s*(\d+)", result, Measurements.BRANCHES)
        self.parse_line(line, r"Choices:\s*(\d+)", result, Measurements.TRANSITIONS)
        self.parse_error(line, result)
        if "Warning: Switching to" in line:
            result.not_supported = True
        if line == "Result: true":
            result.measurements[Measurements.PROPERTY_OUTPUT] = 1
        if line == "Result: false":
            result.measurements[Measurements.PROPERTY_OUTPUT] = 0

    def parse_error(self, line, result):
        error = None
        match = re.search(r"Error: (.*)", line)
        if match:
            error = match.group(1)
        match = re.search(r"Exception in thread \"main\" (.*)", line)
        if match:
            error = match.group(1)
        if line == "# A fatal error has been detected by the Java Runtime Environment:":
            error = "Java runtime environment error"
        if error is not None:
            result.threw_error = True
            result.error_text = error

    def parse_line(self, line, regex, result, measurement):
        match = re.search(regex, line)
        if match:
            result.measurements[measurement] = float(match.group(1))