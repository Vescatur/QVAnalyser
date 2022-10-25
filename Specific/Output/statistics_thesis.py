from Library.Results.measurements import Measurements
from Specific.Output.statistics import Statistics
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Prism.prism_tool import PrismTool
from Specific.Tools.Storm.storm_tool import StormTool


class StatisticsThesis(object):

    def __init__(self, benchmark):

        characteristics = [Measurements.STATES, Measurements.TRANSITIONS, Measurements.BRANCHES]

        Statistics(benchmark, characteristics, Measurements.STATE_SPACE_TIME,"StatisticsStateSpace")
        Statistics(benchmark, characteristics, Measurements.PROPERTY_TIME,"StatisticsProperty")
        Statistics(benchmark, characteristics, Measurements.WALL_TIME,"StatisticsWall")

    def get_algorithms(self):
        modestTool = ModestTool()
        prismTool = PrismTool()
        stormTool = StormTool()

        algorithms = []

        algorithms.append(prismTool.confidence_interval)
        algorithms.append(prismTool.asymptotic_confidence_interval)
        algorithms.append(prismTool.apmc)
        algorithms.append(modestTool.confidence_interval)
        algorithms.append(modestTool.okamoto)
        algorithms.append(modestTool.adaptive)

        algorithms.append(modestTool.glrtdp)
        algorithms.append(modestTool.linear_programming)
        algorithms.append(stormTool.linear_programming_sparse)

        algorithms.append(stormTool.rational_search_sparse)
        algorithms.append(stormTool.walkerchae_sparse)
        algorithms.append(stormTool.abstract_refinement)

        algorithms.append(stormTool.policy_iteration_sparse)
        algorithms.append(stormTool.value_iteration_to_policy_iteration_sparse)
        algorithms.append(prismTool.policy_iteration_explicit)
        algorithms.append(prismTool.modified_policy_iteration_explicit)
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

        algorithms.append(prismTool.backwards_reachability)
        algorithms.append(prismTool.stochastic_games)
        algorithms.append(prismTool.digital_clocks)

        return algorithms