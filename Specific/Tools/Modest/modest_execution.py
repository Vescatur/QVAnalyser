import json
import os
import shutil

from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.execution import Execution
from Library.Results.measurements import Measurements
from Specific.Helpers.modest import Modest
from Specific.Tools.Modest.modest_algorithm_type import ModestAlgorithmType


class ModestExecution(Execution):

    def __init__(self, instance: BenchmarkInstance, result: Result, algorithm_type: ModestAlgorithmType):
        self.algorithm_type = algorithm_type
        super().__init__(instance, result)

    def run(self):
        command = self.generate_command_text()
        self.run_command(command)
        self.read_json()

    def generate_command_text(self):
        parameters_argument = self.generate_parameter_text(self.benchmark_instance.all_parameters)
        benchmark_sequence = self.benchmark_instance.benchmark_sequence
        file_path = benchmark_sequence.benchmark_model.file_path_jani
        property_name = benchmark_sequence.property_name
        algorithm_name = self.to_command_text(self.algorithm_type)

        match self.algorithm_type:
            case ModestAlgorithmType.ValueIteration | ModestAlgorithmType.IntervalIteration | \
                 ModestAlgorithmType.SoundValueIteration | ModestAlgorithmType.OptimisticValueIteration | \
                 ModestAlgorithmType.LinearProgramming | ModestAlgorithmType.SequentialIntervalIteration:
                command = "{} check {} --alg {} --epsilon 1e-6 --width 1e-3 --props {} {} -O {} Json" \
                    .format(Modest().tool_path, file_path, algorithm_name, property_name, parameters_argument, Modest().temp_file_path)
                return command
            case ModestAlgorithmType.APMC | ModestAlgorithmType.ConfidenceInterval | ModestAlgorithmType.Adaptive:
                command = "{} modes {} --statistical {} --max-run-length 0 -C 0.95 --width 1e-3 --props {} {} -O {} Json" \
                    .format(Modest().tool_path, file_path, algorithm_name, property_name, parameters_argument, Modest().temp_file_path)
                return command
            case ModestAlgorithmType.GeneralLabeledRealTimeDynamicProgramming:
                command = "{} modysh {} --epsilon 1e-6 --props {} {} -O {} Json" \
                    .format(Modest().tool_path, file_path, property_name, parameters_argument, Modest().temp_file_path)
                return command

    def generate_parameter_text(self, parameters):
        parametersText = ""
        for key in parameters:
            parametersText += "{}={},".format(key, parameters[key])
        parametersText = parametersText[:-1]  # Removes last comma.
        if parametersText == "":
            return ""
        else:
            return "-E " + parametersText

    def read_json(self):
        if os.path.exists(Modest().temp_file_path):
            file = open(Modest().temp_file_path, "r", encoding='utf-8-sig')
            json_output = json.load(file)
            self.result.json_output = json_output
            file.close()
            os.remove(Modest().temp_file_path)

    def to_command_text(self,algorithm_type) -> str:
        match algorithm_type:
            case ModestAlgorithmType.ValueIteration:
                return "ValueIteration"
            case ModestAlgorithmType.IntervalIteration:
                return "IntervalIteration"
            case ModestAlgorithmType.SequentialIntervalIteration:
                return "SequentialIntervalIteration"
            case ModestAlgorithmType.SoundValueIteration:
                return "SoundValueIteration"
            case ModestAlgorithmType.OptimisticValueIteration:
                return "OptimisticValueIteration"
            case ModestAlgorithmType.LinearProgramming:
                return "LinearProgramming"
            case ModestAlgorithmType.ConfidenceInterval:
                return "CI"
            case ModestAlgorithmType.APMC:
                return "Okamoto"
            case ModestAlgorithmType.Adaptive:
                return "Adaptive"
            case ModestAlgorithmType.GeneralLabeledRealTimeDynamicProgramming:
                return ""

