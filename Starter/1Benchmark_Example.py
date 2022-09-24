from Specific.Benchmarks.example_benchmark import ExampleBenchmark
from Specific.Tools.ModestBound.modest_bound_tool import ModestBoundTool

benchmark = ExampleBenchmark()

benchmark.tools = []
tool = ModestBoundTool()
benchmark.tools.append(tool)
benchmark.algorithms = []
benchmark.algorithms.append(tool.bound)

benchmark.run()

