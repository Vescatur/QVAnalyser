from Library.CommandExecution import CommandExecution
from utility import settings

def execute_command_line(command_line_str : str, time_limit : int, short_track : bool):
    """
    Executes the given command line with the given time limit (in seconds).
    :returns the output of the command (including the output to stderr, if present), the runtime of the command and either the return code or None (in case of a timeout)
    """
    execution = CommandExecution()
    execution.run(command_line_str, time_limit, short_track)
    if execution.timeout:
        return execution.output, execution.wall_time, None
    else:
        return execution.output, execution.wall_time, execution.return_code

class Execution(object):
    def __init__(self, invocation):
        self.invocation = invocation
        if(invocation.track_id == "often-epsilon-correct-10-min"):
            self.time_limit = settings.time_limit_short()
        else:
            self.time_limit = settings.time_limit()
        self.wall_time = None
        self.logs = None
        self.timeout = None
        self.error = None
        self.return_code = None

    def run(self):
        self.error = False
        self.timeout = False
        self.wall_time = 0.0
        self.logs = []
        self.return_code = None
        for command in self.invocation.commands:
            log, wall_time, return_code = execute_command_line(command, self.time_limit - self.wall_time, self.invocation.track_id == "often-epsilon-correct-10-min")
            self.wall_time = self.wall_time + wall_time
            self.logs.append("Command:\t{}\nWallclock time:\t{}\nReturn code:\t{}\nOutput:\n{}\n".format(command, wall_time, return_code, log))
            if return_code is None:
                self.timeout = True
                self.logs[-1] = self.logs[-1] + "\n" + "-"*10 + "\nComputation aborted after {} seconds since the total time limit of {} seconds was exceeded.\n".format(self.wall_time, self.time_limit)
                break
            else:
                self.return_code = return_code
                self.error = self.error or return_code != 0

    def concatenate_logs(self):
        hline = "\n" + "#" * 40 + "\n"
        return hline.join(self.logs)