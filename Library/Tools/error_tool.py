from sys import platform


# Used to check whether benchmark.py is resilient.
class ErrorTool(object):

    def setup_tool(self):
        return True

    def name(self):
        return "Error Tool"

    def generate_commands_with_error(self):
        commands = [1]
        commands[0] = "this_command_does_not_exists"
        return commands
