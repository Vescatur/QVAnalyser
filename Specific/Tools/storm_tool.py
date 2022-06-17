from os import path

from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Algorithms.storm_interval_iteration import StormIntervalIteration
from Specific.Helpers.storm import Storm


class StormTool(Tool):

    def __init__(self):
        self.interval_iteration = Algorithm(StormIntervalIteration, "storm interval iteration")

    def check_setup_tool(self):
        if not path.exists(Storm().tool_folder_path):
            return False
        if not path.exists(Storm().tool_path):
            return False
        return True

    def name(self):
        return "Storm"
