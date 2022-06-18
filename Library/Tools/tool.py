

class Tool(object):

    def check_setup_tool(self):
        raise Exception("Unimplemented method Tool.setup_tool()")

    def name(self):
        raise Exception("Unimplemented method Tool.name()")

    def parse_result(self, result):
        raise Exception("Unimplemented method Tool.parse_result()")