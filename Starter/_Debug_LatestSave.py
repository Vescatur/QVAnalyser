from Library.storage import Storage
from Library.Results.measurements import Measurements

storage = Storage()
benchmark = storage.load_latest_benchmark()

count = 0
total_time = 0

for sequence in benchmark.benchmark_sequences:
    for instance in sequence.benchmark_instances:
        for result in instance.results:
            if result.algorithm_name == "Prism backwards successive over-relaxation explicit":
                i = 1
            if "rectangle" in instance.benchmark_sequence.benchmark_model.file_name_jani:
                i = 1

for algorithm in benchmark.algorithms:
    if algorithm.name == "Prism backwards successive over-relaxation explicit":
        i = 1



for algorithms in benchmark.algorithms:
    pass
#   print("algorithm_to_display_name_array[\"" + algorithms.name+"\"] = \"b\"")