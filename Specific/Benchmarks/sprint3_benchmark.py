from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Specific.Tools.modest_tool import ModestTool
from Specific.Tools.storm_tool import StormTool


class Sprint3Benchmark(Benchmark):
    def __init__(self):
        super().__init__()

        self.add_hadded_monmege()
        self.add_zeroconf()
        self.add_reentrant_queues()

        stormTool = StormTool()
        self.tools.append(stormTool)
        self.algorithms.append(stormTool.interval_iteration)

        modestTool = ModestTool()
        self.tools.append(modestTool)
        self.algorithms.append(modestTool.interval_iteration)



    def add_hadded_monmege(self):
        model = BenchmarkModel(self, 'haddad-monmege.v1.jani')

        sequence = BenchmarkSequence(model, "target", {"p": 0.7})
        for value in range(10, 31):
            BenchmarkInstance(sequence, {"N": value})

    def add_reentrant_queues(self):
        model = BenchmarkModel(self, 'reentrant-queues.v3.jani')

        sequence = BenchmarkSequence(model, "PminBothQueuesFullIsOne", {"JOB_TYPES": 3, "TIME_BOUND": 5})
        for size in range(3, 6):
            BenchmarkInstance(sequence, {"C_LEFT": size, "C_RIGHT": size})

        sequence = BenchmarkSequence(model, "TminBothQueuesFull", {"JOB_TYPES": 3, "TIME_BOUND": 5})
        for size in range(3, 6):
            BenchmarkInstance(sequence, {"C_LEFT": size, "C_RIGHT": size})

        sequence = BenchmarkSequence(model, "TmaxBothQueuesFull", {"JOB_TYPES": 3, "TIME_BOUND": 5})
        for size in range(3, 6):
            BenchmarkInstance(sequence, {"C_LEFT": size, "C_RIGHT": size})

        sequence = BenchmarkSequence(model, "PmaxBothQueuesFullBound", {"JOB_TYPES": 3, "TIME_BOUND": 5})
        for size in range(3, 6):
            BenchmarkInstance(sequence, {"C_LEFT": size, "C_RIGHT": size})

        sequence = BenchmarkSequence(model, "SmaxBothQueuesFull", {"JOB_TYPES": 3, "TIME_BOUND": 5})
        for size in range(3, 6):
            BenchmarkInstance(sequence, {"C_LEFT": size, "C_RIGHT": size})

    def add_zeroconf(self):
        model = BenchmarkModel(self, 'zeroconf_dl.v1.jani')

        sequence = BenchmarkSequence(model, "deadline_max", {"N": 1000, "K": 1, "reset": False})
        for deadline in range(10, 210, 10):
            BenchmarkInstance(sequence, {"deadline": deadline})

        sequence = BenchmarkSequence(model, "deadline_max", {"N": 1000, "K": 2, "reset": False})
        for deadline in range(10, 210, 10):
            BenchmarkInstance(sequence, {"deadline": deadline})

        sequence = BenchmarkSequence(model, "deadline_max", {"N": 2000, "K": 1, "reset": False})
        for deadline in range(10, 210, 10):
            BenchmarkInstance(sequence, {"deadline": deadline})
