import os
import pickle
from os import path

from Library.setup_environment import Setup


class Storage(object):

    def __init__(self):
        self.save_location = Setup().saves_path
        self.save_index = 0
        while path.exists(self.generate_save_folder_path(self.save_index)):
            self.save_index += 1

    def save_result_benchmark(self, benchmark):
        self.save_benchmark(benchmark, self.generate_results_benchmark_path)

    def save_finished_benchmark(self, benchmark):
        self.save_benchmark(benchmark, self.generate_finished_benchmark_path)

    def save_unfinished_benchmark(self, benchmark):
        benchmark.save_index = self.save_index
        self.save_benchmark(benchmark, self.generate_unfinished_benchmark_path)

    def save_benchmark(self,benchmark, path_generator):
        self.try_create_directory(self.generate_save_folder_path(benchmark.save_index))
        benchmark_path = path_generator(benchmark.save_index)
        with open(benchmark_path, 'wb') as save_file:
            pickle.dump(benchmark, save_file)

    def save_result(self, result, instance):
        self.try_create_directory(self.generate_save_folder_path(self.save_index))
        sequence_folder_path = self.generate_sequence_folder_path(self.save_index, instance.benchmark_sequence)
        self.try_create_directory(sequence_folder_path)
        instance_folder_path = self.generate_instance_folder_path(self.save_index, instance)
        self.try_create_directory(instance_folder_path)

        result_path = self.generate_result_path(self.save_index, instance, result.index)
        with open(result_path, 'wb') as save_file:
            pickle.dump(result, save_file)

    def load_latest_benchmark(self):
        return self.load_benchmark(self.save_index - 1)

    def load_benchmark(self, save_index):
        benchmark_path = self.generate_results_benchmark_path(save_index)
        if not path.exists(benchmark_path):
            benchmark_path = self.generate_finished_benchmark_path(save_index)
        if not path.exists(benchmark_path):
            benchmark_path = self.generate_unfinished_benchmark_path(save_index)

        with open(benchmark_path, 'rb') as save_file:
            benchmark = pickle.load(save_file)
        benchmark.save_index = save_index

        for sequence in benchmark.benchmark_sequences:
            if path.exists(self.generate_sequence_folder_path(save_index, sequence)):
                self.load_sequence(save_index, sequence)

        return benchmark

    def load_sequence(self,save_index, sequence):
        counter = 0
        instance = sequence.benchmark_instances[counter]
        location = self.generate_instance_folder_path(save_index, instance)
        while path.exists(location):
            self.load_results(save_index, instance)
            counter += 1
            location = self.generate_instance_folder_path(save_index, instance)
            if counter < len(sequence.benchmark_instances):
                instance = sequence.benchmark_instances[counter]
            else:
                break

    def load_results(self, save_index, instance):
        counter = 0
        location = self.generate_result_path(save_index, instance, counter)
        while path.exists(location):
            with open(location, 'rb') as save_file:
                result = pickle.load(save_file)
                instance.results.append(result)
            counter += 1
            location = self.generate_result_path(save_index, instance, counter)

    def try_create_directory(self, location):
        if not path.exists(location):
            os.mkdir(location)

    def generate_save_folder_path(self, save_index):
        return self.save_location + str(save_index) + "/"

    def generate_unfinished_benchmark_path(self, save_index):
        return self.generate_save_folder_path(save_index) + "unfinished_benchmark.qva"

    def generate_finished_benchmark_path(self, save_index):
        return self.generate_save_folder_path(save_index) + "finished_benchmark.qva"

    def generate_results_benchmark_path(self, save_index):
        return self.generate_save_folder_path(save_index) + "results_benchmark.qva"

    def generate_sequence_folder_path(self, save_index, benchmark_sequence):
        return self.generate_save_folder_path(save_index) + str(benchmark_sequence.index) + "/"

    def generate_instance_folder_path(self, save_index, instance):
        return self.generate_sequence_folder_path(save_index, instance.benchmark_sequence) + str(instance.index) + "/"

    def generate_result_path(self, save_index, instance, result_index):
        return self.generate_instance_folder_path(save_index, instance) + str(result_index) + ".qva"

