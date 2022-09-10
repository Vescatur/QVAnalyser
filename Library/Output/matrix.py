from Library.Results.measurements import Measurements
from Specific.Output.display_name import algorithm_name_to_display_name


class Matrix(object):

    def __init__(self, benchmark,algorithms,instance_filter,use_latex):
        self.benchmark = benchmark
        self.instance_filter = instance_filter
        self.use_latex = use_latex

        self.print_top_row(algorithms)
        self.print_body(algorithms)
        self.print_bottom_row()

    def print_top_row(self, algorithms):
        if self.use_latex:
            print("\\begin{table}[htbp]")
            print("\centering")
            allignments = "l"*(len(algorithms)+1)
            print("\\begin{tabular}{"+allignments+"}")
            print("\\toprule")
            line = ""
            for alg in algorithms:
                display_name = algorithm_name_to_display_name(alg.name)
                line += "\t& \\fonttopsimilar \\rotatebox{90}{"+display_name + "}"
            print(line + "\\\\")
        else:
            line = "\t"
            for alg in algorithms:
                display_name = algorithm_name_to_display_name(alg.name)
                line += display_name + "\t"
            print(line)

    def print_body(self, algorithms):
        for alg in algorithms:
            self.print_body_line(algorithms, alg)

    def print_body_line(self, algorithms, algorithm_left):
        display_name = algorithm_name_to_display_name(algorithm_left.name)
        if self.use_latex:
            line = display_name
            for algorithm_top in algorithms:
                line += "\t& " + str(self.generate_cell_text(algorithm_left, algorithm_top))
            print(line + " \\\\")
        else:
            line = display_name + "\t"
            for algorithm_top in algorithms:
                line += str(self.generate_cell_text(algorithm_left, algorithm_top)) + "\t"
            print(line)

    def generate_cell_text(self, algorithm_left, algorithm_top):
        raise Exception("Unimplemented method Matrix.generate_cell_text()")

    def find_result_with_algorithm(self, instance, algorithm):
        for result in instance.results:
            if result.algorithm_name == algorithm.name:
                return result

    def print_bottom_row(self):
        if self.use_latex:
            print("\\bottomrule")
            print("\\end{tabular}")
            print("\\caption{??}")
            print("\\label{table:??}")
            print("\\end{table}")




