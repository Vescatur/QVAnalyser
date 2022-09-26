from Library.setup_environment import Setup


class TextFileWriter():

    def __init__(self,file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(Setup().output_path+self.file_name+'.txt', 'w')
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def print(self,line):
        self.file.write(line+"\n")
