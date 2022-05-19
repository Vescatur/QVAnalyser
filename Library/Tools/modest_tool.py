from os import path

from Library.Tools.tool import Tool


class ModestTool(Tool):

    def __init__(self):
        self.resourcesPath = "./../Resources"
        self.toolPath = "{}/Tools/Modest/modest.exe".format(self.resourcesPath)

    def generate_commands_interval_iteration(self, filePath, propertyName, parameters):
        commands = [1]
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, parameters[key])
        parametersText = parametersText[:-1]  # Removes last comma.
        commands[0] = "{} check {} --alg IntervalIteration --props {} -E {}"\
            .format(self.toolPath, filePath, propertyName, parametersText)
        # Does not use Interval iteration
        return commands

    def setup_tool(self):
        if not path.exists("./../Resources/Tools/Modest"):
            return False
        if not path.exists("./../Resources/Tools/Modest/modest.exe"):
            return False
        return True

    def name(self):
        return "Modest"