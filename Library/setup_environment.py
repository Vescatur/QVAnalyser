import os
from os import path


class Setup(object):


    def __init__(self):
        self.resources_path = "./../Resources"
        self.tools_path = self.resources_path + "/Tools"
        self.saves_path = self.resources_path + "/Saves"

    def setup_tools(self, benchmark):

        missing_tool = False
        missing_tool_name = ""
        for tool in benchmark.tools:
            succes = tool.setup_tool()
            if not succes:
                missing_tool_name += tool.name() + " "
                missing_tool = True

        if missing_tool:
            raise Exception("Tool(s) {}is/are missing.".format(missing_tool_name))

    def setup_resource_folders(self):
        self.try_create_directory("./../Resources/")
        self.try_create_directory("./../Resources/Saves/")
        self.try_create_directory("./../Resources/Tools/")

    def try_create_directory(self, location):
        if not path.exists(location):
            os.mkdir(location)