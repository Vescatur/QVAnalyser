import json
import random

tab = "    "
text = ""

def add_line(new_line):
    global text
    text += new_line+"\n"

def start():
    random.seed(1)
    benchmark_path = "./../Resources/BenchmarkModels/"
    benchmark_path_file = benchmark_path + "index.json"
    benchmark_file = open(benchmark_path_file)
    data = json.load(benchmark_file)

    generate_start(benchmark_path,data)
    generate_body(benchmark_path, data)
    benchmark_file.close()

    save_file_path = "../Specific/Benchmarks/qvbs_benchmark_one_instance_per_property_random.py"
    with open(save_file_path, 'w') as save_file:
        save_file.writelines(text)


def generate_start(benchmark_path,data):
    add_line("from Library.Benchmarks.benchmark import Benchmark")
    add_line("from Library.Benchmarks.benchmark_model import BenchmarkModel")
    add_line("from Library.Benchmarks.benchmark_sequence import BenchmarkSequence")
    add_line("from Library.Benchmarks.benchmark_instance import BenchmarkInstance")
    add_line("from Library.Benchmarks.model_type import ModelType")
    add_line("from Library.Benchmarks.property_type import PropertyType")
    add_line("from Specific.Tools.Modest.modest_tool import ModestTool")
    add_line("from Specific.Tools.Storm.storm_tool import StormTool")
    add_line("")
    add_line("# This class has been generated using _GenerateBenchmarkFromQVBS.py")
    add_line("class QvbsBenchmarkOneInstancePerPropertyRandom(Benchmark):")
    add_line(tab + "def __init__(self):")
    add_line(tab * 2 + "super().__init__()")
    add_line(tab * 2 + "self.time_limit = 10")
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
        benchmark_model_path = benchmark_path + benchmark_model["path"]
        benchmark_model_file = open(benchmark_model_path + "/index.json")
        benchmark_model_data = json.load(benchmark_model_file)
        for property_data in benchmark_model_data["properties"]:
             match property_data["type"]:
                case "exp-reward" | "exp-time" | "exp-reward" | "prob-reach":
                    add_line(tab * 2 + "self.add_" + short_name.replace("-", "_") + "_" + property_data["name"] + "()")


def generate_body(benchmark_path, data):
    for benchmark_model in data:
        generate_code_for_benchmark_model(benchmark_model, benchmark_path)


def generate_code_for_benchmark_model(benchmark_model, benchmark_path):
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

    for property_data in benchmark_model_data["properties"]:
         match property_data["type"]:
            case "exp-reward" | "exp-time" | "exp-reward" | "prob-reach":
                generate_code_for_property(short_name, property_data, model_type, original, notes, path, benchmark_model_data)

def generate_code_for_property(short_name, property_data, model_type, original, notes, path, benchmark_model_data):

    model_type_argument = to_model_type_argument(model_type)

    add_line(tab)
    add_line(tab + "def add_" + short_name.replace("-", "_") + "_" + property_data["name"] + "(self):")

    file = random.choice(benchmark_model_data["files"])

    parameters_settings = []
    for parameter_setting_data in file["open-parameter-values"]:
        parameters = {}
        if "values" in parameter_setting_data:
            for parameter in parameter_setting_data["values"]:
                parameters[parameter["name"]] = parameter["value"]
        parameters_settings.append(parameters)

    jani_file = path + "/" + file["file"]
    prism_model_file = ""
    prism_props_file = ""
    if original == "PRISM":
        prism_model_file = path + "/" + file["original-file"][0]
        prism_props_file = path + "/" + file["original-file"][1]

    add_line(tab * 2 + "model = BenchmarkModel(self, \"" + jani_file + "\",\"" + prism_props_file + "\",\"" + prism_model_file + "\", " + model_type_argument + ",\"" + original + "\",\"" + notes + "\")")

    if len(parameters_settings) == 0:
        parameters_settings = [{}]

    parameters = random.choice(parameters_settings)
    parameter_argument = generate_parameter_argument(parameters)
    property_type_argument = to_property_type_argument(property_data["type"])
    add_line(tab * 2 + "sequence = BenchmarkSequence(model, \"" + property_data["name"] + "\", " + property_type_argument + ", " + parameter_argument + ")")
    add_line(tab * 2 + "BenchmarkInstance(sequence, {})")


def to_property_type_argument(property_type):
    match property_type:
        case "prob-reach":
            return "PropertyType.REACHABILITY"
        case "exp-time":
            return "PropertyType.EXPECTED_TIME"
        case "exp-reward":
            return "PropertyType.EXPECTED_REWARD"
        case "exp-steps":
            return "PropertyType.EXPECTED_STEPS"
    return "PropertyType.UNSUPPORTED"


def to_model_type_argument(model_type):
    match model_type:
        case "dtmc":
            return "ModelType.DTMC"
        case "ctmc":
            return "ModelType.CTMC"
        case "mdp":
            return "ModelType.MDP"
        case "ma":
            return "ModelType.MA"
        case "pta":
            return "ModelType.PTA"

def generate_parameter_argument(parameters):
    parameter_argument = "{"
    for key in parameters:
        parameter_argument += "\"" + key + "\": " + str(parameters[key]) + ", "
    if len(parameters) >= 1:
        parameter_argument = parameter_argument[:-2]
    parameter_argument += "}"
    return parameter_argument


start()

# properties
# type
# original
# files
# file name
# values
