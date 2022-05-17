from Library.Benchmarks.benchmark import Benchmark
from Library.Tools.modest_tool import ModestTool
from Library.execution import Execution


class Milestone1Benchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.executions = []
        modestTool = ModestTool()
        self.addHaddedMonmegeExecution(modestTool)

    def addHaddedMonmegeExecution(self, modestTool):
        for size in range(10, 30):
            parameters = {"N": size, "p": 0.7}
            benchmarkFile = './../Resources/BenchmarkModels/haddad-monmege.v1.jani'
            propertyName = "target"
            commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
            execution = Execution(commands)
            self.executions.append(execution)
