import os
from os import path

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
