import math

from Library.Results.measurements import Measurements
from Library.Tools.benchmark_result_parser import BenchmarkResultParser
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_before_result_benchmark()
BenchmarkResultParser(benchmark,True,True)

# Tool does not support reading scientific notation. This is used as a quick fix.
for sequence in benchmark.benchmark_sequences:
    for instance in sequence.benchmark_instances:
         for result in instance.results:
             if Measurements.STATES in result.measurements:
                 if sequence.benchmark_model.name == "mdp/philosophers-mdp/philosophers-mdp":
                    result.measurements[Measurements.STATES] = 6.499124097455577*math.pow(10,29)

# The wrong file name was used.
def shouldAddSequence(sequence):
    fileName = sequence.benchmark_model.file_name_jani
    if fileName == "mdp/rectangle-tireworld/rectangle-tireworld.30.jani":
        return False
    return True

newSequences = []
for sequence in benchmark.benchmark_sequences:
    if shouldAddSequence(sequence):
        newSequences.append(sequence)
benchmark.benchmark_sequences = newSequences


def shouldAddResult(result):
    if result.algorithm_name == "Prism Jacobi with over-relaxation explicit":
        return False
    if result.algorithm_name == "Prism successive over-relaxation explicit":
        return False
    if result.algorithm_name == "Prism backwards successive over-relaxation explicit":
        return False
    return True

for sequence in benchmark.benchmark_sequences:
    for instance in sequence.benchmark_instances:
        newResults = []
        for result in instance.results:
            if shouldAddResult(result):
                newResults.append(result)
        instance.results = newResults


def shouldAddAlgorithm(algorithm):
    if algorithm.name == "Prism Jacobi with over-relaxation explicit":
        return False
    if algorithm.name == "Prism successive over-relaxation explicit":
        return False
    if algorithm.name == "Prism backwards successive over-relaxation explicit":
        return False
    return True


newAlgorithms = []
for algorithm in benchmark.algorithms:
    if shouldAddAlgorithm(algorithm):
        newAlgorithms.append(algorithm)
benchmark.algorithms = newAlgorithms


storage.save_result_benchmark(benchmark)