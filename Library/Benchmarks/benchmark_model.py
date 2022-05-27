class BenchmarkModel(object):

    def __init__(self, benchmark, file_name):
        self.file_path = benchmark.benchmark_path+file_name
        self.file_name = file_name
        self.name = file_name.split(".")[0]
        self.benchmark = benchmark
        benchmark.benchmark_models.append(self)
