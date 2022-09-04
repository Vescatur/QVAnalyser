from Library.Output.matrix_similiar import MatrixSimiliar
from Library.Output.matrix_wins import MatrixWins
from Library.Output.plot_filters import only_dtmc_and_ctmc
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Prism.prism_tool import PrismTool
from Specific.Tools.Storm.storm_tool import StormTool


class MatrixSprint6(object):

    def __init__(self, benchmark):
        algorithms_markov_chains = []
        stormTool = StormTool()
        modestTool = ModestTool()
        prismTool = PrismTool()


        #algorithms_markov_chains.append(stormTool.policy_iteration_sparse)
        #algorithms_markov_chains.append(stormTool.linear_programming_sparse)
        #algorithms_markov_chains.append(stormTool.value_iteration_to_policy_iteration_sparse)
        #algorithms_markov_chains.append(modestTool.glrtdp)
        #algorithms_markov_chains.append(prismTool.backwards_reachability)
        #algorithms_markov_chains.append(prismTool.policy_iteration_explicit)
        #algorithms_markov_chains.append(prismTool.modified_policy_iteration_explicit)
        #algorithms_markov_chains.append(prismTool.stochastic_games)
        #algorithms_markov_chains.append(prismTool.digital_clocks)


        algorithms_markov_chains.append(stormTool.abstract_refinement)
        algorithms_markov_chains.append(prismTool.jacobi_with_over_relaxation_explicit)
        algorithms_markov_chains.append(prismTool.succesive_over_relaxation_explicit)
        algorithms_markov_chains.append(prismTool.backwards_succesive_over_relaxation_explicit)
        algorithms_markov_chains.append(modestTool.linear_programming)
        algorithms_markov_chains.append(stormTool.elimination_sparse)
        algorithms_markov_chains.append(prismTool.jacobi_explicit)
        algorithms_markov_chains.append(prismTool.gauss_seidel_explicit)
        algorithms_markov_chains.append(prismTool.backwards_gauss_seidel_explicit)
        algorithms_markov_chains.append(prismTool.value_iteration_explicit)



        algorithms_markov_chains.append(stormTool.successive_over_relaxation_sparse)
        algorithms_markov_chains.append(stormTool.gmm_sparse)
        algorithms_markov_chains.append(stormTool.jacobi_sparse)
        algorithms_markov_chains.append(stormTool.gauss_seidel_sparse)
        algorithms_markov_chains.append(stormTool.sound_value_iteration_sparse)
        algorithms_markov_chains.append(stormTool.optimistic_value_iteration_sparse)
        algorithms_markov_chains.append(stormTool.interval_iteration_sparse)
        algorithms_markov_chains.append(stormTool.eigen_sparse)

        algorithms_markov_chains.append(modestTool.interval_iteration)
        algorithms_markov_chains.append(modestTool.sequential_interval_iteration)
        algorithms_markov_chains.append(modestTool.sound_value_iteration)
        algorithms_markov_chains.append(modestTool.optimistic_value_iteration)

        algorithms_markov_chains.append(modestTool.value_iteration)
        algorithms_markov_chains.append(stormTool.value_iteration_sparse)
        algorithms_markov_chains.append(stormTool.top_value_iteration_sparse)

        algorithms_markov_chains.append(prismTool.value_iteration_sparse)
        algorithms_markov_chains.append(stormTool.value_iteration_hybrid)
        algorithms_markov_chains.append(prismTool.value_iteration_hybrid)
        algorithms_markov_chains.append(stormTool.top_value_iteration_hybrid)
        algorithms_markov_chains.append(stormTool.bi_value_iteration_sparse)
        algorithms_markov_chains.append(stormTool.bi_value_iteration_hybrid)
        algorithms_markov_chains.append(stormTool.bi_top_value_iteration_sparse)
        algorithms_markov_chains.append(stormTool.bi_top_value_iteration_hybrid)
        algorithms_markov_chains.append(prismTool.top_value_iteration_sparse)
        algorithms_markov_chains.append(prismTool.top_value_iteration_explicit)
        algorithms_markov_chains.append(prismTool.top_value_iteration_hybrid)

        algorithms_markov_chains.append(stormTool.value_iteration_dd_to_sparse)
        algorithms_markov_chains.append(stormTool.top_value_iteration_dd_to_sparse)
        algorithms_markov_chains.append(stormTool.bi_value_iteration_dd_to_sparse)
        algorithms_markov_chains.append(stormTool.bi_top_value_iteration_dd_to_sparse)

        algorithms_markov_chains.append(prismTool.top_value_iteration_mtbddd)
        algorithms_markov_chains.append(stormTool.bi_value_iteration_dd)
        algorithms_markov_chains.append(prismTool.value_iteration_mtbddd)
        algorithms_markov_chains.append(stormTool.value_iteration_dd)

        algorithms_markov_chains.append(stormTool.rational_search_sparse)
        algorithms_markov_chains.append(stormTool.walkerchae_sparse)

        algorithms_markov_chains.append(modestTool.confidence_interval)
        algorithms_markov_chains.append(prismTool.confidence_interval)
        algorithms_markov_chains.append(prismTool.asymptotic_confidence_interval)
        algorithms_markov_chains.append(prismTool.apmc)
        algorithms_markov_chains.append(modestTool.okamoto)
        algorithms_markov_chains.append(modestTool.adaptive)

        MatrixSimiliar(benchmark, algorithms_markov_chains, only_dtmc_and_ctmc())
        #MatrixWins(benchmark,benchmark.algorithms)