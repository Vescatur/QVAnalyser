from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()

for sequence in benchmark.benchmark_sequences:
    if "resource" in sequence.benchmark_model.name:
        for instance in sequence.benchmark_instances:
             for result in instance.results:
                 if not result.not_supported:
                        i = 1

for algorithms in benchmark.algorithms:
    print("algorithm_to_display_name_array[\"" + algorithms.name+"\"] = \"b\"")