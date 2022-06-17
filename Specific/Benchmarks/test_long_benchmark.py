from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Specific.Tools.Modest.modest_tool import ModestTool


# noinspection DuplicatedCode
class TestLongBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.time_limit = 5
        modestTool = ModestTool()
        self.add_haddad_monmege_sequence()
        self.tools.append(modestTool)
        self.algorithms.append(modestTool.interval_iteration)

    # noinspection SpellCheckingInspection
    def add_haddad_monmege_sequence(self):
        model = BenchmarkModel(self, 'haddad-monmege.v1.jani')

        sequence = BenchmarkSequence(model, "target", {"p": 0.7})
        for value in range(30, 31):
            BenchmarkInstance(sequence, {"N": value})
