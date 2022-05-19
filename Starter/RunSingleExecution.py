from Library.Tools.modest_tool import ModestTool
from Library.execution import Execution

modestTool = ModestTool()
parameters = {"JOB_TYPES": 3, "C_LEFT": 4, "C_RIGHT": 4, "TIME_BOUND": 5}
benchmarkFile = './../Resources/BenchmarkModels/reentrant-queues.v3.jani'
propertyName = "PmaxBothQueuesFullBound"
commands = modestTool.generate_commands_interval_iteration(benchmarkFile, propertyName, parameters)
execution = Execution(commands,0)
execution.run()
print(execution.wall_time)
print(execution.command_executions[0].output)