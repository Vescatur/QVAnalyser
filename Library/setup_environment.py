import os
from os import path
from sys import platform


class Setup(object):

    def __init__(self):
        self.resources_path = "./../Resources/"
        self.benchmark_models_path = self.resources_path + "BenchmarkModels/"
        self.tools_path = self.resources_path + "Tools/"
        self.saves_path = self.resources_path + "Saves/"
        self.output_path = self.resources_path + "Output/"

    def setup_tools(self, benchmark):
        missing_tool = False
        missing_tool_name = ""
        for tool in benchmark.tools:
            succes = tool.check_setup_tool()
            if not succes:
                missing_tool_name += tool.name() + " "
                missing_tool = True

        if missing_tool:
            raise Exception("Tool(s) {}is/are missing.".format(missing_tool_name))

    def setup_resource_folders(self):
        self.try_create_directory(self.resources_path)
        self.try_create_directory(self.benchmark_models_path)
        self.try_create_directory(self.tools_path)
        self.try_create_directory(self.saves_path)
        self.try_create_directory(self.output_path)

    def try_create_directory(self, location):
        if not path.exists(location):
            os.mkdir(location)