from Library.Benchmarks.benchmark import Benchmark
from Library.Tools.error_tool import ErrorTool
from Library.Tools.modest_tool import ModestTool
from Library.execution import Execution
from Library.execution_sequence import ExecutionSequence


# noinspection DuplicatedCode
class TestErrorBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.execution_sequences = []
        errorTool = ErrorTool()
        self.add_hadded_monmege_execution(errorTool)
        self.tools.append(errorTool)

    # noinspection SpellCheckingInspection
    def add_hadded_monmege_execution(self, modestTool):
        executions = []
        for size in range(30, 33):
            commands = modestTool.generate_commands_with_error()
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "hadded_monmege"))
