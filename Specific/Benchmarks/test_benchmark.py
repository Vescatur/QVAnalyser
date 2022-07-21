from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Specific.Tools.Modest.modest_tool import ModestTool


# noinspection DuplicatedCode
class TestBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.time_limit = 10

        self.add_haddad_monmege_sequence_target()
        self.add_haddad_monmege_sequence_exp_steps()
        self.add_beb()

        modestTool = ModestTool()
        self.tools.append(modestTool)
        '''self.algorithms.append(modestTool.value_iteration)
        self.algorithms.append(modestTool.interval_iteration)
        self.algorithms.append(modestTool.sequential_interval_iteration)
        self.algorithms.append(modestTool.sound_value_iteration)
        self.algorithms.append(modestTool.optimistic_value_iteration)
        self.algorithms.append(modestTool.linear_programming)
        self.algorithms.append(modestTool.confidence_interval)
        self.algorithms.append(modestTool.okamoto)
        self.algorithms.append(modestTool.adaptive)'''
        self.algorithms.append(modestTool.glrtdp)

    # noinspection SpellCheckingInspection
    def add_haddad_monmege_sequence_target(self):
        model = BenchmarkModel(self, 'dtmc/haddad-monmege/haddad-monmege.jani', "haddad-monmege.prctl", "haddad-monmege.pm", "dtmc",
                       "PRISM", "adversarial example for value iteration")
        sequence = BenchmarkSequence(model, "target", "prob-reach", {"p": 0.7})
        BenchmarkInstance(sequence, {"N": 1})

    def add_haddad_monmege_sequence_exp_steps(self):
        model = BenchmarkModel(self, 'dtmc/haddad-monmege/haddad-monmege.jani', "haddad-monmege.prctl", "haddad-monmege.pm", "dtmc",
                       "PRISM", "adversarial example for value iteration")
        sequence = BenchmarkSequence(model, "exp_steps", "exp-steps", {"p": 0.7})
        BenchmarkInstance(sequence, {"N": 1})

    def add_beb(self):
        model = BenchmarkModel(self, 'mdp/beb/beb.3-4.jani', "", "", "mdp",
                       "Modest", "")
        sequence = BenchmarkSequence(model, 'LineSeized','prob-reach', {"N": 1})
        BenchmarkInstance(sequence, {})