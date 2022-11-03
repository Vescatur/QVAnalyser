import re

from Specific.Benchmarks.qvbs_benchmark_sprint_6 import QvbsBenchmarkSprint6

benchmark = QvbsBenchmarkSprint6()


def generate_parameter_text(parameters):
    parametersText = ""
    for key in parameters:
        parametersText += "{}={}, ".format(key, parameters[key])
    parametersText = parametersText[:-2]  # Removes last comma.
    if parametersText == "":
        return ""
    else:
        return "" + parametersText

print("\\begin{table}[]")
print("\\begin{tabular}{lll}")
print("\\toprule")
print("Model name & Property name & Parameters \\\\")
previousModel = None
for sequence in benchmark.benchmark_sequences:
    for instance in sequence.benchmark_instances:
        parametersText = generate_parameter_text(instance.all_parameters).replace("_","\_")
        if sequence.benchmark_model.name == previousModel:
            print("\t& " + sequence.property_name.replace("_","\_") + "\t& " + parametersText + "\t\\\\")
        else:
            print("\cmidrule(){1-3}")
            benchmark_name = sequence.benchmark_model.name
            regex = r"\/[a-zA-Z-_]*"
            match = re.search(regex, benchmark_name)
            short_name1 = match.group(0)
            short_name2 = short_name1[1:] # Removes first character
            display_name = short_name2.replace("_", " ").replace("-", " ")
            print(display_name + "\t& " + sequence.property_name.replace("_","\_") + "\t& " + parametersText + "\\hspace{1mm}\t\\\\")

        previousModel = sequence.benchmark_model.name

print("\\bottomrule")
print("\\end{tabular}")
print("\\caption{??}")
print("\\label{table:??}")
print("\\end{table}")