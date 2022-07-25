from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType
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
        model = BenchmarkModel(self, "dtmc/haddad-monmege/haddad-monmege.jani","dtmc/haddad-monmege/haddad-monmege.prctl","dtmc/haddad-monmege/haddad-monmege.pm", ModelType.DTMC,"PRISM","adversarial example for value iteration")
        sequence = BenchmarkSequence(model, "target", PropertyType.REACHABILITY, {"N": 100, "p": 0.7})
        BenchmarkInstance(sequence, {})
