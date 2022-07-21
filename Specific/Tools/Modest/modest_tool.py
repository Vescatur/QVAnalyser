import os
from os import path

from Library.Tools.tool import Tool
from Specific.Tools.Modest.modest_algorithm import ModestAlgorithm
from Specific.Tools.Modest.modest_algorithm_type import ModestAlgorithmType
from Specific.Helpers.modest import Modest
from Specific.Tools.Modest.modest_result_parser import ModestResultParser


class ModestTool(Tool):

    def __init__(self):
        super().__init__(ModestResultParser())
        self.value_iteration = ModestAlgorithm(self, "modest value iteration", ModestAlgorithmType.ValueIteration)
        self.interval_iteration = ModestAlgorithm(self, "modest interval iteration", ModestAlgorithmType.IntervalIteration)
        self.sequential_interval_iteration = ModestAlgorithm(self, "modest sequential interval iteration", ModestAlgorithmType.SequentialIntervalIteration)
        self.sound_value_iteration = ModestAlgorithm(self, "modest sound value iteration", ModestAlgorithmType.SoundValueIteration)
        self.optimistic_value_iteration = ModestAlgorithm(self, "modest optimistic value iteration", ModestAlgorithmType.OptimisticValueIteration)
        self.linear_programming = ModestAlgorithm(self, "modest linear programming", ModestAlgorithmType.LinearProgramming)
        self.confidence_interval = ModestAlgorithm(self, "modest confidence interval", ModestAlgorithmType.ConfidenceInterval)
        self.okamoto = ModestAlgorithm(self, "modest apmc", ModestAlgorithmType.APMC)
        self.adaptive = ModestAlgorithm(self, "modest adaptive", ModestAlgorithmType.Adaptive)
        self.glrtdp = ModestAlgorithm(self, "modest glrtdp", ModestAlgorithmType.GeneralLabeledRealTimeDynamicProgramming)

    def check_setup_tool(self):
        if not path.exists(Modest().tool_folder_path):
            return False
        if not path.exists(Modest().tool_path):
            return False
        if path.exists(Modest().temp_file_path):
            os.remove(Modest().temp_file_path)
        return True

    def name(self):
        return "Modest"
