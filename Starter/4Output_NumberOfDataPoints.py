from Library.Results.measurements import Measurements
from Library.storage import Storage
from Specific.Output.display_name import algorithm_name_to_display_name

storage = Storage()
benchmark = storage.load_latest_benchmark()

print("\t Supported \t Threw error \t Timed out \t Finished")


results = {}
for algorithm in benchmark.algorithms:
    results[algorithm.name] = []

for sequence in benchmark.benchmark_sequences:
    for instance in sequence.benchmark_instances:
        for result in instance.results:
            results[result.algorithm_name].append(result)

for algorithm in benchmark.algorithms:
    line = algorithm_name_to_display_name(algorithm.name)
    supported = 0
    error = 0
    time_out = 0
    finished = 0
    for result in results[algorithm.name]:
        if not result.not_supported:
            supported += 1
            if result.threw_error:
                error += 1
            elif result.timed_out:
                time_out += 1
            elif Measurements.PROPERTY_OUTPUT in result.measurements:
                finished += 1
    line += "\t"+ str(supported)
    line += "\t"+ str(error)
    line += "\t"+ str(time_out)
    line += "\t"+ str(finished)
    print(line)