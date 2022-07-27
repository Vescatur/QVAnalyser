import re

from Library.Benchmarks.benchmark import Benchmark
from Library.Results.measurements import Measurements
from Library.Tools.result_parser import ResultParser
from Specific.Tools.Modest.modest_algorithm_type import ModestAlgorithmType


class ModestResultParser(ResultParser):


    def parse_result(self, result, benchmark: Benchmark):
        self.search_for_errors(result)
        if not hasattr(result, 'json_output'):
            if not result.timed_out:
                result.threw_error = True
                if len(result.command_results) >=1:
                    if result.command_results[0].return_code == -11:
                        result.error_text = "return code -11"
                if result.error_text is None:
                    result.error_text = "No json_output"
        else:
            algorithm = self.get_algorithm_from_name(benchmark, result)
            if algorithm == None:
                raise Exception("Could not find algorithm")
            if result.threw_error:
                return
            self.parse_json(algorithm, result)

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
        print(property_data)
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

    def search_for_errors(self, result):
        if result.not_supported or result.threw_error:
            return

        if len(result.command_results) == 0:
            result.error_text = "no command_result"
            result.threw_error = True

        match = re.search(r": error: (.*)\n", result.command_results[0].error_log)
        if match:
            result.error_text = match.group(1)
            result.threw_error = True
            return

        match = re.search(r": error: (.*)\n", result.command_results[0].output_log)
        if match:
            result.error_text = match.group(1)
            result.threw_error = True
            return


