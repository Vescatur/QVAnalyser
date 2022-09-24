from Library.setup_environment import Setup


class ModestBoundHelper(object):

    def __init__(self):
        self.tool_folder_path = "{}ModestBound/".format(Setup().tools_path)
        self.tool_path = "{}modest".format(self.tool_folder_path)
        self.temp_file_path = "{}temp_output.json".format(self.tool_folder_path)
