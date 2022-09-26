from Library.Results.measurements import Measurements
from Specific.Output.Matrix.text_file_printer import TextFileWriter
from Specific.Output.display_name import algorithm_name_to_display_name


class AlgorithmMatrix(object):

    def __init__(self, benchmark,algorithms,instance_filter,use_latex,name):
        with TextFileWriter(name) as self.writer:
            self.benchmark = benchmark
            self.instance_filter = instance_filter
            self.use_latex = use_latex

            self.print_top_row(algorithms)
            self.print_body(algorithms)
            self.print_bottom_row()

    def print_top_row(self, algorithms):
        if self.use_latex:
            self.writer.print("\\begin{table}[htbp]")
            self.writer.print("\centering")
            allignments = "l"*(len(algorithms)+1)
            self.writer.print("\\begin{tabular}{"+allignments+"}")
            self.writer.print("\\toprule")
            line = ""
            for alg in algorithms:
                display_name = algorithm_name_to_display_name(alg.name)
                line += "\t& \\fonttopsimilar \\rotatebox{90}{"+display_name + "}"
            self.writer.print(line + "\\\\")
        else:
            line = "\t"
            for alg in algorithms:
                display_name = algorithm_name_to_display_name(alg.name)
                line += display_name + "\t"
            self.writer.print(line)

    def print_body(self, algorithms):
        for alg in algorithms:
            self.print_body_line(algorithms, alg)

    def print_body_line(self, algorithms, algorithm_left):
        display_name = algorithm_name_to_display_name(algorithm_left.name)
        if self.use_latex:
            line = display_name
            for algorithm_top in algorithms:
                line += "\t& " + str(self.generate_cell_text(algorithm_left, algorithm_top))
            self.writer.print(line + " \\\\")
        else:
            line = display_name + "\t"
            for algorithm_top in algorithms:
                line += str(self.generate_cell_text(algorithm_left, algorithm_top)) + "\t"
            self.writer.print(line)

    def generate_cell_text(self, algorithm_left, algorithm_top):
        raise Exception("Unimplemented method Matrix.generate_cell_text()")

    def find_result_with_algorithm(self, instance, algorithm):
        for result in instance.results:
            if result.algorithm_name == algorithm.name:
                return result

    def print_bottom_row(self):
        if self.use_latex:
            self.writer.print("\\bottomrule")
            self.writer.print("\\end{tabular}")
            self.writer.print("\\caption{??}")
            self.writer.print("\\label{table:??}")
            self.writer.print("\\end{table}")




