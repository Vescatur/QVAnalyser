from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Specific.Tools.Modest.modest_tool import ModestTool


# noinspection DuplicatedCode
class TestBenchmark(Benchmark):
    def __init__(self):
        super().__init__()

        self.add_haddad_monmege_sequence_target()
        self.add_haddad_monmege_sequence_exp_steps()

        modestTool = ModestTool()
        self.tools.append(modestTool)
        self.algorithms.append(modestTool.interval_iteration)

    # noinspection SpellCheckingInspection
    def add_haddad_monmege_sequence_target(self):
        model = BenchmarkModel(self, 'dtmc/haddad-monmege/haddad-monmege.jani', "haddad-monmege.prctl", "haddad-monmege.pm", "dtmc",
                       "PRISM", "adversarial example for value iteration")
        sequence = BenchmarkSequence(model, "target","prob-reach", {"p": 0.7})
        BenchmarkInstance(sequence, {"N": 10})

    def add_haddad_monmege_sequence_exp_steps(self):
        model = BenchmarkModel(self, 'dtmc/haddad-monmege/haddad-monmege.jani', "haddad-monmege.prctl", "haddad-monmege.pm", "dtmc",
                       "PRISM", "adversarial example for value iteration")
        sequence = BenchmarkSequence(model, "exp_steps","exp-steps", {"p": 0.7})
        BenchmarkInstance(sequence, {"N": 10})
