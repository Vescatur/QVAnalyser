from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Results.measurements import Measurements
from Library.Results.result import Result
from Library.Tools.algorithm_with_constructor import AlgorithmWithConstructor


def result_contains_measurement(measurement: Measurements):
    def filter(result):
        return measurement in result.measurements

    return filter


def result_not_timeout():
    def filter(result: Result):
        return not result.timed_out

    return filter


def result_not_threw_error():
    def filter(result: Result):
        return not result.threw_error

    return filter


def result_is_from_algorithm(algorithm_name: str):
    def filter(result: Result):
        return result.algorithm_name == algorithm_name

    return filter


def instance_contains_algorithms(algorithm1: AlgorithmWithConstructor, algorithm2: AlgorithmWithConstructor):
    def filter(instance):
        if get_result_with_algorithm(instance, algorithm1) is None:
            return False
        if get_result_with_algorithm(instance, algorithm2) is None:
            return False
        return True

    return filter


def get_result_with_algorithm(benchmark_instance: BenchmarkInstance, algorithm_x: AlgorithmWithConstructor):
    for result in benchmark_instance.results:
        if result.algorithm_name == algorithm_x.name:
            return result
    return None

def only_dtmc_and_mdp():
    def filter(sequence: BenchmarkSequence):
        if '/mdp/' in sequence.benchmark_model.file_path_jani:
            return True
        if '/dtmc/' in sequence.benchmark_model.file_path_jani:
            return True
        return False

    return filter

