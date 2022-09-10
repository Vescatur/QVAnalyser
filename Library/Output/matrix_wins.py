from Library.Output.matrix import Matrix
from Library.Results.measurements import Measurements


class MatrixWins(Matrix):

    def generate_cell_text(self, algorithm_left, algorithm_top):
        wins = 0
        draws = 0
        loss = 0
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if self.instance_filter(instance):
                    result_left = self.find_result_with_algorithm(instance, algorithm_left)
                    result_top = self.find_result_with_algorithm(instance, algorithm_top)
                    if not result_left.not_supported and not result_top.not_supported:
                        if Measurements.WALL_TIME in result_left.measurements and Measurements.WALL_TIME in result_top.measurements:
                            if result_left.measurements[Measurements.WALL_TIME]+1 < result_top.measurements[Measurements.WALL_TIME]:
                                wins += 1
                            elif result_left.measurements[Measurements.WALL_TIME] == result_top.measurements[Measurements.WALL_TIME]:
                                draws += 1
                            elif result_left.measurements[Measurements.WALL_TIME] > result_top.measurements[Measurements.WALL_TIME]+1:
                                loss += 1
                            else:
                                draws += 1
        if wins+loss == 0:
            return "0"
        return str(wins/(wins+loss)).replace(".",",")

