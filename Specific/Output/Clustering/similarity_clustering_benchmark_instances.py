import re

from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import average, dendrogram, ward, median, centroid, weighted, leaves_list
import matplotlib.pyplot as plt

from Library.Results.measurements import Measurements
from Library.setup_environment import Setup
from Specific.Output.Clustering.similarity_clustering_benchmark_instances_matrix import \
    SimilarityClusteringBenchmarkInstancesMatrix
from Specific.Output.Matrix.matrix_similar import MatrixSimilar
from Specific.Output.display_name import algorithm_name_to_display_name



class SimilarityClusteringBenchmarkInstances(object):

    def __init__(self, benchmark,instance_filter,name):

        instances = self.get_instances(benchmark, instance_filter)
        similarity_matrix = self.generate_similarity_matrix(benchmark,instances)

        clustering = self.generate_clustering(instances, similarity_matrix)

        self.generate_figure(clustering, instances, name, benchmark)


    def instance_to_display_name(self,instance):
        benchmark_name = instance.benchmark_sequence.benchmark_model.name
        regex = r"\/[a-zA-Z-_]*"
        match = re.search(regex, benchmark_name)
        short_name1 = match.group(0)
        short_name2 = short_name1[1:] # Removes first character
        display_name = short_name2.replace("_", " ").replace("-", " ")
        property_name = instance.benchmark_sequence.property_name
        return display_name + " " + property_name.replace("_","\_")

    def get_instances(self, benchmark,instance_filter):
        instances = []
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if instance_filter(instance):
                    instances.append(instance)
        return instances

    def generate_similarity_matrix(self, benchmark, instances):
        similarity_matrix = {}
        for instance_left in instances:
            similarity_matrix[self.instance_to_display_name(instance_left)] = {}
            for instance_top in instances:
                metric = self.calculate_similarity_metric(benchmark, instance_left, instance_top)
                similarity_matrix[self.instance_to_display_name(instance_left)][self.instance_to_display_name(instance_top)] = metric
        return similarity_matrix

    def calculate_similarity_metric(self, benchmark, instance_left, instance_top):
        time_limit = benchmark.time_limit
        total = 0
        differences = 0
        for algorithm in benchmark.algorithms:
            if algorithm.name == "Prism Jacobi with over-relaxation explicit" or algorithm.name == "Prism successive over-relaxation explicit" or algorithm.name == "Prism backwards successive over-relaxation explicit":
                continue
            result_left = self.find_result_with_algorithm(instance_left, algorithm)
            result_top = self.find_result_with_algorithm(instance_top, algorithm)
            if not result_left.not_supported and not result_top.not_supported:
                total += time_limit*2
                time_left = time_limit*2
                if not result_left.threw_error and not result_left.timed_out:
                    if Measurements.WALL_TIME in result_left.measurements:
                        time_left = result_left.measurements[Measurements.WALL_TIME]
                time_top = time_limit*2
                if not result_top.threw_error and not result_top.timed_out:
                    if Measurements.WALL_TIME in result_top.measurements:
                        time_top = result_top.measurements[Measurements.WALL_TIME]
                differences += abs(time_left-time_top)
        if total == 0:
            return ""
        similarity_metric = 1-(differences/total)
        return similarity_metric

    def find_result_with_algorithm(self, instance, algorithm):
        for result in instance.results:
            if result.algorithm_name == algorithm.name:
                return result

    def get_time(self, result_top, time_limit):
        time_top = time_limit * 2
        if not result_top.threw_error and not result_top.timed_out:
            if Measurements.WALL_TIME in result_top.measurements:
                time_top = result_top.measurements[Measurements.WALL_TIME]
        return time_top

    def generate_clustering(self, instances, similarity_matrix):
        def distance(instance_left_name,instance_top_name):
            return 1-similarity_matrix[instance_left_name[0]][instance_top_name[0]]
        data = []
        for i in range(0,len(instances)):
            data.append([self.instance_to_display_name(instances[i])])

        matrix = pdist(data,distance)
        result = ward(matrix)
        return result


    def generate_figure(self, clustering, instances, name, benchmark):
        labels = []
        for i in range(0,len(instances)):
            labels.append(self.instance_to_display_name(instances[i]))
        plt.figure()
        dendrogram(clustering,orientation="left",labels=labels,color_threshold=1.2)
        plt.savefig(Setup().output_path + name + ".png", bbox_inches = "tight",dpi=400)
        plt.close()

        new_instances= []
        for i in leaves_list(clustering):
            new_instances.append(instances[i])

        new_instances.reverse()

        SimilarityClusteringBenchmarkInstancesMatrix(benchmark, new_instances, "Ordered" + name)

