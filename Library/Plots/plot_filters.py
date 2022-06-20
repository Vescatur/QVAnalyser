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