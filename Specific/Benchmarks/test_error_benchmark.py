from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType
from Specific.Tools.ErrorTool.error_tool import ErrorTool


# noinspection DuplicatedCode
class TestErrorBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        errorTool = ErrorTool()
        self.add_haddad_monmege_sequence()
        self.tools.append(errorTool)
        self.algorithms.append(errorTool.error_algorithm)

    # noinspection SpellCheckingInspection
    def add_haddad_monmege_sequence(self):
        model = BenchmarkModel(self, "dtmc/leader_sync/leader_sync.3-2.jani","dtmc/leader_sync/leader_sync.props","dtmc/leader_sync/leader_sync.3-2.prism",ModelType.DTMC,"PRISM","PRISM benchmark",)
        sequence = BenchmarkSequence(model, "eventually_elected", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})