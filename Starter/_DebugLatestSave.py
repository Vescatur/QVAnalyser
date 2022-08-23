from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()
i = 1

sequence = benchmark.benchmark_sequences[0]
instance = sequence.benchmark_instances[0]
for result in instance.results:
    print(result.index)
    print(result.algorithm_name)