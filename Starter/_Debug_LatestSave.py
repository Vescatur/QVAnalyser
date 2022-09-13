from Library.storage import Storage
from Library.Results.measurements import Measurements

storage = Storage()
benchmark = storage.load_latest_benchmark()

count = 0
total_time = 0

for sequence in benchmark.benchmark_sequences:
    if "resource" in sequence.benchmark_model.name:
        for instance in sequence.benchmark_instances:
             for result in instance.results:
                 if Measurements.WALL_TIME in result.measurements:
                    count += 1
                    total_time += result.measurements[Measurements.WALL_TIME]
                    if result.threw_error or result.timed_out:
                        print("error")
                        total_time -= result.measurements[Measurements.WALL_TIME]
                        total_time += benchmark.time_limit*2
print(total_time/count)

for algorithms in benchmark.algorithms:
    pass
#   print("algorithm_to_display_name_array[\"" + algorithms.name+"\"] = \"b\"")