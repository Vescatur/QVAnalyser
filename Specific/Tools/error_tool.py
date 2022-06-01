# Used to check whether benchmark.py is resilient.
from Library.Algorithms.algorithm import Algorithm
from Specific.Algorithms.error_algorithm import ErrorAlgorithm


class ErrorTool(object):

    def __init__(self):
        self.error_algorithm = Algorithm(ErrorAlgorithm, "error")

    def setup_tool(self):
        return True

    def name(self):
        return "Error Tool"

