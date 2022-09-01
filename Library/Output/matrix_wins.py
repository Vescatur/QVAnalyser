from Library.Results.measurements import Measurements


class MatrixWins(object):

    def __init__(self, benchmark):
        self.print_top_row(benchmark)
        self.print_body(benchmark)

    def print_top_row(self, benchmark):
        line = "\t"
        for alg in benchmark.algorithms:
            line += alg.name + "\t"
        print(line)

    def print_body(self, benchmark):
        for alg in benchmark.algorithms:
            self.print_body_line(benchmark, alg)

    def print_body_line(self, benchmark, algorithm_left):
        line = algorithm_left.name + "\t"
        for algorithm_top in benchmark.algorithms:
            line += str(self.generate_cell_text(benchmark, algorithm_left, algorithm_top)) + "\t"
        print(line)

    def generate_cell_text(self, benchmark, algorithm_left, algorithm_top):
        wins = 0
        draws = 0
        loss = 0
        for sequence in benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                result_left = self.find_result_with_algorithm(instance, algorithm_left)
                result_top = self.find_result_with_algorithm(instance, algorithm_top)
                # if not result_left.not_supported and not result_top.not_supported:
                #    count += 1
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

    def find_result_with_algorithm(self, instance, algorithm):
        for result in instance.results:
            if result.algorithm_name == algorithm.name:
                return result
