from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()

sequence = benchmark.benchmark_sequences[0]
instance = sequence.benchmark_instances[0]

i = 0
for result in instance.results:
    print("_"+str(result.index) + " " + str(i) + " " + result.algorithm_name)
    i = i + 1

