def result_contains_measurement(measurement):
    def filter(result):
        return measurement in result.measurements

    return filter


def result_not_timeout():
    def filter(result):
        return not result.timed_out

    return filter


def result_not_threw_error():
    def filter(result):
        return not result.threw_error

    return filter


def result_is_from_algorithm(algorithm_name):
    def filter(result):
        return result.algorithm_name == algorithm_name

    return filter


def instance_contains_algorithms(algorithm1, algorithm2):
    def filter(instance):
        if get_result_with_algorithm(instance, algorithm1) is None:
            return False
        if get_result_with_algorithm(instance, algorithm2) is None:
            return False
        return True

    return filter


def get_result_with_algorithm(benchmark_instance, algorithm_x):
    for result in benchmark_instance.results:
        if result.algorithm_name == algorithm_x.name:
            return result
    return None

def only_dtmc_and_mdp():
    def filter(sequence):
        if '/mdp/' in sequence.benchmark_model.file_path_jani:
            return True
        if '/dtmc/' in sequence.benchmark_model.file_path_jani:
            return True
        return False

    return filter

