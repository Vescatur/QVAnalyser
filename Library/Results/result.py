

class Result(object):

    def __init__(self):
        self.algorithm = None   # TODO: fill this.

        self.command_results = []
        self.timed_out = False
        self.threw_error = False

        self.statistics = {}
