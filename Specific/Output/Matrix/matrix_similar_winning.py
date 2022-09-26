from Specific.Output.Matrix.algorithm_matrix import AlgorithmMatrix
from Library.Results.measurements import Measurements


class AlgorithmMatrixSimilarWinning(AlgorithmMatrix):

    def generate_cell_text(self, algorithm_left, algorithm_top):
        time_limit = self.benchmark.time_limit
        total = 0
        differences = 0
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if self.instance_filter(instance):
                    result_left = self.find_result_with_algorithm(instance, algorithm_left)
                    result_top = self.find_result_with_algorithm(instance, algorithm_top)
                    if not result_left.not_supported and not result_top.not_supported:
                        total += time_limit*2
                        time_left = time_limit*2
                        if not result_left.not_supported and not result_left.threw_error and not result_left.timed_out:
                            if Measurements.WALL_TIME in result_left.measurements:
                                time_left = result_left.measurements[Measurements.WALL_TIME]
                        time_top = time_limit*2
                        if not result_top.not_supported and not result_top.threw_error and not result_top.timed_out:
                            if Measurements.WALL_TIME in result_top.measurements:
                                time_top = result_top.measurements[Measurements.WALL_TIME]
                        differences = differences + time_left-time_top
        if total == 0:
            return ""
        return str((differences/total)).replace(".",",")

