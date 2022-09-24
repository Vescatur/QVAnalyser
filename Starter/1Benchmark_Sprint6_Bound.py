from Specific.Benchmarks.qvbs_benchmark_sprint_6 import QvbsBenchmarkSprint6
from Specific.Tools.ModestBound.modest_bound_tool import ModestBoundTool

benchmark = QvbsBenchmarkSprint6()

benchmark.tools = []
tool = ModestBoundTool()
benchmark.tools.append(tool)
benchmark.algorithms = []
benchmark.algorithms.append(tool.bound)

benchmark.run()