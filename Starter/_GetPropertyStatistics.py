import json

from Specific.Benchmarks.qvbs_benchmark import QvbsBenchmark

def print_properties():
    properties = {}
    properties["dtmc"] = generate_properties()
    properties["mdp"] = generate_properties()
    properties["ctmc"] = generate_properties()
    properties["ma"] = generate_properties()
    properties["pta"] = generate_properties()

    benchmark_path = "./../Resources/BenchmarkModels/"
    benchmark_path_file = benchmark_path + "index.json"
    benchmark_file = open(benchmark_path_file)
    data = json.load(benchmark_file)

    for benchmark_model in data:
        benchmark_model_path = benchmark_path + benchmark_model["path"]
        benchmark_model_file = open(benchmark_model_path + "/index.json")
        benchmark_model_data = json.load(benchmark_model_file)
        model_type = benchmark_model_data["type"]
        for property_data in benchmark_model_data["properties"]:
            properties[model_type][property_data["type"]] += 1


    for key2 in properties["dtmc"]:
        print(key2)

    for key1 in properties:
        print("")
        print(key1)
        for key2 in properties[key1]:
            print(properties[key1][key2])


def generate_properties():
    properties = {}
    properties["exp-reward-step-bounded"] = 0
    properties["exp-steps"] = 0
    properties["prob-reach-reward-bounded"] = 0
    properties["exp-time"] = 0
    properties["prob-reach-step-bounded"] = 0
    properties["steady-state-reward"] = 0
    properties["steady-state-prob"] = 0
    properties["exp-reward-time-instant"] = 0
    properties["exp-reward-time-bounded"] = 0
    properties["prob-reach-time-bounded"] = 0
    properties["exp-reward"] = 0
    properties["prob-reach"] = 0
    return properties

print_properties()