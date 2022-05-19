from Library.Benchmarks.benchmark import Benchmark
from Library.Tools.modest_tool import ModestTool
from Library.execution import Execution
from Library.execution_sequence import ExecutionSequence


# noinspection DuplicatedCode
class TestBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.execution_sequences = []
        modestTool = ModestTool()
        self.add_hadded_monmege_execution(modestTool)
        self.add_reentrant_queues_execution(modestTool)
        self.tools.append(modestTool)

    # noinspection SpellCheckingInspection
    def add_hadded_monmege_execution(self, modestTool):
        executions = []
        for size in range(10, 12):
            parameters = {"N": size, "p": 0.7}
            benchmarkFile = self.benchmark_path+'haddad-monmege.v1.jani'
            propertyName = "target"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "hadded_monmege"))

    def add_reentrant_queues_execution(self, modestTool):
        executions = []
        for size in range(2, 3):
            parameters = {"JOB_TYPES": 3, "C_LEFT": size, "C_RIGHT": size, "TIME_BOUND": 5}
            benchmarkFile = self.benchmark_path+'reentrant-queues.v3.jani'
            propertyName = "PminBothQueuesFullIsOne"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "reentrant_queue"))
