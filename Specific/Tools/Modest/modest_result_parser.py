from Library.Results.measurements import Measurements
from Library.Tools.result_parser import ResultParser


class ModestResultParser(ResultParser):

    def parse_result(self, result):
        if not hasattr(result, 'json_output'):
            if not result.timed_out:
                result.threw_error = True
                if result.error_text == None:
                    result.error_text = "No json_output"
        else:
            json_output = result.json_output
            result.measurements[Measurements.TOOL_REPORTED_TIME] = json_output["time"]
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
            elif property_data["data"][0]["group"] == "LongRunAverage":
                result.measurements[Measurements.PROPERTY_TIME] = property_data["values"][0]["value"]
            elif property_data["data"][0]["group"] == "Precomputations" and len(property_data["data"]) == 1:
                result.measurements[Measurements.PROPERTY_OUTPUT] = int(property_data["value"])
            elif property_data["data"][0]["group"] == "Precomputations" and property_data["data"][1]["group"] == "Unif+":
                pass
            elif property_data["data"][0]["group"] == "Precomputations" and property_data["data"][1]["group"] == "Interval iteration" :
                result.measurements[Measurements.PROPERTY_OUTPUT] = property_data["value"]
            elif property_data["data"][0]["group"] == "Precomputations" and property_data["data"][2]["group"] == "Unif+":
                pass
            else:
                result.measurements[Measurements.PROPERTY_OUTPUT] = json_output["data"][1]["value"]