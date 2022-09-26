from Specific.Benchmarks.example_benchmark import ExampleBenchmark
from Specific.Tools.Modest.modest_tool import ModestTool

benchmark = ExampleBenchmark()

benchmark.tools = []
tool = ModestTool()
benchmark.tools.append(tool)
benchmark.algorithms = []
benchmark.algorithms.append(tool.interval_iteration)

benchmark.run()

