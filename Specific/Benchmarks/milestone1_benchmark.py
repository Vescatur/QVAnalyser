from Library.Benchmarks.benchmark import Benchmark
from Specific.Tools.modest_tool import ModestTool
from QComp.execution_old.execution import Execution
from QComp.execution_old.execution_sequence import ExecutionSequence


class Milestone1Benchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.execution_sequences = []
        modestTool = ModestTool()
        self.add_hadded_monmege_execution(modestTool)
        self.add_reentrant_queues_execution(modestTool)
        self.add_zeroconf_execution(modestTool)
        self.tools.append(modestTool)

    def add_hadded_monmege_execution(self, modestTool):
        executions = []
        for size in range(10, 31):
            parameters = {"N": size, "p": 0.7}
            benchmarkFile = self.benchmark_path+'haddad-monmege.v1.jani'
            propertyName = "target"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "hadded_monmege_target"))

    def add_reentrant_queues_execution(self, modestTool):
        executions = []
        for size in range(3, 6):
            parameters = {"JOB_TYPES": 3, "C_LEFT": size, "C_RIGHT": size, "TIME_BOUND": 5}
            benchmarkFile = self.benchmark_path+'reentrant-queues.v3.jani'
            propertyName = "PminBothQueuesFullIsOne"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "reentrant_queues_PminBothQueuesFullIsOne"))

        executions = []
        for size in range(3, 6):
            parameters = {"JOB_TYPES": 3, "C_LEFT": size, "C_RIGHT": size, "TIME_BOUND": 5}
            benchmarkFile = self.benchmark_path+'reentrant-queues.v3.jani'
            propertyName = "TminBothQueuesFull"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "reentrant_queues_TminBothQueuesFull"))

        executions = []
        for size in range(3, 6):
            parameters = {"JOB_TYPES": 3, "C_LEFT": size, "C_RIGHT": size, "TIME_BOUND": 5}
            benchmarkFile = self.benchmark_path+'reentrant-queues.v3.jani'
            propertyName = "TmaxBothQueuesFull"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "reentrant_queues_TmaxBothQueuesFull"))

        executions = []
        for size in range(3, 6):
            parameters = {"JOB_TYPES": 3, "C_LEFT": size, "C_RIGHT": size, "TIME_BOUND": 5}
            benchmarkFile = self.benchmark_path+'reentrant-queues.v3.jani'
            propertyName = "PmaxBothQueuesFullBound"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "reentrant_queues_TminBothQueuesFull"))

        executions = []
        for size in range(3, 6):
            parameters = {"JOB_TYPES": 3, "C_LEFT": size, "C_RIGHT": size, "TIME_BOUND": 5}
            benchmarkFile = self.benchmark_path+'reentrant-queues.v3.jani'
            propertyName = "SmaxBothQueuesFull"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "reentrant_queues_SmaxBothQueuesFull"))

    def add_zeroconf_execution(self, modestTool):
        executions = []
        for deadline in range(10, 210, 10):
            parameters = {"N": 1000, "K": 1, "reset": False, "deadline": deadline}
            benchmarkFile = self.benchmark_path+'zeroconf_dl.v1.jani'
            propertyName = "deadline_max"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "zeroconf_deadline_max_default"))

        executions = []
        for deadline in range(10, 210, 10):
            parameters = {"N": 1000, "K": 2, "reset": False, "deadline": deadline}
            benchmarkFile = self.benchmark_path+'zeroconf_dl.v1.jani'
            propertyName = "deadline_max"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "zeroconf_deadline_max_K2"))

        executions = []
        for deadline in range(10, 210, 10):
            parameters = {"N": 2000, "K": 1, "reset": False, "deadline": deadline}
            benchmarkFile = self.benchmark_path+'zeroconf_dl.v1.jani'
            propertyName = "deadline_max"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands, len(executions))
            executions.append(execution)
        self.execution_sequences.append(ExecutionSequence(executions, "zeroconf_deadline_max_N2000"))
