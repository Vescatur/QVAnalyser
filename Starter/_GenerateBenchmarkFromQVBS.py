import json

tab = "    "



def start():
    benchmark_path = "./../Resources/BenchmarkModels/"
    benchmark_path_file = benchmark_path + "index.json"
    benchmark_file = open(benchmark_path_file)
    data = json.load(benchmark_file)

    print_start(data)
    print_body(benchmark_path, data)
    print_end()

    benchmark_file.close()


def print_start(data):
    print("from Library.Benchmarks.benchmark import Benchmark")
    print("from Library.Benchmarks.benchmark_model import BenchmarkModel")
    print("from Library.Benchmarks.benchmark_sequence import BenchmarkSequence")
    print("from Library.Benchmarks.benchmark_instance import BenchmarkInstance")
    print("from Specific.Tools.modest_tool import ModestTool")
    print("from Specific.Tools.storm_tool import StormTool")
    print("")
    print("")
    print("class QvbsBenchmark(Benchmark):")
    print(tab+"def __init__(self):")
    print(tab*2+"super().__init__()")
    print(tab*2+"")
    print(tab*2+"self.add_benchmark_instances()")
    print(tab*2+"")
    print(tab*2+"stormTool = StormTool()")
    print(tab*2+"self.tools.append(stormTool)")
    print(tab*2+"self.algorithms.append(stormTool.interval_iteration)")
    print(tab*2+"")
    print(tab*2+"modestTool = ModestTool()")
    print(tab*2+"self.tools.append(modestTool)")
    print(tab*2+"self.algorithms.append(modestTool.interval_iteration)")
    print(tab+"")
    print(tab*1+"def add_benchmark_instances(self):")

    for benchmark_model in data:
        short_name = benchmark_model["short"]
        print(tab*2+"self.add_" + short_name.replace("-", "_") + "()")


def print_end():
    print(tab)
    print(tab+"def add_model(self, file_name, properties, parameter_settings):")
    print(tab*2+"model = BenchmarkModel(self, file_name)")
    print(tab*2+"for property_name in properties:")
    print(tab*3+"for parameters in parameter_settings:")
    print(tab*4+"sequence = BenchmarkSequence(model, property_name, parameters)")
    print(tab*4+"BenchmarkInstance(sequence, {})")
    print("")


def print_body(benchmark_path, data):
    for benchmark_model in data:
        benchmark_model_path = benchmark_path + benchmark_model["path"]
        benchmark_model_file = open(benchmark_model_path + "/index.json")
        benchmark_model_data = json.load(benchmark_model_file)
        path = benchmark_model["path"]
        short_name = benchmark_model["short"]
        model_type = benchmark_model_data["type"]
        original = benchmark_model_data["original"]
        name = benchmark_model_data["name"]
        files = read_file_data(benchmark_model_data)
        properties = read_property_data(benchmark_model_data)
        print_benchmark_instances(path, short_name, name, model_type, original, files, properties)


def print_benchmark_instances(path, short_name, name, model_type, original, files, properties):
    print(tab)
    print(tab+"def add_" + short_name.replace("-", "_") + "(self):")
    for file in files:
        path_argument = "''"
        property_argument = "''"
        parameter_argument = "''"
        print(tab*2+"self.add_model("+path_argument+", "+property_argument+", "+parameter_argument+")")



def read_property_data(benchmark_model_data):
    properties = []
    for property_data in benchmark_model_data["properties"]:
        properties.append([property_data["name"], property_data["type"]])
    return properties


def read_file_data(benchmark_model_data):
    files = []
    for file_data in benchmark_model_data["files"]:
        parameters_settings = []
        for parameter_setting_data in file_data["open-parameter-values"]:
            parameters = {}
            if "values" in parameter_setting_data:
                for parameter in parameter_setting_data["values"]:
                    parameters[parameter["name"]] = parameter["value"]
            parameters_settings.append(parameters)
        files.append([file_data["file"], parameters_settings])
    return files





start()

# properties
# type
# original
# files
# file name
# values
