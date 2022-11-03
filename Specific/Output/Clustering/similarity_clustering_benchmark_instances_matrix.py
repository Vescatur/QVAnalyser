from Specific.Output.Matrix.matrix_benchmark_instances import MatrixBenchmarkInstances
from Specific.Output.Matrix.text_file_printer import TextFileWriter


class SimilarityClusteringBenchmarkInstancesMatrix(MatrixBenchmarkInstances):

    # noinspection PyMissingConstructor
    def __init__(self, benchmark, instances, name):
        with TextFileWriter(name) as self.writer:
            self.benchmark = benchmark
            self.use_latex = True

            self.instances = instances
            self.print_top_row()
            self.print_body()
            self.print_bottom_row()
