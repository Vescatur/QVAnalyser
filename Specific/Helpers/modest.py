from Library.setup_environment import Setup


class Modest(object):

    def __init__(self):
        self.tool_folder_path = "{}Modest/".format(Setup().tools_path)
        if Setup().is_linux():
            self.tool_path = "{}modest".format(self.tool_folder_path)
        else:
            self.tool_path = "{}modest.exe".format(self.tool_folder_path)
        self.temp_file_path = "{}temp_output.json".format(self.tool_folder_path)