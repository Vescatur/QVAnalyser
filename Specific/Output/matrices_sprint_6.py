from Library.Output.matrix_benchmark_instances import MatrixBenchmarkInstances
from Library.Output.matrix_similiar import MatrixSimiliar
from Library.Output.matrix_wins import MatrixWins
from Library.Output.plot_filters import only_dtmc_and_ctmc, only_mdp_and_ma, only_pta, only_ma, only_mdp_reward, \
    only_mdp_reachability
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Prism.prism_tool import PrismTool
from Specific.Tools.Storm.storm_tool import StormTool


class MatrixSprint6(object):

    def __init__(self, benchmark):
        stormTool = StormTool()
        modestTool = ModestTool()
        prismTool = PrismTool()

        algorithms_markov_chains = self.algorithms_for_markov_chains(modestTool, prismTool, stormTool)
        algorithms_mdp_ma = self.algorithms_for_mdp_and_ma(modestTool, prismTool, stormTool)
        algorithms_pta = self.algorithms_for_pta(modestTool, prismTool, stormTool)


        #MatrixSimiliar(benchmark, algorithms_markov_chains, only_dtmc_and_ctmc(),True)
        #MatrixSimiliar(benchmark, algorithms_mdp_ma, only_mdp_and_ma(),True)
        #MatrixSimiliar(benchmark, algorithms_pta, only_pta(),True)
        #MatrixWins(benchmark, algorithms_markov_chains, only_dtmc_and_ctmc(),True)

        MatrixBenchmarkInstances(benchmark,only_dtmc_and_ctmc(),True)
        #MatrixBenchmarkInstances(benchmark,only_mdp_reward(),True)
        #MatrixBenchmarkInstances(benchmark,only_mdp_reachability(),True)
        #MatrixBenchmarkInstances(benchmark,only_ma(),True)
        #MatrixBenchmarkInstances(benchmark,only_pta(),True)


    def algorithms_for_pta(self, modestTool, prismTool, stormTool):
        algorithms = []
        algorithms.append(prismTool.backwards_reachability)
        algorithms.append(prismTool.stochastic_games)
        algorithms.append(prismTool.digital_clocks)

        algorithms.append(modestTool.value_iteration)
        algorithms.append(modestTool.interval_iteration)
        algorithms.append(modestTool.sequential_interval_iteration)
        algorithms.append(modestTool.sound_value_iteration)
        algorithms.append(modestTool.optimistic_value_iteration)
        algorithms.append(modestTool.linear_programming)

        return algorithms

    def algorithms_for_mdp_and_ma(self, modestTool, prismTool, stormTool):
        algorithms = []
        algorithms.append(modestTool.glrtdp)
        algorithms.append(modestTool.linear_programming)
        algorithms.append(stormTool.linear_programming_sparse)

        algorithms.append(stormTool.rational_search_sparse)
        #algorithms.append(stormTool.walkerchae_sparse)
        algorithms.append(stormTool.abstract_refinement)

        algorithms.append(stormTool.policy_iteration_sparse)
        algorithms.append(stormTool.value_iteration_to_policy_iteration_sparse)
        algorithms.append(prismTool.policy_iteration_explicit)
        algorithms.append(prismTool.modified_policy_iteration_explicit)
        algorithms.append(prismTool.value_iteration_explicit)
        algorithms.append(prismTool.top_value_iteration_explicit)
        algorithms.append(prismTool.gauss_seidel_explicit)
        #algorithms.append(prismTool.jacobi_explicit)

        algorithms.append(modestTool.value_iteration)
        algorithms.append(modestTool.interval_iteration)
        algorithms.append(modestTool.sequential_interval_iteration)
        algorithms.append(modestTool.sound_value_iteration)
        algorithms.append(modestTool.optimistic_value_iteration)

        algorithms.append(stormTool.value_iteration_sparse)
        algorithms.append(stormTool.top_value_iteration_sparse)

        #algorithms.append(stormTool.eigen_sparse)
        #algorithms.append(stormTool.elimination_sparse)

        #algorithms.append(prismTool.backwards_gauss_seidel_explicit)
        #algorithms.append(stormTool.gmm_sparse)
        #algorithms.append(stormTool.gauss_seidel_sparse)
        #algorithms.append(stormTool.jacobi_sparse)
        #algorithms.append(stormTool.successive_over_relaxation_sparse)
        algorithms.append(stormTool.interval_iteration_sparse)
        algorithms.append(stormTool.sound_value_iteration_sparse)
        algorithms.append(stormTool.optimistic_value_iteration_sparse)
        algorithms.append(stormTool.value_iteration_dd_to_sparse)
        algorithms.append(stormTool.top_value_iteration_dd_to_sparse)


        algorithms.append(prismTool.value_iteration_sparse)
        algorithms.append(prismTool.top_value_iteration_sparse)

        algorithms.append(prismTool.value_iteration_hybrid)
        algorithms.append(prismTool.top_value_iteration_hybrid)
        algorithms.append(stormTool.value_iteration_hybrid)
        algorithms.append(stormTool.top_value_iteration_hybrid)

        algorithms.append(stormTool.bi_value_iteration_sparse)
        algorithms.append(stormTool.bi_top_value_iteration_sparse)

        algorithms.append(stormTool.bi_value_iteration_hybrid)
        algorithms.append(stormTool.bi_top_value_iteration_hybrid)
        algorithms.append(stormTool.bi_value_iteration_dd_to_sparse)
        algorithms.append(stormTool.bi_top_value_iteration_dd_to_sparse)

        algorithms.append(stormTool.value_iteration_dd)
        algorithms.append(stormTool.bi_value_iteration_dd)
        algorithms.append(prismTool.value_iteration_mtbddd)
        algorithms.append(prismTool.top_value_iteration_mtbddd)

        return algorithms

    def algorithms_for_markov_chains(self, modestTool, prismTool, stormTool):
        algorithms = []

        algorithms.append(prismTool.confidence_interval)
        algorithms.append(prismTool.asymptotic_confidence_interval)
        algorithms.append(prismTool.apmc)
        algorithms.append(modestTool.confidence_interval)
        algorithms.append(modestTool.okamoto)
        algorithms.append(modestTool.adaptive)

        algorithms.append(modestTool.linear_programming)
        algorithms.append(stormTool.rational_search_sparse)
        algorithms.append(stormTool.walkerchae_sparse)
        algorithms.append(stormTool.abstract_refinement)

        algorithms.append(prismTool.value_iteration_explicit)
        algorithms.append(prismTool.top_value_iteration_explicit)
        algorithms.append(prismTool.gauss_seidel_explicit)
        algorithms.append(prismTool.backwards_gauss_seidel_explicit)
        algorithms.append(prismTool.jacobi_explicit)

        algorithms.append(modestTool.value_iteration)
        algorithms.append(modestTool.interval_iteration)
        algorithms.append(modestTool.sequential_interval_iteration)
        algorithms.append(modestTool.sound_value_iteration)
        algorithms.append(modestTool.optimistic_value_iteration)

        algorithms.append(stormTool.value_iteration_sparse)
        algorithms.append(stormTool.top_value_iteration_sparse)

        algorithms.append(stormTool.eigen_sparse)
        algorithms.append(stormTool.elimination_sparse)

        algorithms.append(stormTool.gmm_sparse)
        algorithms.append(stormTool.gauss_seidel_sparse)
        algorithms.append(stormTool.jacobi_sparse)
        algorithms.append(stormTool.successive_over_relaxation_sparse)
        algorithms.append(stormTool.interval_iteration_sparse)
        algorithms.append(stormTool.sound_value_iteration_sparse)
        algorithms.append(stormTool.optimistic_value_iteration_sparse)
        algorithms.append(stormTool.value_iteration_dd_to_sparse)
        algorithms.append(stormTool.top_value_iteration_dd_to_sparse)


        algorithms.append(prismTool.value_iteration_sparse)
        algorithms.append(prismTool.top_value_iteration_sparse)

        algorithms.append(prismTool.value_iteration_hybrid)
        algorithms.append(prismTool.top_value_iteration_hybrid)
        algorithms.append(stormTool.value_iteration_hybrid)
        algorithms.append(stormTool.top_value_iteration_hybrid)

        algorithms.append(stormTool.bi_value_iteration_sparse)
        algorithms.append(stormTool.bi_top_value_iteration_sparse)

        algorithms.append(stormTool.bi_value_iteration_hybrid)
        algorithms.append(stormTool.bi_top_value_iteration_hybrid)
        algorithms.append(stormTool.bi_value_iteration_dd_to_sparse)
        algorithms.append(stormTool.bi_top_value_iteration_dd_to_sparse)

        algorithms.append(stormTool.value_iteration_dd)
        algorithms.append(stormTool.bi_value_iteration_dd)
        algorithms.append(prismTool.value_iteration_mtbddd)
        algorithms.append(prismTool.top_value_iteration_mtbddd)


        return algorithms