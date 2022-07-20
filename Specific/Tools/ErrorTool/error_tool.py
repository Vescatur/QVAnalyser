# Used to check whether benchmark.py is resilient.
from Library.Tools.algorithm import Algorithm
from Library.Tools.tool import Tool
from Specific.Tools.ErrorTool.command_error_algorithm import CommandErrorAlgorithm
from Specific.Tools.ErrorTool.error_algorithm import ErrorAlgorithm
from Specific.Tools.ErrorTool.error_result_parser import ErrorResultParser


class ErrorTool(Tool):

    def __init__(self):
        super().__init__(ErrorResultParser())
        self.error_algorithm = Algorithm(self,ErrorAlgorithm, "error")
        self.command_error_algorithm = Algorithm(self,CommandErrorAlgorithm, "command_error")

    def check_setup_tool(self):
        return True

    def name(self):
        return "Error Tool"

