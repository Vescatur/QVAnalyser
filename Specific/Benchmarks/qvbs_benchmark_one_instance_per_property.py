from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Storm.storm_tool import StormTool

# This class has been generated using _GenerateBenchmarkFromQVBS.py
class QvbsBenchmarkOneInstancePerProperty(Benchmark):
    def __init__(self):
        super().__init__()
        self.time_limit = 10
        
        self.add_benchmark_instances()
        

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
        self.algorithms.append(modestTool.glrtdp)

        stormTool = StormTool()
        self.algorithms.append(stormTool.top_jacobi)
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
        self.algorithms.append(stormTool.abstract_refinement)
        self.algorithms.append(stormTool.value_iteration_dd)
        self.algorithms.append(stormTool.policy_iteration_dd)
        self.algorithms.append(stormTool.jacobi_dd)
        self.algorithms.append(stormTool.rational_search_dd)
        self.algorithms.append(stormTool.value_iteration_dd_to_sparse)
        self.algorithms.append(stormTool.top_value_iteration_dd_to_sparse)
        self.algorithms.append(stormTool.value_iteration_hybrid)
        self.algorithms.append(stormTool.top_value_iteration_hybrid)
    
    def add_benchmark_instances(self):
        self.add_cluster_1()
        self.add_embedded_1()
        self.add_fms_1()
        self.add_hill_toggle_1()
        self.add_kanban_1()
        self.add_majority_1()
        self.add_mapk_cascade_1()
        self.add_p53_1()
        self.add_philosophers_1()
        self.add_polling_1()
        self.add_speed_ind_1()
        self.add_tandem_1()
        self.add_toggle_switch_1()
        self.add_bluetooth_1()
        self.add_brp_1()
        self.add_coupon_1()
        self.add_crowds_1()
        self.add_egl_1()
        self.add_haddad_monmege_1()
        self.add_herman_1()
        self.add_leader_sync_1()
        self.add_nand_1()
        self.add_oscillators_1()
        self.add_bitcoin_attack_1()
        self.add_breakdown_queues_1()
        self.add_cabinets_1()
        self.add_dpm_1()
        self.add_erlang_1()
        self.add_flexible_manufacturing_1()
        self.add_ftpp_1()
        self.add_ftwc_1()
        self.add_hecs_1()
        self.add_jobs_1()
        self.add_mcs_1()
        self.add_polling_system_1()
        self.add_readers_writers_1()
        self.add_reentrant_queues_1()
        self.add_sf_1()
        self.add_sms_1()
        self.add_stream_1()
        self.add_vgs_1()
        self.add_beb_1()
        self.add_blocksworld_1()
        self.add_boxworld_1()
        self.add_cdrive_1()
        self.add_consensus_1()
        self.add_csma_1()
        self.add_eajs_1()
        self.add_echoring_1()
        self.add_elevators_1()
        self.add_exploding_blocksworld_1()
        self.add_firewire_1()
        self.add_firewire_abst_1()
        self.add_firewire_dl_1()
        self.add_ij_1()
        self.add_pacman_1()
        self.add_philosophers_mdp_1()
        self.add_pnueli_zuck_1()
        self.add_rabin_1()
        self.add_random_predicates_1()
        self.add_rectangle_tireworld_1()
        self.add_resource_gathering_1()
        self.add_tireworld_1()
        self.add_triangle_tireworld_1()
        self.add_wlan_1()
        self.add_wlan_dl_1()
        self.add_zenotravel_1()
        self.add_zeroconf_1()
        self.add_zeroconf_dl_1()
        self.add_brp_pta_1()
        self.add_csma_pta_1()
        self.add_csma_abst_pta_1()
        self.add_firewire_pta_1()
        self.add_firewire_abst_pta_1()
        self.add_repudiation_honest_1()
        self.add_repudiation_malicious_1()
        self.add_wlan_large_1()
        self.add_zeroconf_pta_1()
    
    def add_cluster_1(self):
        model = BenchmarkModel(self, "ctmc/cluster/cluster.jani","ctmc/cluster/cluster.props","ctmc/cluster/cluster.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
    
    def add_embedded_1(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani","ctmc/embedded/embedded.props","ctmc/embedded/embedded.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "actuators", PropertyType.REACHABILITY, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "danger_time", PropertyType.EXPECTED_REWARD, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "io", PropertyType.REACHABILITY, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "main", PropertyType.REACHABILITY, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "sensors", PropertyType.REACHABILITY, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "up_time", PropertyType.EXPECTED_REWARD, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
    
    def add_fms_1(self):
        model = BenchmarkModel(self, "ctmc/fms/fms.jani","ctmc/fms/fms.props","ctmc/fms/fms.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
    
    def add_hill_toggle_1(self):
        model = BenchmarkModel(self, "ctmc/hill-toggle/hill-toggle.jani","","", ModelType.CTMC,"PRISM-∞","infinite-state biological model")
    
    def add_kanban_1(self):
        model = BenchmarkModel(self, "ctmc/kanban/kanban.jani","ctmc/kanban/kanban.props","ctmc/kanban/kanban.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
    
    def add_majority_1(self):
        model = BenchmarkModel(self, "ctmc/majority/majority.jani","ctmc/majority/majority.props","ctmc/majority/majority.prism", ModelType.CTMC,"PRISM","biological model")
    
    def add_mapk_cascade_1(self):
        model = BenchmarkModel(self, "ctmc/mapk_cascade/mapk_cascade.jani","ctmc/mapk_cascade/mapk_cascade.props","ctmc/mapk_cascade/mapk_cascade.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "activated_time", PropertyType.EXPECTED_REWARD, {"N": 1, "T": 30})
        BenchmarkInstance(sequence, {})
    
    def add_p53_1(self):
        model = BenchmarkModel(self, "ctmc/p53/p53.jani","","", ModelType.CTMC,"PRISM-∞","infinite-state biological model")
    
    def add_philosophers_1(self):
        model = BenchmarkModel(self, "ctmc/philosophers/philosophers.4.jani","","", ModelType.CTMC,"GreatSPN","small symbolic representation")
        sequence = BenchmarkSequence(model, "MaxPrReachDeadlock", PropertyType.REACHABILITY, {"TIME_BOUND": 1})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MinExpTimeDeadlock", PropertyType.EXPECTED_TIME, {"TIME_BOUND": 1})
        BenchmarkInstance(sequence, {})
    
    def add_polling_1(self):
        model = BenchmarkModel(self, "ctmc/polling/polling.3.jani","ctmc/polling/polling.props","ctmc/polling/polling.3.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "s1_before_s2", PropertyType.REACHABILITY, {"T": 16})
        BenchmarkInstance(sequence, {})
    
    def add_speed_ind_1(self):
        model = BenchmarkModel(self, "ctmc/speed-ind/speed-ind.jani","ctmc/speed-ind/speed-ind.props","ctmc/speed-ind/speed-ind.prism", ModelType.CTMC,"PRISM","biological model")
    
    def add_tandem_1(self):
        model = BenchmarkModel(self, "ctmc/tandem/tandem.jani","ctmc/tandem/tandem.props","ctmc/tandem/tandem.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
    
    def add_toggle_switch_1(self):
        model = BenchmarkModel(self, "ctmc/toggle-switch/toggle-switch.jani","ctmc/toggle-switch/toggle-switch.props","ctmc/toggle-switch/toggle-switch.prism", ModelType.CTMC,"PRISM","biological model")
    
    def add_bluetooth_1(self):
        model = BenchmarkModel(self, "dtmc/bluetooth/bluetooth.jani","dtmc/bluetooth/bluetooth.props","dtmc/bluetooth/bluetooth.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time", PropertyType.EXPECTED_REWARD, {"mrec": 1})
        BenchmarkInstance(sequence, {})
    
    def add_brp_1(self):
        model = BenchmarkModel(self, "dtmc/brp/brp.jani","dtmc/brp/brp.props","dtmc/brp/brp.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "p1", PropertyType.REACHABILITY, {"N": 16, "MAX": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "p2", PropertyType.REACHABILITY, {"N": 16, "MAX": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "p4", PropertyType.REACHABILITY, {"N": 16, "MAX": 2})
        BenchmarkInstance(sequence, {})
    
    def add_coupon_1(self):
        model = BenchmarkModel(self, "dtmc/coupon/coupon.5-2.jani","","", ModelType.DTMC,"PGCL","classic probabilistic programming example")
        sequence = BenchmarkSequence(model, "collect_all", PropertyType.REACHABILITY, {"B": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "exp_draws", PropertyType.EXPECTED_REWARD, {"B": 5})
        BenchmarkInstance(sequence, {})
    
    def add_crowds_1(self):
        model = BenchmarkModel(self, "dtmc/crowds/crowds.jani","dtmc/crowds/crowds.props","dtmc/crowds/crowds.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "positive", PropertyType.REACHABILITY, {"TotalRuns": 3, "CrowdSize": 5})
        BenchmarkInstance(sequence, {})
    
    def add_egl_1(self):
        model = BenchmarkModel(self, "dtmc/egl/egl.jani","dtmc/egl/egl.props","dtmc/egl/egl.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "messagesA", PropertyType.EXPECTED_REWARD, {"N": 5, "L": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "messagesB", PropertyType.EXPECTED_REWARD, {"N": 5, "L": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "unfairA", PropertyType.REACHABILITY, {"N": 5, "L": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "unfairB", PropertyType.REACHABILITY, {"N": 5, "L": 2})
        BenchmarkInstance(sequence, {})
    
    def add_haddad_monmege_1(self):
        model = BenchmarkModel(self, "dtmc/haddad-monmege/haddad-monmege.jani","dtmc/haddad-monmege/haddad-monmege.prctl","dtmc/haddad-monmege/haddad-monmege.pm", ModelType.DTMC,"PRISM","adversarial example for value iteration")
        sequence = BenchmarkSequence(model, "target", PropertyType.REACHABILITY, {"N": 20, "p": 0.7})
        BenchmarkInstance(sequence, {})
    
    def add_herman_1(self):
        model = BenchmarkModel(self, "dtmc/herman/herman.3.jani","dtmc/herman/herman.props","dtmc/herman/herman.3.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "steps", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_leader_sync_1(self):
        model = BenchmarkModel(self, "dtmc/leader_sync/leader_sync.3-2.jani","dtmc/leader_sync/leader_sync.props","dtmc/leader_sync/leader_sync.3-2.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually_elected", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_nand_1(self):
        model = BenchmarkModel(self, "dtmc/nand/nand.jani","dtmc/nand/nand.props","dtmc/nand/nand.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "reliable", PropertyType.REACHABILITY, {"N": 20, "K": 1})
        BenchmarkInstance(sequence, {})
    
    def add_oscillators_1(self):
        model = BenchmarkModel(self, "dtmc/oscillators/oscillators.3-6-0.1-1.jani","dtmc/oscillators/oscillators.props","dtmc/oscillators/oscillators.3-6-0.1-1.prism", ModelType.DTMC,"PRISM","large fan-out from initial state")
        sequence = BenchmarkSequence(model, "time_to_synch", PropertyType.EXPECTED_REWARD, {"mu": 0.1, "lambda": 1.0})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "power_consumption", PropertyType.EXPECTED_REWARD, {"mu": 0.1, "lambda": 1.0})
        BenchmarkInstance(sequence, {})
    
    def add_bitcoin_attack_1(self):
        model = BenchmarkModel(self, "ma/bitcoin-attack/bitcoin-attack.jani","","", ModelType.MA,"Modest","")
        sequence = BenchmarkSequence(model, "T_MWinMin", PropertyType.EXPECTED_TIME, {"MALICIOUS": 20, "CD": 6})
        BenchmarkInstance(sequence, {})
    
    def add_breakdown_queues_1(self):
        model = BenchmarkModel(self, "ma/breakdown-queues/breakdown-queues.jani","","", ModelType.MA,"Modest","")
        sequence = BenchmarkSequence(model, "Min", PropertyType.REACHABILITY, {"K": 8})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "Max", PropertyType.REACHABILITY, {"K": 8})
        BenchmarkInstance(sequence, {})
    
    def add_cabinets_1(self):
        model = BenchmarkModel(self, "ma/cabinets/cabinets.2-1-false.jani","","", ModelType.MA,"Galileo","")
    
    def add_dpm_1(self):
        model = BenchmarkModel(self, "ma/dpm/dpm.jani","","", ModelType.MA,"Modest","scalable nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PminQueuesFull", PropertyType.REACHABILITY, {"N": 4, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "PmaxQueuesFull", PropertyType.REACHABILITY, {"N": 4, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "PminQueue1Full", PropertyType.REACHABILITY, {"N": 4, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "PmaxQueue1Full", PropertyType.REACHABILITY, {"N": 4, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TminQueuesFull", PropertyType.EXPECTED_TIME, {"N": 4, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_erlang_1(self):
        model = BenchmarkModel(self, "ma/erlang/erlang.jani","","", ModelType.MA,"Modest","scalable sanity check model")
        sequence = BenchmarkSequence(model, "PminReach", PropertyType.REACHABILITY, {"K": 10, "R": 10, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TminReach", PropertyType.EXPECTED_TIME, {"K": 10, "R": 10, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_flexible_manufacturing_1(self):
        model = BenchmarkModel(self, "ma/flexible-manufacturing/flexible-manufacturing.3.jani","","", ModelType.MA,"GreatSPN","small symbolic representation")
        sequence = BenchmarkSequence(model, "M2Fail_E", PropertyType.EXPECTED_TIME, {"T": 1})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "M3Fail_E", PropertyType.EXPECTED_TIME, {"T": 1})
        BenchmarkInstance(sequence, {})
    
    def add_ftpp_1(self):
        model = BenchmarkModel(self, "ma/ftpp/ftpp.1-1-false.jani","","", ModelType.MA,"Galileo","")
    
    def add_ftwc_1(self):
        model = BenchmarkModel(self, "ma/ftwc/ftwc.jani","","", ModelType.MA,"Modest","fault-tolerant queueing system")
        sequence = BenchmarkSequence(model, "ReachMinIsOne", PropertyType.REACHABILITY, {"N": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TimeMin", PropertyType.EXPECTED_TIME, {"N": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TimeMax", PropertyType.EXPECTED_TIME, {"N": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_hecs_1(self):
        model = BenchmarkModel(self, "ma/hecs/hecs.false-1-1.jani","","", ModelType.MA,"Galileo","")
    
    def add_jobs_1(self):
        model = BenchmarkModel(self, "ma/jobs/jobs.5-2.jani","","", ModelType.MA,"PRISM-MA","stochastic scheduling problem")
        sequence = BenchmarkSequence(model, "completiontime", PropertyType.EXPECTED_TIME, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "avgtime", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_mcs_1(self):
        model = BenchmarkModel(self, "ma/mcs/mcs.1-1-10-false.jani","","", ModelType.MA,"Galileo","")
    
    def add_polling_system_1(self):
        model = BenchmarkModel(self, "ma/polling-system/polling-system.jani","","", ModelType.MA,"Modest","small nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PminBothFullIsOne", PropertyType.REACHABILITY, {"JOB_TYPES": 3, "C": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TminBothFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TmaxBothFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_readers_writers_1(self):
        model = BenchmarkModel(self, "ma/readers-writers/readers-writers.5.jani","","", ModelType.MA,"GreatSPN","standard GSPN example")
        sequence = BenchmarkSequence(model, "pr_many_requests", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "exp_time_many_requests", PropertyType.EXPECTED_TIME, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "pr_network", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_reentrant_queues_1(self):
        model = BenchmarkModel(self, "ma/reentrant-queues/reentrant-queues.jani","","", ModelType.MA,"Modest","asymmetric nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PminBothQueuesFullIsOne", PropertyType.REACHABILITY, {"JOB_TYPES": 3, "C_LEFT": 3, "C_RIGHT": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TminBothQueuesFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C_LEFT": 3, "C_RIGHT": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "TmaxBothQueuesFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C_LEFT": 3, "C_RIGHT": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_sf_1(self):
        model = BenchmarkModel(self, "ma/sf/sf.1-10.jani","","", ModelType.MA,"Galileo","")
    
    def add_sms_1(self):
        model = BenchmarkModel(self, "ma/sms/sms.1-false.jani","","", ModelType.MA,"Galileo","")
    
    def add_stream_1(self):
        model = BenchmarkModel(self, "ma/stream/stream.jani","","", ModelType.MA,"PRISM-MA","simple scalable planning benchmark")
        sequence = BenchmarkSequence(model, "exp_buffertime", PropertyType.EXPECTED_REWARD, {"N": 10})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "exp_restarts", PropertyType.EXPECTED_REWARD, {"N": 10})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "pr_underrun", PropertyType.REACHABILITY, {"N": 10})
        BenchmarkInstance(sequence, {})
    
    def add_vgs_1(self):
        model = BenchmarkModel(self, "ma/vgs/vgs.4.jani","","", ModelType.MA,"Galileo","industrial case study")
        sequence = BenchmarkSequence(model, "MaxPrReachFailed", PropertyType.REACHABILITY, {"TIME_BOUND": 10000})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MinExpTimeFailed", PropertyType.EXPECTED_TIME, {"TIME_BOUND": 10000})
        BenchmarkInstance(sequence, {})
    
    def add_beb_1(self):
        model = BenchmarkModel(self, "mdp/beb/beb.3-4.jani","","", ModelType.MDP,"Modest","")
        sequence = BenchmarkSequence(model, "LineSeized", PropertyType.REACHABILITY, {"N": 3})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "GaveUp", PropertyType.REACHABILITY, {"N": 3})
        BenchmarkInstance(sequence, {})
    
    def add_blocksworld_1(self):
        model = BenchmarkModel(self, "mdp/blocksworld/blocksworld.5.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_boxworld_1(self):
        model = BenchmarkModel(self, "mdp/boxworld/boxworld.10-5.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_cdrive_1(self):
        model = BenchmarkModel(self, "mdp/cdrive/cdrive.2.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_consensus_1(self):
        model = BenchmarkModel(self, "mdp/consensus/consensus.2.jani","mdp/consensus/consensus.props","mdp/consensus/consensus.2.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "c1", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "c2", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "disagree", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "steps_max", PropertyType.EXPECTED_REWARD, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "steps_min", PropertyType.EXPECTED_REWARD, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_csma_1(self):
        model = BenchmarkModel(self, "mdp/csma/csma.2-2.jani","mdp/csma/csma.props","mdp/csma/csma.2-2.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "all_before_max", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "all_before_min", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "some_before", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_eajs_1(self):
        model = BenchmarkModel(self, "mdp/eajs/eajs.2.jani","mdp/eajs/eajs.props","mdp/eajs/eajs.2.prism", ModelType.MDP,"PRISM","reward-bounded properties")
        sequence = BenchmarkSequence(model, "ExpUtil", PropertyType.EXPECTED_REWARD, {"energy_capacity": 100, "B": 5})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_1(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MinFailed", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MinOffline1", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MaxOffline1", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MinOffline2", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MaxOffline2", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MinOffline3", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "MaxOffline3", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
    
    def add_elevators_1(self):
        model = BenchmarkModel(self, "mdp/elevators/elevators.a-3-3.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_exploding_blocksworld_1(self):
        model = BenchmarkModel(self, "mdp/exploding-blocksworld/exploding-blocksworld.5.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_1(self):
        model = BenchmarkModel(self, "mdp/firewire/firewire.false.jani","mdp/firewire/firewire.false.props","mdp/firewire/firewire.false.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "elected", PropertyType.REACHABILITY, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_sending", PropertyType.EXPECTED_REWARD, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_abst_1(self):
        model = BenchmarkModel(self, "mdp/firewire_abst/firewire_abst.jani","mdp/firewire_abst/firewire_abst.props","mdp/firewire_abst/firewire_abst.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "elected", PropertyType.REACHABILITY, {"delay": 3})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "rounds", PropertyType.EXPECTED_REWARD, {"delay": 3})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {"delay": 3})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {"delay": 3})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_dl_1(self):
        model = BenchmarkModel(self, "mdp/firewire_dl/firewire_dl.jani","mdp/firewire_dl/firewire_dl.props","mdp/firewire_dl/firewire_dl.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "deadline", PropertyType.REACHABILITY, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
    
    def add_ij_1(self):
        model = BenchmarkModel(self, "mdp/ij/ij.3.jani","mdp/ij/ij.3.props","mdp/ij/ij.3.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "stable", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_pacman_1(self):
        model = BenchmarkModel(self, "mdp/pacman/pacman.jani","mdp/pacman/pacman.props","mdp/pacman/pacman.nm", ModelType.MDP,"PRISM","learned probabilities")
        sequence = BenchmarkSequence(model, "crash", PropertyType.REACHABILITY, {"MAXSTEPS": 5})
        BenchmarkInstance(sequence, {})
    
    def add_philosophers_mdp_1(self):
        model = BenchmarkModel(self, "mdp/philosophers-mdp/philosophers-mdp.3.jani","mdp/philosophers-mdp/philosophers-mdp.3.props","mdp/philosophers-mdp/philosophers-mdp.3.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "eat", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_pnueli_zuck_1(self):
        model = BenchmarkModel(self, "mdp/pnueli-zuck/pnueli-zuck.3.jani","mdp/pnueli-zuck/pnueli-zuck.props","mdp/pnueli-zuck/pnueli-zuck.3.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "live", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_rabin_1(self):
        model = BenchmarkModel(self, "mdp/rabin/rabin.3.jani","mdp/rabin/rabin.3.props","mdp/rabin/rabin.3.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "live", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_random_predicates_1(self):
        model = BenchmarkModel(self, "mdp/random-predicates/random-predicates.a.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_rectangle_tireworld_1(self):
        model = BenchmarkModel(self, "mdp/rectangle-tireworld/rectangle-tireworld.5.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_resource_gathering_1(self):
        model = BenchmarkModel(self, "mdp/resource-gathering/resource-gathering.jani","mdp/resource-gathering/resource-gathering.prctl","mdp/resource-gathering/resource-gathering.pm", ModelType.MDP,"PRISM","")
    
    def add_tireworld_1(self):
        model = BenchmarkModel(self, "mdp/tireworld/tireworld.17.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_triangle_tireworld_1(self):
        model = BenchmarkModel(self, "mdp/triangle-tireworld/triangle-tireworld.9.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_1(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.0.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.0.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "collisions", PropertyType.REACHABILITY, {"COL": 0})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "cost_max", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "cost_min", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "num_collisions", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "sent", PropertyType.REACHABILITY, {"COL": 0})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_dl_1(self):
        model = BenchmarkModel(self, "mdp/wlan_dl/wlan_dl.0.jani","mdp/wlan_dl/wlan_dl.props","mdp/wlan_dl/wlan_dl.0.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "deadline", PropertyType.REACHABILITY, {"deadline": 80})
        BenchmarkInstance(sequence, {})
    
    def add_zenotravel_1(self):
        model = BenchmarkModel(self, "mdp/zenotravel/zenotravel.4-2-2.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_1(self):
        model = BenchmarkModel(self, "mdp/zeroconf/zeroconf.jani","mdp/zeroconf/zeroconf.props","mdp/zeroconf/zeroconf.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "correct_max", PropertyType.REACHABILITY, {"N": 20, "K": 2, "reset": True})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "correct_min", PropertyType.REACHABILITY, {"N": 20, "K": 2, "reset": True})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_dl_1(self):
        model = BenchmarkModel(self, "mdp/zeroconf_dl/zeroconf_dl.jani","mdp/zeroconf_dl/zeroconf_dl.props","mdp/zeroconf_dl/zeroconf_dl.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "deadline_max", PropertyType.REACHABILITY, {"N": 1000, "K": 1, "reset": True, "deadline": 10})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "deadline_min", PropertyType.REACHABILITY, {"N": 1000, "K": 1, "reset": True, "deadline": 10})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_1(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "T_1", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "T_2", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "T_A1", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "T_A2", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_A", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_B", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_1", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_2", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_3", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_4", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "Emax", PropertyType.EXPECTED_TIME, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "Emin", PropertyType.EXPECTED_TIME, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
    
    def add_csma_pta_1(self):
        model = BenchmarkModel(self, "pta/csma-pta/csma-pta.jani","pta/csma-pta/csma-pta.props","pta/csma-pta/csma-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "collisions", PropertyType.REACHABILITY, {"K": 2, "COL": 4})
        BenchmarkInstance(sequence, {})
    
    def add_csma_abst_pta_1(self):
        model = BenchmarkModel(self, "pta/csma_abst-pta/csma_abst-pta.jani","pta/csma_abst-pta/csma_abst-pta.props","pta/csma_abst-pta/csma_abst-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"K": 1, "T": 1000})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_pta_1(self):
        model = BenchmarkModel(self, "pta/firewire-pta/firewire-pta.jani","pta/firewire-pta/firewire-pta.props","pta/firewire-pta/firewire-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"delay": 30, "T": 2500})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_abst_pta_1(self):
        model = BenchmarkModel(self, "pta/firewire_abst-pta/firewire_abst-pta.jani","pta/firewire_abst-pta/firewire_abst-pta.props","pta/firewire_abst-pta/firewire_abst-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"delay": 30, "T": 50})
        BenchmarkInstance(sequence, {})
    
    def add_repudiation_honest_1(self):
        model = BenchmarkModel(self, "pta/repudiation_honest/repudiation_honest.jani","pta/repudiation_honest/repudiation_honest.props","pta/repudiation_honest/repudiation_honest.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"T": 40})
        BenchmarkInstance(sequence, {})
    
    def add_repudiation_malicious_1(self):
        model = BenchmarkModel(self, "pta/repudiation_malicious/repudiation_malicious.jani","pta/repudiation_malicious/repudiation_malicious.props","pta/repudiation_malicious/repudiation_malicious.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"T": 5})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_large_1(self):
        model = BenchmarkModel(self, "pta/wlan-large/wlan-large.jani","","", ModelType.PTA,"Modest","")
        sequence = BenchmarkSequence(model, "P_1", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_min", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "P_max", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "E_and", PropertyType.EXPECTED_TIME, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "E_or", PropertyType.EXPECTED_TIME, {"K": 2})
        BenchmarkInstance(sequence, {})
        sequence = BenchmarkSequence(model, "E_1", PropertyType.EXPECTED_REWARD, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_pta_1(self):
        model = BenchmarkModel(self, "pta/zeroconf-pta/zeroconf-pta.jani","pta/zeroconf-pta/zeroconf-pta.props","pta/zeroconf-pta/zeroconf-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "incorrect", PropertyType.REACHABILITY, {"T": 100})
        BenchmarkInstance(sequence, {})
