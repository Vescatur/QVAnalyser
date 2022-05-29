from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Specific.Tools.modest_tool import ModestTool
from Library.execution_old.execution import Execution
from Library.execution_old.execution_sequence import ExecutionSequence


# noinspection DuplicatedCode
class TestBenchmark(Benchmark):
    def __init__(self):
        super().__init__()

        self.add_haddad_monmege_sequence()
        self.add_reentrant_queues_sequence()

        modestTool = ModestTool()
        self.tools.append(modestTool)
        self.add_executions(modestTool)

    # noinspection SpellCheckingInspection
    def add_haddad_monmege_sequence(self):
        model = BenchmarkModel(self,'haddad-monmege.v1.jani')

        sequence = BenchmarkSequence(model,"target",{"p": 0.7})
        for value in range(10,12):
            BenchmarkInstance(sequence, {"N": value})

    def add_reentrant_queues_sequence(self):
        model = BenchmarkModel(self,'reentrant-queues.v3.jani')

        sequence = BenchmarkSequence(model,"PminBothQueuesFullIsOne",{"JOB_TYPES": 3,"TIME_BOUND": 5})
        for value in range(2,3):
            BenchmarkInstance(sequence, {"C_LEFT": value, "C_RIGHT": value})

    def add_executions(self,modestTool):
        for benchmark_sequence in self.benchmark_sequences:
            executions = []
            self.execution_sequences.append(ExecutionSequence(executions, benchmark_sequence.benchmark_model.name))
            for instance in benchmark_sequence.benchmark_instances:
                commands = modestTool.generate_commands_interval_iteration(benchmark_sequence.benchmark_model.file_path, benchmark_sequence.property, instance.all_parameters)
                execution = Execution(commands, len(executions))
                executions.append(execution)
