import os
from os import path

from Library.Tools.tool import Tool
from Specific.Tools.Modest.modest_algorithm import ModestAlgorithm
from Specific.Tools.Modest.modest_algorithm_type import ModestAlgorithmType
from Specific.Tools.Modest.modest_helper import ModestHelper
from Specific.Tools.Modest.modest_result_parser import ModestResultParser


class ModestTool(Tool):

    def __init__(self):
        super().__init__(ModestResultParser())
        self.value_iteration = ModestAlgorithm(self, "modest value iteration", ModestAlgorithmType.VALUE_ITERATION)
        self.interval_iteration = ModestAlgorithm(self, "modest interval iteration", ModestAlgorithmType.INTERVAL_ITERATION)
        self.sequential_interval_iteration = ModestAlgorithm(self, "modest sequential interval iteration", ModestAlgorithmType.SEQUENTIAL_INTERVAL_ITERATION)
        self.sound_value_iteration = ModestAlgorithm(self, "modest sound value iteration", ModestAlgorithmType.SOUND_VALUE_ITERATION)
        self.optimistic_value_iteration = ModestAlgorithm(self, "modest optimistic value iteration", ModestAlgorithmType.OPTIMISTIC_VALUE_ITERATION)
        self.linear_programming = ModestAlgorithm(self, "modest linear programming", ModestAlgorithmType.LINEAR_PROGRAMMING)
        self.confidence_interval = ModestAlgorithm(self, "modest confidence interval", ModestAlgorithmType.CONFIDENCE_INTERVAL)
        self.okamoto = ModestAlgorithm(self, "modest apmc", ModestAlgorithmType.APMC)
        self.adaptive = ModestAlgorithm(self, "modest adaptive", ModestAlgorithmType.ADAPTIVE)
        self.glrtdp = ModestAlgorithm(self, "modest glrtdp", ModestAlgorithmType.GENERAL_LABELED_REAL_TIME_DYNAMIC_PROGRAMMING)

    def check_setup_tool(self):
        if not path.exists(ModestHelper().tool_folder_path):
            return False
        if not path.exists(ModestHelper().tool_path):
            return False
        if path.exists(ModestHelper().temp_file_path):
            os.remove(ModestHelper().temp_file_path)
        return True

    def name(self):
        return "Modest"
