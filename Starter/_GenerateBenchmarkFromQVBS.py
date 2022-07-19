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

    generate_start(data)
    generate_body(benchmark_path, data)
    generate_end()
    benchmark_file.close()

    save_file_path = "./../Specific/Benchmarks/qvbs_benchmark.py"
    with open(save_file_path, 'w') as save_file:
        save_file.writelines(text)


def generate_start(data):
    add_line("from Library.Benchmarks.benchmark import Benchmark")
    add_line("from Library.Benchmarks.benchmark_model import BenchmarkModel")
    add_line("from Library.Benchmarks.benchmark_sequence import BenchmarkSequence")
    add_line("from Library.Benchmarks.benchmark_instance import BenchmarkInstance")
    add_line("from Specific.Tools.Modest.modest_tool import ModestTool")
    add_line("from Specific.Tools.Storm.storm_tool import StormTool")
    add_line("")
    add_line("# This class has been generated using _GenerateBenchmarkFromQVBS.py")
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


def generate_end():
    add_line(tab)
    add_line(tab + "def add_model(self, file_name_jani,file_name_prism_model,file_name_prism_props,formal_model_type,original_model_format,notes, properties, parameter_settings):")
    add_line(tab * 2 + "model = BenchmarkModel(self, file_name_jani,file_name_prism_model,file_name_prism_props,formal_model_type,original_model_format,notes)")
    add_line(tab * 2 + "for property in properties:")
    add_line(tab * 3 + "for parameters in parameter_settings:")
    add_line(tab * 4 + "sequence = BenchmarkSequence(model, property[0], property[1], parameters)")
    add_line(tab * 4 + "BenchmarkInstance(sequence, {})")
    add_line("")


def generate_body(benchmark_path, data):
    for benchmark_model in data:
        generate_method_for_benchmark_model(benchmark_model, benchmark_path)


def generate_method_for_benchmark_model(benchmark_model, benchmark_path):
    benchmark_model_path = benchmark_path + benchmark_model["path"]
    benchmark_model_file = open(benchmark_model_path + "/index.json")
    benchmark_model_data = json.load(benchmark_model_file)
    path = benchmark_model["path"]
    short_name = benchmark_model["short"]
    model_type = benchmark_model_data["type"]
    original = benchmark_model_data["original"]
    notes = ""
    if "notes" in benchmark_model_data:
        notes = benchmark_model_data["notes"]

    property_argument = generate_property_argument(benchmark_model_data)

    add_line(tab)
    add_line(tab + "def add_" + short_name.replace("-", "_") + "(self):")
    add_line(tab * 2 + "properties = " + property_argument)

    for file in benchmark_model_data["files"]:
        generate_line_for_file(file, model_type, original,notes, path)

def generate_line_for_file(file, model_type, original,notes , path):
    parameters_settings = []
    for parameter_setting_data in file["open-parameter-values"]:
        parameters = {}
        if "values" in parameter_setting_data:
            for parameter in parameter_setting_data["values"]:
                parameters[parameter["name"]] = parameter["value"]
        parameters_settings.append(parameters)

    path_argument = "'" + path + "/" + file["file"] + "'"
    parameter_argument = generate_parameter_argument(parameters_settings)
    prism_model_file = ""
    prism_props_file = ""
    if original == "PRISM":
        prism_model_file = file["original-file"][0]
        prism_props_file = file["original-file"][1]

    add_line(
        tab * 2 + "self.add_model(" + path_argument + ",\"" + prism_props_file + "\",\"" + prism_model_file + "\",\"" + model_type + "\",\"" + original  + "\",\"" + notes + "\", properties, " + parameter_argument + ")")


def generate_parameter_argument(parameters_settings):
    parameter_argument = "["
    for parameters in parameters_settings:
        parameter_argument += "{"
        for key in parameters:
            parameter_argument += "'" + key + "': " + str(parameters[key]) + ", "
        if len(parameters) >= 1:
            parameter_argument = parameter_argument[:-2]
        parameter_argument += "},"
    if len(parameters_settings) == 0:
        parameter_argument += "{}"
    else:
        parameter_argument = parameter_argument[:-1]
    parameter_argument += "]"
    return parameter_argument


def generate_property_argument(benchmark_model_data):
    property_argument = []
    for property_data in benchmark_model_data["properties"]:
        property_argument.append("['" + property_data["name"] + "','" + property_data["type"] + "']")

    property_argument_text = "[" + ", ".join(property_argument) + "]"
    return property_argument_text






start()

# properties
# type
# original
# files
# file name
# values
