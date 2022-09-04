from Library.Output.matrix import Matrix
from Library.Results.measurements import Measurements


class MatrixWins(Matrix):

    def generate_cell_text(self, benchmark, algorithm_left, algorithm_top):
        wins = 0
        draws = 0
        loss = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                result_left = self.find_result_with_algorithm(instance, algorithm_left)
                result_top = self.find_result_with_algorithm(instance, algorithm_top)
                if Measurements.WALL_TIME in result_left.measurements and Measurements.WALL_TIME in result_top.measurements:
                    if result_left.measurements[Measurements.WALL_TIME] > result_top.measurements[Measurements.WALL_TIME]:
                        wins += 1
                if Measurements.WALL_TIME in result_left.measurements and Measurements.WALL_TIME in result_top.measurements:
                    if result_left.measurements[Measurements.WALL_TIME] == result_top.measurements[Measurements.WALL_TIME]:
                        draws += 1
                    if result_left.measurements[Measurements.WALL_TIME] < result_top.measurements[Measurements.WALL_TIME]:
                        loss += 1
        if wins+draws+loss == 0:
            return "0"
        return str(wins/(wins+draws+loss)).replace(".",",")

