import math

from Library.Results.measurements import Measurements
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()

for sequence in benchmark.benchmark_sequences:
    for instance in sequence.benchmark_instances:
         for result in instance.results:
             if Measurements.STATES in result.measurements:
                 if sequence.benchmark_model.name == "mdp/philosophers-mdp/philosophers-mdp":
                    print(sequence.benchmark_model.name)
                    print(result.measurements[Measurements.STATES])
                    result.measurements[Measurements.STATES] = 6.499124097455577*math.pow(10,29)


storage.save_result_benchmark(benchmark)