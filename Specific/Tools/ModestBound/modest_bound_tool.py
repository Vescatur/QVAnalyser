import os
from os import path

from Library.Tools.tool import Tool
from Specific.Tools.ModestBound.modest_bound_algorithm import ModestBoundAlgorithm
from Specific.Tools.ModestBound.modest_bound_helper import ModestBoundHelper
from Specific.Tools.ModestBound.modest_bound_result_parser import ModestBoundResultParser


class ModestBoundTool(Tool):

    def __init__(self):
        super().__init__(ModestBoundResultParser())
        self.bound = ModestBoundAlgorithm(self, "modest bound")

    def check_setup_tool(self):
        if not path.exists(ModestBoundHelper().tool_folder_path):
            return False
        if not path.exists(ModestBoundHelper().tool_path):
            return False
        if path.exists(ModestBoundHelper().temp_file_path):
            os.remove(ModestBoundHelper().temp_file_path)
        return True

    def name(self):
        return "Bound"