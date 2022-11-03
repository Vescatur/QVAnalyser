
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import average, dendrogram, ward, median, centroid, weighted, leaves_list
import matplotlib.pyplot as plt

from Library.Results.measurements import Measurements
from Library.setup_environment import Setup
from Specific.Output.Matrix.matrix_similar import MatrixSimilar
from Specific.Output.display_name import algorithm_name_to_display_name



class SimilarityClusteringAlgorithms(object):

    def __init__(self, benchmark,instance_filter,algorithms,name):

        similarity_matrix = self.generate_similarity_matrix(benchmark,instance_filter,algorithms)

        clustering = self.generate_clustering(algorithms, similarity_matrix)

        self.generate_figure(clustering, algorithms, name, benchmark, instance_filter)



    def generate_similarity_matrix(self, benchmark, instance_filter, algorithms):
        similarity_matrix = {}
        for algorithm_left in algorithms:
            similarity_matrix[algorithm_left.name] = {}
            for algorithm_top in algorithms:
                metric = self.calculate_similarity_metric(benchmark,instance_filter,algorithm_left,algorithm_top)
                similarity_matrix[algorithm_left.name][algorithm_top.name] = metric
        return similarity_matrix

    def calculate_similarity_metric(self, benchmark,instance_filter, algorithm_left, algorithm_top):
        time_limit = benchmark.time_limit
        total = 0
        differences = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if instance_filter(instance):
                    result_left = self.find_result_with_algorithm(instance, algorithm_left)
                    result_top = self.find_result_with_algorithm(instance, algorithm_top)
                    if not result_left.not_supported and not result_top.not_supported:
                        total += time_limit*2
                        time_left = self.get_time(result_left, time_limit)
                        time_top = self.get_time(result_top, time_limit)
                        differences += abs(time_left-time_top)
        if total <= 3:
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

    def generate_clustering(self, algorithms, similarity_matrix):
        def distance(algorithm_left_name,algorithm_top_name):
            return 1-similarity_matrix[algorithm_left_name[0]][algorithm_top_name[0]]
        data = []
        for i in range(0,len(algorithms)):
            data.append([algorithms[i].name])

        #for algorithm_left in algorithms:
        #    point = []
        #    for algorithm_top in algorithms:
        #        point.append(similarity_matrix[algorithm_left.name][algorithm_top.name])
        #    data.append(point)


        matrix = pdist(data,distance)
        result = ward(matrix)
        return result


    def generate_figure(self, clustering, algorithms, name, benchmark, instance_filer):
        labels = []
        for i in range(0,len(algorithms)):
            labels.append(algorithm_name_to_display_name(algorithms[i].name))
        plt.figure()
        dendrogram(clustering,orientation="left",labels=labels,color_threshold=0.4)
        plt.savefig(Setup().output_path + name + ".png", bbox_inches = "tight",dpi=400)
        plt.close()

        new_algorithms = []
        for i in leaves_list(clustering):
            new_algorithms.append(algorithms[i])

        new_algorithms.reverse()

        MatrixSimilar(benchmark,new_algorithms, instance_filer,True, "Ordered" + name)

