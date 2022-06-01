# Used to check whether benchmark.py is resilient.
from Library.Algorithms.algorithm import Algorithm
from Library.Algorithms.tool import Tool
from Specific.Algorithms.command_error_algorithm import CommandErrorAlgorithm
from Specific.Algorithms.error_algorithm import ErrorAlgorithm


class ErrorTool(Tool):

    def __init__(self):
        self.error_algorithm = Algorithm(ErrorAlgorithm, "error")
        self.command_error_algorithm = Algorithm(CommandErrorAlgorithm, "command_error")

    def check_setup_tool(self):
        return True

    def name(self):
        return "Error Tool"

