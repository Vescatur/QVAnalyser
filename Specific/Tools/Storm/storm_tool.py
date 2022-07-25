from os import path

from Library.Tools.tool import Tool
from Specific.Tools.Storm.storm_algorithm import StormAlgorithm
from Specific.Tools.Storm.storm_algorithm_type import StormAlgorithmType
from Specific.Tools.Storm.storm_engine_type import StormEngineType
from Specific.Helpers.storm import Storm
from Specific.Tools.Storm.storm_result_parser import StormResultParser


class StormTool(Tool):

    def __init__(self):
        super().__init__(StormResultParser())
        self.value_iteration_dd = StormAlgorithm(self, "storm value iteration dd",
                                                  StormAlgorithmType.VALUE_ITERATION, StormEngineType.DECISION_DIAGRAM,
                                                  False)
        self.policy_iteration_dd = StormAlgorithm(self, "storm policy iteration dd",
                                                  StormAlgorithmType.POLICY_ITERATION, StormEngineType.DECISION_DIAGRAM,
                                                  False)

        self.jacobi_dd = StormAlgorithm(self, "storm jacobi dd",
                                                  StormAlgorithmType.JACOBI, StormEngineType.DECISION_DIAGRAM,
                                                  False)

        self.rational_search_dd = StormAlgorithm(self, "storm rational search dd",
                                                  StormAlgorithmType.RATIONAL_SEARCH, StormEngineType.DECISION_DIAGRAM,
                                                  False)

        self.value_iteration_dd_to_sparse = StormAlgorithm(self, "storm value iteration dd-to-sparse",
                                                  StormAlgorithmType.VALUE_ITERATION, StormEngineType.DECISION_DIAGRAM_TO_SPARSE_MATRICES,
                                                  False)
        self.top_value_iteration_dd_to_sparse = StormAlgorithm(self, "storm topological value iteration dd-to-sparse",
                                                  StormAlgorithmType.VALUE_ITERATION, StormEngineType.DECISION_DIAGRAM_TO_SPARSE_MATRICES,
                                                  True)

        self.value_iteration_hybrid = StormAlgorithm(self, "storm value iteration hybrid",
                                                  StormAlgorithmType.VALUE_ITERATION, StormEngineType.HYBRID,
                                                  False)
        self.top_value_iteration_hybrid = StormAlgorithm(self, "storm topological value iteration hybrid",
                                                  StormAlgorithmType.VALUE_ITERATION, StormEngineType.HYBRID,
                                                  True)

        self.top_jacobi = StormAlgorithm(self, "storm topological jacobi sparse", StormAlgorithmType.JACOBI, StormEngineType.SPARSE_MATRICES, True)
        self.top_gmm_plus_plus = StormAlgorithm(self, "storm topological gmm plus plus sparse", StormAlgorithmType.GMM_PLUS_PLUS, StormEngineType.SPARSE_MATRICES, True)
        self.top_gauss_seidel = StormAlgorithm(self, "storm topological gauss seidel sparse", StormAlgorithmType.GAUSS_SEIDEL, StormEngineType.SPARSE_MATRICES, True)
        self.top_successive_over_relaxation = StormAlgorithm(self, "storm topological successive_over_relaxation  sparse", StormAlgorithmType.SUCCESSIVE_OVER_RELAXATION, StormEngineType.SPARSE_MATRICES, True)
        self.top_walkerchae = StormAlgorithm(self, "storm topological walkerchae sparse", StormAlgorithmType.WALKERCHAE, StormEngineType.SPARSE_MATRICES, True)
        self.top_value_iteration = StormAlgorithm(self, "storm topological value iteration sparse", StormAlgorithmType.VALUE_ITERATION, StormEngineType.SPARSE_MATRICES, True)
        self.top_interval_iteration = StormAlgorithm(self, "storm topological interval iteration sparse", StormAlgorithmType.INTERVAL_ITERATION, StormEngineType.SPARSE_MATRICES, True)
        self.top_sound_value_iteration = StormAlgorithm(self, "storm topological sound_value iteration sparse", StormAlgorithmType.SOUND_VALUE_ITERATION, StormEngineType.SPARSE_MATRICES, True)
        self.top_optimistic_value_iteration = StormAlgorithm(self, "storm topological optimistic value iteration sparse", StormAlgorithmType.OPTIMISTIC_VALUE_ITERATION, StormEngineType.SPARSE_MATRICES, True)
        self.top_rational_search = StormAlgorithm(self, "storm topological rational search sparse", StormAlgorithmType.RATIONAL_SEARCH, StormEngineType.SPARSE_MATRICES, True)
        self.top_eigen = StormAlgorithm(self, "storm topological eigen sparse", StormAlgorithmType.EIGEN, StormEngineType.SPARSE_MATRICES, True)
        self.top_elimination = StormAlgorithm(self, "storm topological elimination sparse", StormAlgorithmType.ELIMINATION, StormEngineType.SPARSE_MATRICES, True)
        self.top_policy_iteration = StormAlgorithm(self, "storm topological policy iteration sparse", StormAlgorithmType.POLICY_ITERATION, StormEngineType.SPARSE_MATRICES, True)
        self.top_linear_programming = StormAlgorithm(self, "storm topological linear programming sparse", StormAlgorithmType.LINEAR_PROGRAMMING, StormEngineType.SPARSE_MATRICES, True)
        self.top_value_iteration_to_policy_iteration = StormAlgorithm(self, "storm topological value iteration to policy iteration sparse", StormAlgorithmType.VALUE_ITERATION_TO_POLICY_ITERATION, StormEngineType.SPARSE_MATRICES, True)

        self.acyclic = StormAlgorithm(self, "storm acyclic sparse", StormAlgorithmType.ACYCLIC, StormEngineType.SPARSE_MATRICES, False)
        # can only handle acyclic models

        self.abstract_refinement = StormAlgorithm(self, "storm abstract refinement", StormAlgorithmType.ABSTRACTION_REFINEMENT, StormEngineType.ABSTRACTION_REFINEMENT, False)
        # self.exploration = StormAlgorithm(self, "storm exploration", StormAlgorithmType.EXPLORATION, StormEngineType.EXPLORATION, False)
        # only for prism files

    def check_setup_tool(self):
        if not path.exists(Storm().tool_folder_path):
            return False
        if not path.exists(Storm().tool_path):
            return False
        return True

    def name(self):
        return "Storm"

