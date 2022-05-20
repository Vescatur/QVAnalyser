import os
from os import path

from Library.Tools.tool import Tool
from Library.setup_environment import Setup


class ModestTool(Tool):

    def __init__(self):
        self.tool_folder_path = "{}Modest/".format(Setup().tools_path)
        self.tool_path = "{}modest".format(self.tool_folder_path)
        self.temp_file_path = "{}temp_output.json".format(self.tool_folder_path)

    def generate_commands_interval_iteration(self, filePath, propertyName, parameters):
        commands = [1]
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, parameters[key])
        parametersText = parametersText[:-1]  # Removes last comma.
        commands[0] = "{} check {} --alg IntervalIteration --props {} -E {} -O {} Json"\
            .format(self.tool_path, filePath, propertyName, parametersText,self.temp_file_path)
        # Does not use Interval iteration
        return commands

    def setup_tool(self):
        if not path.exists(self.tool_folder_path):
            return False
        if not path.exists(self.tool_path):
            return False
        if path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)
        return True

    def name(self):
        return "Modest"
