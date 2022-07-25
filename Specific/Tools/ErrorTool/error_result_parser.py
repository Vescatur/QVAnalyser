from Library.Results.measurements import Measurements
from Library.Tools.result_parser import ResultParser


class ErrorResultParser(ResultParser):

    def parse_result(self, result):
        return