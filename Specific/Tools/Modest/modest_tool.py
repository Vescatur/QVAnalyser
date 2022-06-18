import os
from os import path

from Library.Results.measurements import Measurements
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.Modest.modest_interval_iteration import ModestIntervalIteration
from Specific.Helpers.modest import Modest


class ModestTool(Tool):

    def __init__(self):
        self.interval_iteration = Algorithm(self,ModestIntervalIteration, "modest interval iteration")

    def check_setup_tool(self):
        if not path.exists(Modest().tool_folder_path):
            return False
        if not path.exists(Modest().tool_path):
            return False
        if path.exists(Modest().temp_file_path):
            os.remove(Modest().temp_file_path)
        return True

    def name(self):
        return "Modest"

    def parse_result(self, result):
        if not hasattr(result, 'json_output'):
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
            result.measurements[Measurements.PROPERTY_TIME] = json_output["property-times"][0]["time"]
            result.measurements[Measurements.PROPERTY_OUTPUT] = json_output["data"][1]["value"]