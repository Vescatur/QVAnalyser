

class Result(object):

    def __init__(self):
        self.algorithm = None

        self.command_results = []
        self.timed_out = False
        self.threw_error = False
        self.qva_error = None

        self.statistics = {}

        self.index = None