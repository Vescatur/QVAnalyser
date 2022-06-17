
from Library.Tools.execution import Execution


class ErrorAlgorithm(Execution):

    def run(self):
        raise Exception("This is error algorithm")

