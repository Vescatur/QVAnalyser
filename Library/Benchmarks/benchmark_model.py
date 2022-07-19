class BenchmarkModel(object):

    def __init__(self, benchmark, file_name_jani,file_name_prism_model,file_name_prism_props,formal_model_type,original_model_format,notes):
        self.file_path_jani = benchmark.benchmark_path + file_name_jani
        self.file_name_jani = file_name_jani
        self.file_name_prism_model = file_name_prism_model
        self.file_name_prism_props = file_name_prism_props
        self.formal_model_type = formal_model_type
        self.original_model_format = original_model_format
        self.notes = notes
        self.name = file_name_jani.split(".")[0]
        self.benchmark = benchmark
        benchmark.benchmark_models.append(self)
