from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Specific.Tools.modest_tool import ModestTool
from Library.execution import Execution
from Library.execution_sequence import ExecutionSequence


# noinspection DuplicatedCode
class TestBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.benchmark_sequences = []
        self.execution_sequences = []

        self.add_hadded_monmege_sequence()
        self.add_reentrant_queues_sequence()

        modestTool = ModestTool()
        self.tools.append(modestTool)
        self.add_executions(modestTool)

    def add_sequence(self, file_name, property, sequence_parameters, instance_parameter_name, instance_parameter_range):
        model = BenchmarkModel(self.benchmark_path+file_name)
        sequence = BenchmarkSequence(model,property,sequence_parameters)
        for value in instance_parameter_range:
            parameters = {instance_parameter_name: value}
            BenchmarkInstance(sequence, parameters)
        self.benchmark_sequences.append(sequence)

    # noinspection SpellCheckingInspection
    def add_hadded_monmege_sequence(self):
        model = BenchmarkModel(self.benchmark_path+'haddad-monmege.v1.jani',"haddad-monmege")

        sequence = BenchmarkSequence(model,"target",{"p": 0.7})
        for value in range(10,12):
            parameters = {"N": value}
            BenchmarkInstance(sequence, parameters)
        self.benchmark_sequences.append(sequence)

    def add_reentrant_queues_sequence(self):
        model = BenchmarkModel(self.benchmark_path+'haddad-monmege.v1.jani',"haddad-monmege")

        sequence = BenchmarkSequence(model,"PminBothQueuesFullIsOne",{"JOB_TYPES": 3,"TIME_BOUND": 5})
        for value in range(2,3):
            parameters = {"C_LEFT": value, "C_RIGHT": value}
            BenchmarkInstance(sequence, parameters)
        self.benchmark_sequences.append(sequence)



    def add_executions(self,modestTool):
        for benchmark_sequence in self.benchmark_sequences:
            executions = []
            self.execution_sequences.append(ExecutionSequence(executions, instance.benchmark_model.))
            for instance in benchmark_sequence.benchmark_instances:
                commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
                execution = Execution(commands, len(executions))
                executions.append(execution)

