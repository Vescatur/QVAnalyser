from sys import platform

class Tool(object):

    def setup_tool(self):
        raise Exception("Unimplemented method Tool.setup_tool()")

    def name(self):
        raise Exception("Unimplemented method Tool.name()")

    def isLinux(self):
        if platform == "linux" or platform == "linux2":
            return True
        elif platform == "win32":
            return False
        elif platform == "darwin":
            raise Exception("Apple is not supported")
        raise Exception("Operating system not recognized")