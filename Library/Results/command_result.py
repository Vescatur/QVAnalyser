

class CommandResult(object):

    def __init__(self, command: str):
        self.command = command
        self.timed_out = False
        self.return_code = None
        self.wall_time = None
        self.output_log = ""
        self.error_log = ""
        self.exception = None
