import json
import os
import shutil

from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Results.result import Result
from Library.Tools.execution import Execution
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
            case ModestAlgorithmType.VALUE_ITERATION | ModestAlgorithmType.INTERVAL_ITERATION | \
                 ModestAlgorithmType.SOUND_VALUE_ITERATION | ModestAlgorithmType.OPTIMISTIC_VALUE_ITERATION | \
                 ModestAlgorithmType.LINEAR_PROGRAMMING | ModestAlgorithmType.SEQUENTIAL_INTERVAL_ITERATION:
                command = "{} check {} --alg {} --epsilon 1e-6 --width 1e-3 --props {} {} -O {} Json" \
                    .format(Modest().tool_path, file_path, algorithm_name, property_name, parameters_argument, Modest().temp_file_path)
                return command
            case ModestAlgorithmType.APMC | ModestAlgorithmType.CONFIDENCE_INTERVAL | ModestAlgorithmType.ADAPTIVE:
                command = "{} modes {} --statistical {} --max-run-length 0 -C 0.95 --width 1e-3 --props {} {} -O {} Json" \
                    .format(Modest().tool_path, file_path, algorithm_name, property_name, parameters_argument, Modest().temp_file_path)
                return command
            case ModestAlgorithmType.GENERAL_LABELED_REAL_TIME_DYNAMIC_PROGRAMMING:
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
            case ModestAlgorithmType.VALUE_ITERATION:
                return "ValueIteration"
            case ModestAlgorithmType.INTERVAL_ITERATION:
                return "IntervalIteration"
            case ModestAlgorithmType.SEQUENTIAL_INTERVAL_ITERATION:
                return "SequentialIntervalIteration"
            case ModestAlgorithmType.SOUND_VALUE_ITERATION:
                return "SoundValueIteration"
            case ModestAlgorithmType.OPTIMISTIC_VALUE_ITERATION:
                return "OptimisticValueIteration"
            case ModestAlgorithmType.LINEAR_PROGRAMMING:
                return "LinearProgramming"
            case ModestAlgorithmType.CONFIDENCE_INTERVAL:
                return "CI"
            case ModestAlgorithmType.APMC:
                return "Okamoto"
            case ModestAlgorithmType.ADAPTIVE:
                return "Adaptive"
            case ModestAlgorithmType.GENERAL_LABELED_REAL_TIME_DYNAMIC_PROGRAMMING:
                return ""

