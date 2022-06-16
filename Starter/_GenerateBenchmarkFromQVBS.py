import json

tab = "    "
text = ""

def add_line(new_line):
    global text
    text += new_line+"\n"

def start():
    benchmark_path = "./../Resources/BenchmarkModels/"
    benchmark_path_file = benchmark_path + "index.json"
    benchmark_file = open(benchmark_path_file)
    data = json.load(benchmark_file)

    add_line_start(data)
    add_line_body(benchmark_path, data)
    add_line_end()

    print(text)
    benchmark_file.close()

    save_file_path = "./../Specific/Benchmarks/qvbs_benchmark.py"



def add_line_start(data):
    add_line("from Library.Benchmarks.benchmark import Benchmark")
    add_line("from Library.Benchmarks.benchmark_model import BenchmarkModel")
    add_line("from Library.Benchmarks.benchmark_sequence import BenchmarkSequence")
    add_line("from Library.Benchmarks.benchmark_instance import BenchmarkInstance")
    add_line("from Specific.Tools.modest_tool import ModestTool")
    add_line("from Specific.Tools.storm_tool import StormTool")
    add_line("")
    add_line("")
    add_line("class QvbsBenchmark(Benchmark):")
    add_line(tab + "def __init__(self):")
    add_line(tab * 2 + "super().__init__()")
    add_line(tab * 2 + "")
    add_line(tab * 2 + "self.add_benchmark_instances()")
    add_line(tab * 2 + "")
    add_line(tab * 2 + "stormTool = StormTool()")
    add_line(tab * 2 + "self.tools.append(stormTool)")
    add_line(tab * 2 + "self.algorithms.append(stormTool.interval_iteration)")
    add_line(tab * 2 + "")
    add_line(tab * 2 + "modestTool = ModestTool()")
    add_line(tab * 2 + "self.tools.append(modestTool)")
    add_line(tab * 2 + "self.algorithms.append(modestTool.interval_iteration)")
    add_line(tab + "")
    add_line(tab * 1 + "def add_benchmark_instances(self):")

    for benchmark_model in data:
        short_name = benchmark_model["short"]
        add_line(tab * 2 + "self.add_" + short_name.replace("-", "_") + "()")


def add_line_end():
    add_line(tab)
    add_line(tab + "def add_model(self, file_name, properties, parameter_settings):")
    add_line(tab * 2 + "model = BenchmarkModel(self, file_name)")
    add_line(tab * 2 + "for property_name in properties:")
    add_line(tab * 3 + "for parameters in parameter_settings:")
    add_line(tab * 4 + "sequence = BenchmarkSequence(model, property_name, parameters)")
    add_line(tab * 4 + "BenchmarkInstance(sequence, {})")
    add_line("")


def add_line_body(benchmark_path, data):
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
        add_line_benchmark_instances(path, short_name, name, model_type, original, files, properties)


def add_line_benchmark_instances(path, short_name, name, model_type, original, files, properties):
    add_line(tab)
    add_line(tab + "def add_" + short_name.replace("-", "_") + "(self):")

    property_argument = []
    for property_data in properties:
        property_argument.append("'" + property_data[0] + "'")
    property_argument_text = "[" + ", ".join(property_argument) + "]"
    add_line(tab*2 + "properties = "+property_argument_text)

    for file in files:
        path_argument = "'" + path+"/"+ file[0] + "'"

        parameter_argument = "["
        for parameters in file[1]:
            parameter_argument += "{"
            for key in parameters:
                parameter_argument += "'"+key+"': " + str(parameters[key]) + ", "
            if len(parameters) >= 1:
                parameter_argument = parameter_argument[:-2]
            parameter_argument += "},"
        if len(file[1]) ==0:
            parameter_argument += "{}"
        else:
            parameter_argument = parameter_argument[:-1]
        parameter_argument += "]"
        add_line(tab * 2 + "self.add_model(" + path_argument + ", properties, " + parameter_argument + ")")


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
