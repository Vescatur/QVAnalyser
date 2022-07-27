from os import path

from Library.Tools.tool import Tool
from Library.setup_environment import Setup
from Specific.Tools.Prism.prism_algorithm import PrismAlgorithm
from Specific.Tools.Prism.prism_algorithm_type import PrismAlgorithmType
from Specific.Tools.Prism.prism_engine_type import PrismEngineType
from Specific.Tools.Prism.prism_helper import PrismHelper
from Specific.Tools.Prism.prism_result_parser import PrismResultParser


class PrismTool(Tool):

    def __init__(self):
        super().__init__(PrismResultParser())
        self.tool_folder_path = "{}prism-4.7-linux64/".format(Setup().tools_path)
        self.tool_path = "{}bin/prism".format(self.tool_folder_path)
        self.add_algorithms()

    def check_setup_tool(self):
        if not path.exists(PrismHelper().tool_folder_path):
            return False
        if not path.exists(PrismHelper().tool_path):
            return False
        return True

    def name(self):
        return "Prism"

    def add_algorithms(self):
        self.value_iteration_sparse = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.SPARSE_MATRICES, False)
        self.top_value_iteration_sparse = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.SPARSE_MATRICES, True)
        self.value_iteration_explicit = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.EXPLICIT, False)
        self.top_value_iteration_explicit = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.EXPLICIT, True)
        self.value_iteration_hybrid = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.HYBRID, False)
        self.top_value_iteration_hybrid = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.HYBRID, True)
        self.value_iteration_mtbddd = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.MT_BINARY_DECISION_DIAGRAM, False)
        self.top_value_iteration_mtbddd = PrismAlgorithm(self, PrismAlgorithmType.VALUE_ITERATION, PrismEngineType.MT_BINARY_DECISION_DIAGRAM, True)

        self.jacobi_explicit = PrismAlgorithm(self, PrismAlgorithmType.JACOBI, PrismEngineType.EXPLICIT, False)
        self.gauss_seidel_explicit = PrismAlgorithm(self, PrismAlgorithmType.GAUSS_SEIDEL, PrismEngineType.EXPLICIT, False)
        self.backwards_gauss_seidel_explicit = PrismAlgorithm(self, PrismAlgorithmType.BACKWARDS_GAUSS_SEIDEL, PrismEngineType.EXPLICIT, False)
        self.jacobi_with_over_relaxation_explicit = PrismAlgorithm(self, PrismAlgorithmType.JACOBI_WITH_OVER_RELAXATION, PrismEngineType.EXPLICIT, False)
        self.succesive_over_relaxation_explicit = PrismAlgorithm(self, PrismAlgorithmType.SUCCESSIVE_OVER_RELAXATION, PrismEngineType.EXPLICIT, False)
        self.backwards_succesive_over_relaxation_explicit = PrismAlgorithm(self, PrismAlgorithmType.BACKWARDS_SUCCESSIVE_OVER_RELAXATION, PrismEngineType.EXPLICIT, False)

        self.confidence_interval = PrismAlgorithm(self, PrismAlgorithmType.CONFIDENCE_INTERVAL, PrismEngineType.SIMULATOR, False)
        self.asymptotic_confidence_interval = PrismAlgorithm(self, PrismAlgorithmType.ASYMPTOTIC_CONFIDENCE_INTERVAL, PrismEngineType.SIMULATOR, False)
        self.apmc = PrismAlgorithm(self, PrismAlgorithmType.APPROXIMATE_PROBABILISTIC_MODEL_CHECKING, PrismEngineType.SIMULATOR, False)

        self.policy_iteration_explicit = PrismAlgorithm(self, PrismAlgorithmType.POLICY_ITERATION, PrismEngineType.EXPLICIT, False)
        self.modified_policy_iteration_explicit = PrismAlgorithm(self, PrismAlgorithmType.MODIFIED_POLICY_ITERATION, PrismEngineType.EXPLICIT, False)

        self.stochastic_games = PrismAlgorithm(self, PrismAlgorithmType.STOCHASTIC_GAMES, PrismEngineType.PTA, False)
        self.digital_clocks = PrismAlgorithm(self, PrismAlgorithmType.DIGITAL_CLOCKS, PrismEngineType.PTA, False)
        self.backwards_reachability = PrismAlgorithm(self, PrismAlgorithmType.BACKWARDS_REACHABILITY, PrismEngineType.PTA, False)
