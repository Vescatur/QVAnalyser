from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType
from Specific.Tools.Modest.modest_tool import ModestTool


# noinspection DuplicatedCode
from Specific.Tools.Storm.storm_tool import StormTool


class TestBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        self.time_limit = 10

        self.add_leader_sync_1()
        self.add_embedded_1()
        self.add_resource_gathering_1()
        self.add_csma_1()
        self.add_dpm_1()
        self.add_brp_pta_1()

        '''
        modestTool = ModestTool()
        self.tools.append(modestTool)
        self.algorithms.append(modestTool.value_iteration)
        self.algorithms.append(modestTool.interval_iteration)
        self.algorithms.append(modestTool.sequential_interval_iteration)
        self.algorithms.append(modestTool.sound_value_iteration)
        self.algorithms.append(modestTool.optimistic_value_iteration)
        self.algorithms.append(modestTool.linear_programming)
        self.algorithms.append(modestTool.confidence_interval)
        self.algorithms.append(modestTool.okamoto)
        self.algorithms.append(modestTool.adaptive)
        self.algorithms.append(modestTool.glrtdp)'''
        stormTool = StormTool()
        '''self.algorithms.append(stormTool.top_jacobi)
        self.algorithms.append(stormTool.top_gmm_plus_plus)
        self.algorithms.append(stormTool.top_gauss_seidel)
        self.algorithms.append(stormTool.top_successive_over_relaxation)
        self.algorithms.append(stormTool.top_walkerchae)
        self.algorithms.append(stormTool.top_value_iteration)
        self.algorithms.append(stormTool.top_interval_iteration)
        self.algorithms.append(stormTool.top_sound_value_iteration)
        self.algorithms.append(stormTool.top_optimistic_value_iteration)
        self.algorithms.append(stormTool.top_rational_search)
        self.algorithms.append(stormTool.top_eigen)
        self.algorithms.append(stormTool.top_elimination)
        self.algorithms.append(stormTool.top_policy_iteration)
        self.algorithms.append(stormTool.top_linear_programming)
        self.algorithms.append(stormTool.top_value_iteration_to_policy_iteration)
        self.algorithms.append(stormTool.abstract_refinement)'''
        self.algorithms.append(stormTool.value_iteration_dd)
        self.algorithms.append(stormTool.policy_iteration_dd)
        self.algorithms.append(stormTool.jacobi_dd)
        self.algorithms.append(stormTool.rational_search_dd)
        self.algorithms.append(stormTool.value_iteration_dd_to_sparse)
        self.algorithms.append(stormTool.top_value_iteration_dd_to_sparse)
        self.algorithms.append(stormTool.value_iteration_hybrid)
        self.algorithms.append(stormTool.top_value_iteration_hybrid)


    def add_leader_sync_1(self):
        model = BenchmarkModel(self, "dtmc/leader_sync/leader_sync.3-2.jani","dtmc/leader_sync/leader_sync.props","dtmc/leader_sync/leader_sync.3-2.prism",ModelType.DTMC,"PRISM","PRISM benchmark",)
        sequence = BenchmarkSequence(model, "eventually_elected", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})

    def add_embedded_1(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani", "ctmc/embedded/embedded.props",
                               "ctmc/embedded/embedded.prism", ModelType.CTMC, "PRISM", "PRISM benchmark", )
        sequence = BenchmarkSequence(model, "actuators", PropertyType.REACHABILITY, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "up_time", PropertyType.EXPECTED_REWARD, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})

    def add_resource_gathering_1(self):
        model = BenchmarkModel(self, "mdp/resource-gathering/resource-gathering.jani","mdp/resource-gathering/resource-gathering.prctl","mdp/resource-gathering/resource-gathering.pm",ModelType.MDP,"PRISM","",)
        sequence = BenchmarkSequence(model, "expsteps", PropertyType.EXPECTED_STEPS, {"B": 1000000, "GOLD_TO_COLLECT": 0, "GEM_TO_COLLECT": 0})
        BenchmarkInstance(sequence, {})

    def add_csma_1(self):
        model = BenchmarkModel(self, "mdp/csma/csma.2-2.jani","mdp/csma/csma.props","mdp/csma/csma.2-2.prism",ModelType.MDP,"PRISM","PRISM benchmark",)
        sequence = BenchmarkSequence(model, "all_before_max", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "all_before_min", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "some_before", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})

    def add_dpm_1(self):
        model = BenchmarkModel(self, "ma/dpm/dpm.jani","","",ModelType.MA,"Modest","scalable nondeterministic queueing system",)
        sequence = BenchmarkSequence(model, "PmaxQueue1Full", PropertyType.REACHABILITY, {"N": 4, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TminQueuesFull", PropertyType.EXPECTED_TIME, {"N": 4, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})

    def add_brp_pta_1(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani", "", "", ModelType.PTA, "Modest", "scalable in multiple dimensions",)
        sequence = BenchmarkSequence(model, "T_1", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "Emin", PropertyType.EXPECTED_TIME, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})