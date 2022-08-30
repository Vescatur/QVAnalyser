import re

from Library.Benchmarks.benchmark import Benchmark
from Library.Results.measurements import Measurements
from Library.Tools.result_parser import ResultParser
from Specific.Tools.Modest.modest_algorithm_type import ModestAlgorithmType


class ModestResultParser(ResultParser):


    def parse_result(self, result, benchmark: Benchmark):
        if result.not_supported or result.threw_error or result.timed_out:
            return

        self.search_for_errors(result)
        if result.not_supported or result.threw_error:
            return

        if not hasattr(result, 'json_output'):
            self.no_json_output(result)
        else:
            algorithm = self.get_algorithm_from_name(benchmark, result)
            self.parse_json(algorithm, result)

    def no_json_output(self, result):
        result.threw_error = True
        if len(result.command_results) >= 1:
            if result.command_results[0].return_code == -11:
                result.error_text = "return code -11"
            else:
                error_log = result.command_results[0].error_log
                output_log = result.command_results[0].output_log
                result.error_text = "No json_output\n" + error_log + "\n" + output_log
        else:
            result.error_text = "No command_results"

    def parse_json(self, algorithm, result):
        json_output = result.json_output
        result.measurements[Measurements.TOOL_REPORTED_TIME] = json_output["time"]
        match algorithm.algorithm_type:
            case ModestAlgorithmType.VALUE_ITERATION | ModestAlgorithmType.INTERVAL_ITERATION | \
                 ModestAlgorithmType.SEQUENTIAL_INTERVAL_ITERATION | ModestAlgorithmType.SOUND_VALUE_ITERATION | \
                 ModestAlgorithmType.OPTIMISTIC_VALUE_ITERATION | ModestAlgorithmType.LINEAR_PROGRAMMING | \
                 ModestAlgorithmType.SYMBLICIT_STATE_ELIMINATION:
                self.parse_json_vi(json_output, result)
            case ModestAlgorithmType.CONFIDENCE_INTERVAL | \
                 ModestAlgorithmType.APMC | ModestAlgorithmType.ADAPTIVE:
                pass
            case ModestAlgorithmType.GENERAL_LABELED_REAL_TIME_DYNAMIC_PROGRAMMING:
                pass

    def parse_json_vi(self, json_output, result):
        state_space_exploration_values = json_output["data"][0]["values"]
        result.measurements[Measurements.STATES] = state_space_exploration_values[1]["value"]
        result.measurements[Measurements.TRANSITIONS] = state_space_exploration_values[2]["value"]
        result.measurements[Measurements.BRANCHES] = state_space_exploration_values[3]["value"]
        result.measurements[Measurements.STATE_SPACE_TIME] = state_space_exploration_values[5]["value"]
        if len(json_output["property-times"]) >= 1:
            result.measurements[Measurements.PROPERTY_TIME] = json_output["property-times"][0]["time"]
        property_data = json_output["data"][1]
        # print(property_data)
        if "data" not in property_data:
            pass
        elif property_data["data"][0]["group"] == "Precomputations" and len(property_data["data"]) == 1:
            result.measurements[Measurements.PROPERTY_OUTPUT] = int(property_data["value"])
        elif property_data["data"][0]["group"] == "Precomputations":
            result.measurements[Measurements.PROPERTY_OUTPUT] = property_data["value"]
        else:
            result.measurements[Measurements.PROPERTY_OUTPUT] = json_output["data"][1]["value"]

    def get_algorithm_from_name(self, benchmark, result):
        for algorithm_1 in benchmark.algorithms:
            if algorithm_1.name == result.algorithm_name:
                return algorithm_1
        raise Exception("Could not find algorithm")

    def search_for_errors(self, result):
        if len(result.command_results) == 0:
            result.error_text = "no command_result"
            result.threw_error = True

        self.search_errors_with_query(result, r": error: (.*)\n")
        self.search_errors_with_query(result, r"Error: (.*)\n")
        self.search_errors_with_query(result, r"Unhandled exception. (.*)\n")
        self.search_errors_with_query(result, r"Unhandled exception. (.*)\n")
        self.search_errors_with_error_message(result, "No suitable input formalism found for the given file names")

    def search_errors_with_query(self, result, query):
        for error in re.finditer(query, result.command_results[0].error_log):
            self.process_error(result, error.group(1))
        for error in re.finditer(query, result.command_results[0].output_log):
            self.process_error(result, error.group(1))

    def search_errors_with_error_message(self, result, error_message):
        for error in re.finditer(error_message, result.command_results[0].error_log):
            self.process_error(result, error_message)
        for error in re.finditer(error_message, result.command_results[0].output_log):
            self.process_error(result, error_message)

    def process_error(self,result,error):
        if result.threw_error:
            return

        result.error_text = error
        result.threw_error = True




