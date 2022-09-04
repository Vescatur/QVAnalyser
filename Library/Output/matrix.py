from Library.Results.measurements import Measurements


class Matrix(object):

    def __init__(self, benchmark,algorithms,instance_filter):
        self.benchmark = benchmark
        self.instance_filter = instance_filter
        self.print_top_row(algorithms)
        self.print_body(algorithms)

    def print_top_row(self, algorithms):
        line = "\t"
        for alg in algorithms:
            line += alg.name + "\t"
        print(line)

    def print_body(self, algorithms):
        for alg in algorithms:
            self.print_body_line(algorithms, alg)

    def print_body_line(self, algorithms, algorithm_left):
        line = algorithm_left.name + "\t"
        for algorithm_top in algorithms:
            line += str(self.generate_cell_text(algorithm_left, algorithm_top)) + "\t"
        print(line)

    def generate_cell_text(self, algorithm_left, algorithm_top):
        raise Exception("Unimplemented method Matrix.generate_cell_text()")

    def find_result_with_algorithm(self, instance, algorithm):
        for result in instance.results:
            if result.algorithm_name == algorithm.name:
                return result
