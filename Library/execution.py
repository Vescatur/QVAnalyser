import json
import os

from Specific.Tools.modest_tool import ModestTool
from Library.command_execution import CommandExecution


class Execution(object):
    def __init__(self, commands, index):
        self.commands = commands
        self.time_limit = 600
        self.wall_time = None
        self.logs = None
        self.timeout = None
        self.error = None
        self.return_code = None
        self.command_executions = None
        self.index = index
        self.json_output = None
        self.states = 0
        self.total_time = 0
        self.state_space_time = 0
        self.property_time = 0
        self.property_output = 0

    def modest_specific(self):
        if os.path.exists(ModestTool().temp_file_path):
            file = open(ModestTool().temp_file_path, "r", encoding='utf-8-sig')
            self.json_output = json.load(file)
            file.close()
            os.remove(ModestTool().temp_file_path)

            self.total_time = self.json_output["time"]
            state_space_exploration_values = self.json_output["data"][0]["values"]
            self.states = state_space_exploration_values[1]["value"]
            self.state_space_time = state_space_exploration_values[5]["value"]
            self.property_time = self.json_output["property-times"][0]["time"]
            self.property_output = self.json_output["data"][1]

    def run(self):
        self.error = False
        self.timeout = False
        self.wall_time = 0.0
        self.logs = []
        self.return_code = None
        self.command_executions = []
        self.json_output = None
        self.states = 0
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
        self.modest_specific()
