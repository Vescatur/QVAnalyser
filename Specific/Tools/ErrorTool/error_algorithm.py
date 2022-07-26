from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.algorithm import Algorithm


class ErrorAlgorithm(Algorithm):

    def is_supported(self, instance: BenchmarkInstance):
        return True

    def protected_run(self, instance: BenchmarkInstance, result: Result) -> Result:
        raise Exception("This is error algorithm")

