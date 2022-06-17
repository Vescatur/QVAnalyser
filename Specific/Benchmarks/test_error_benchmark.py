from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Specific.Tools.ErrorTool.error_tool import ErrorTool


# noinspection DuplicatedCode
class TestErrorBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        errorTool = ErrorTool()
        self.add_haddad_monmege_sequence()
        self.tools.append(errorTool)
        self.algorithms.append(errorTool.error_algorithm)
        self.algorithms.append(errorTool.command_error_algorithm)

    # noinspection SpellCheckingInspection
    def add_haddad_monmege_sequence(self):
        model = BenchmarkModel(self, 'haddad-monmege.v1.jani')

        sequence = BenchmarkSequence(model, "target", {"p": 0.7})
        for value in range(10, 12):
            BenchmarkInstance(sequence, {"N": value})