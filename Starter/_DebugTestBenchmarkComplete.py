from Library.Tools.benchmark_result_parser import BenchmarkResultParser
from Specific.Benchmarks.test_benchmark import TestBenchmark

benchmark = TestBenchmark()
benchmark.run()
BenchmarkResultParser(benchmark)

