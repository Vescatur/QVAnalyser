from Library.setup_environment import Setup


class Storm(object):

    def __init__(self):
        self.tool_folder_path = "{}storm/".format(Setup().tools_path)
        self.tool_path = "{}build/bin/storm".format(self.tool_folder_path)