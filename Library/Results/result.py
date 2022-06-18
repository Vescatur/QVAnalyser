

class Result(object):

    def __init__(self):
        self.algorithm_name = None
        self.tool_name = None

        self.command_results = []
        self.timed_out = False
        self.threw_error = False
        self.qva_error = None
        self.error_text = None

        self.measurements = {}

        self.index = None
