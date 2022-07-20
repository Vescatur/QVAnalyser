from Library.Tools.benchmark_result_parser import BenchmarkResultParser
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()
BenchmarkResultParser(benchmark)
storage.save_result_benchmark(benchmark)