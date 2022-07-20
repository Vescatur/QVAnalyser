from os import path
import re

from Library.Results.measurements import Measurements
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.Storm.storm_interval_iteration import StormIntervalIteration
from Specific.Helpers.storm import Storm
from Specific.Tools.Storm.storm_result_parser import StormResultParser


class StormTool(Tool):

    def __init__(self):
        super().__init__(StormResultParser())
        self.interval_iteration = Algorithm(self,StormIntervalIteration, "storm interval iteration")
        self.result_in_next_line = False

    def check_setup_tool(self):
        if not path.exists(Storm().tool_folder_path):
            return False
        if not path.exists(Storm().tool_path):
            return False
        return True

    def name(self):
        return "Storm"

