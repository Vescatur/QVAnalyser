from Library.command_execution import CommandExecution


class Execution(object):
    def __init__(self, commands, index):
        self.commands = commands
        self.time_limit = 500
        self.wall_time = None
        self.logs = None
        self.timeout = None
        self.error = None
        self.return_code = None
        self.command_executions = None
        self.index = index

    def run(self):
        self.error = False
        self.timeout = False
        self.wall_time = 0.0
        self.logs = []
        self.return_code = None
        self.command_executions = []
        for command in self.commands:
            command_execution = CommandExecution(command, self.time_limit)
            self.command_executions.append(command_execution)
            command_execution.run()
            self.wall_time = self.wall_time + command_execution.wall_time
            self.logs.append("Command:\t{}\nWallclock time:\t{}\nReturn code:\t{}\nOutput:\n{}\n"
                             .format(command, command_execution.wall_time, command_execution.return_code,
                                     command_execution.output))
            if command_execution.timeout:
                self.timeout = True
                self.logs[-1] = self.logs[
                                    -1] + "\n" + "-" * 10 + "\nComputation aborted after {} seconds since the total time limit of {} seconds was exceeded.\n"\
                    .format(command_execution.wall_time, self.time_limit)
                break
            else:
                self.return_code = command_execution.return_code
                self.error = self.error or command_execution.return_code != 0
