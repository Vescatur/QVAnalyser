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
        self.result_in_next_line = False
        self.parse_log(result.command_results[0].output_log, result)
        self.parse_log(result.command_results[0].error_log, result)

    def parse_log(self,log:str,result):
        for line in log.splitlines():
            self.parse_log_line(line,result)

    def parse_log_line(self, line, result):
        self.parse_line(line, r"Result: (.*) \((.*)\)", result, Measurements.PROPERTY_OUTPUT)
        self.parse_line(line, r"Result \(.*\): (.*)", result, Measurements.PROPERTY_OUTPUT)
        self.parse_line(line, r"Time for model construction: (.*) seconds", result, Measurements.STATE_SPACE_TIME)
        self.parse_line(line, r"Time for model checking: (.*) seconds", result, Measurements.PROPERTY_TIME)
        self.parse_line(line, r"States:\s*(\d+)", result, Measurements.STATES)
        self.parse_line(line, r"Transitions:\s*(\d+)", result, Measurements.TRANSITIONS)
        self.parse_error(line, result)

    def parse_error(self, line, result):
        error = None
        match = re.search(r"Error: (.*)", line)
        if match:
            error = match.group(1)
        match = re.search(r"Exception in thread \"main\" (.*)", line)
        if match:
            error = match.group(1)
        if error is not None:
            result.threw_error = True
            result.error_text = error

    def parse_line(self, line, regex, result, measurement):
        match = re.search(regex, line)
        if match:
            result.measurements[measurement] = float(match.group(1))