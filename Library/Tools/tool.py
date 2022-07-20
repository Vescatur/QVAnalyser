from Library.Results.result import Result
from Library.Tools.result_parser import ResultParser


class Tool(object):

    def __init__(self,parser: ResultParser):
        self.result_parser = parser

    def check_setup_tool(self):
        raise Exception("Unimplemented method Tool.setup_tool()")

    def name(self):
        raise Exception("Unimplemented method Tool.name()")