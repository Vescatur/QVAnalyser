import os
import pickle
from os import path

from Library.execution_old.execution_sequence import ExecutionSequence
from Library.setup_environment import Setup


class Storage(object):

    def __init__(self):
        self.save_location = Setup().saves_path
        self.save_index = 0
        while path.exists(self.generate_save_folder_path(self.save_index)):
            self.save_index += 1

    def save_execution(self, execution, execution_sequence):
        self.try_create_directory(self.generate_save_folder_path(self.save_index))
        folder_location = self.generate_sequence_folder_path(self.save_index, execution_sequence.name)
        self.try_create_directory(folder_location)
        file_location = self.generate_execution_path(self.save_index, execution_sequence.name, execution.index)
        with open(file_location, 'wb') as save_file:
            pickle.dump(execution, save_file)

    def load_latest_execution_sequences(self):
        return self.load_execution_sequences(self.save_index - 1)

    def load_execution_sequences(self, save_index):
        execution_sequences = []
        for sequence_name in os.listdir(self.generate_save_folder_path(save_index)):
            executions = []
            counter = 0
            location = self.generate_execution_path(save_index, sequence_name, counter)
            while path.exists(location):
                executions.append(self.load_execution(location))
                counter += 1
                location = self.generate_execution_path(save_index, sequence_name, counter)
            execution_sequences.append(ExecutionSequence(executions, sequence_name))
        return execution_sequences

    def load_execution(self, location):
        with open(location, 'rb') as save_file:
            execution = pickle.load(save_file)
        return execution

    def try_create_directory(self, location):
        if not path.exists(location):
            os.mkdir(location)

    def generate_save_folder_path(self, save_index):
        return self.save_location + str(save_index) + "/"

    def generate_sequence_folder_path(self, save_index, sequence_name):
        return self.generate_save_folder_path(save_index) + sequence_name + "/"

    def generate_execution_path(self, save_index, sequence_name, file_index):
        return self.generate_sequence_folder_path(save_index, sequence_name) + str(file_index) + ".execution"
