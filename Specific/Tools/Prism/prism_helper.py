from Library.setup_environment import Setup


class PrismHelper(object):

    def __init__(self):
        self.tool_folder_path = "{}prism-4.7-linux64/".format(Setup().tools_path)
        self.tool_path = "{}bin/prism".format(self.tool_folder_path)
