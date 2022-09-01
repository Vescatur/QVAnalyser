from Library.Tools.benchmark_result_parser import BenchmarkResultParser
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_before_result_benchmark()
BenchmarkResultParser(benchmark,True)
storage.save_result_benchmark(benchmark)