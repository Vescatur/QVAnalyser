from Library.Tools.benchmark_result_parser import BenchmarkResultParser
from Library.storage import Storage
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Storm.storm_tool import StormTool

storage = Storage()
benchmark = storage.load_latest_benchmark()
benchmark.tools = []
benchmark.tools.append(StormTool())
benchmark.tools.append(ModestTool())
BenchmarkResultParser(benchmark)
storage.save_result_benchmark(benchmark)