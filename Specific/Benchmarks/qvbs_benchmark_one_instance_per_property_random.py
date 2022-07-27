from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Library.Benchmarks.model_type import ModelType
from Library.Benchmarks.property_type import PropertyType
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Storm.storm_tool import StormTool

# This class has been generated using _GenerateBenchmarkFromQVBS.py
class QvbsBenchmarkOneInstancePerPropertyRandom(Benchmark):
    def __init__(self):
        super().__init__()
        self.time_limit = 10
        
        self.add_benchmark_instances()

        modestTool = ModestTool()
        self.tools.append(modestTool)
        self.algorithms.append(modestTool.interval_iteration)
    
    def add_benchmark_instances(self):
        self.add_embedded_actuators()
        self.add_embedded_danger_time()
        self.add_embedded_io()
        self.add_embedded_main()
        self.add_embedded_sensors()
        self.add_embedded_up_time()
        self.add_mapk_cascade_activated_time()
        self.add_philosophers_MaxPrReachDeadlock()
        self.add_philosophers_MinExpTimeDeadlock()
        self.add_polling_s1_before_s2()
        self.add_bluetooth_time()
        self.add_brp_p1()
        self.add_brp_p2()
        self.add_brp_p4()
        self.add_coupon_collect_all()
        self.add_coupon_exp_draws()
        self.add_crowds_positive()
        self.add_egl_messagesA()
        self.add_egl_messagesB()
        self.add_egl_unfairA()
        self.add_egl_unfairB()
        self.add_haddad_monmege_target()
        self.add_herman_steps()
        self.add_leader_sync_eventually_elected()
        self.add_leader_sync_time()
        self.add_nand_reliable()
        self.add_oscillators_time_to_synch()
        self.add_oscillators_power_consumption()
        self.add_bitcoin_attack_T_MWinMin()
        self.add_breakdown_queues_Min()
        self.add_breakdown_queues_Max()
        self.add_dpm_PminQueuesFull()
        self.add_dpm_PmaxQueuesFull()
        self.add_dpm_PminQueue1Full()
        self.add_dpm_PmaxQueue1Full()
        self.add_dpm_TminQueuesFull()
        self.add_erlang_PminReach()
        self.add_erlang_TminReach()
        self.add_flexible_manufacturing_M2Fail_E()
        self.add_flexible_manufacturing_M3Fail_E()
        self.add_ftwc_ReachMinIsOne()
        self.add_ftwc_TimeMin()
        self.add_ftwc_TimeMax()
        self.add_jobs_completiontime()
        self.add_jobs_avgtime()
        self.add_polling_system_PminBothFullIsOne()
        self.add_polling_system_TminBothFull()
        self.add_polling_system_TmaxBothFull()
        self.add_readers_writers_pr_many_requests()
        self.add_readers_writers_exp_time_many_requests()
        self.add_readers_writers_pr_network()
        self.add_reentrant_queues_PminBothQueuesFullIsOne()
        self.add_reentrant_queues_TminBothQueuesFull()
        self.add_reentrant_queues_TmaxBothQueuesFull()
        self.add_stream_exp_buffertime()
        self.add_stream_exp_restarts()
        self.add_stream_pr_underrun()
        self.add_vgs_MaxPrReachFailed()
        self.add_vgs_MinExpTimeFailed()
        self.add_beb_LineSeized()
        self.add_beb_GaveUp()
        self.add_blocksworld_goal()
        self.add_boxworld_goal()
        self.add_cdrive_goal()
        self.add_consensus_c1()
        self.add_consensus_c2()
        self.add_consensus_disagree()
        self.add_consensus_steps_max()
        self.add_consensus_steps_min()
        self.add_csma_all_before_max()
        self.add_csma_all_before_min()
        self.add_csma_some_before()
        self.add_csma_time_max()
        self.add_csma_time_min()
        self.add_eajs_ExpUtil()
        self.add_echoring_MinFailed()
        self.add_echoring_MinOffline1()
        self.add_echoring_MaxOffline1()
        self.add_echoring_MinOffline2()
        self.add_echoring_MaxOffline2()
        self.add_echoring_MinOffline3()
        self.add_echoring_MaxOffline3()
        self.add_elevators_goal()
        self.add_exploding_blocksworld_goal()
        self.add_firewire_elected()
        self.add_firewire_time_max()
        self.add_firewire_time_min()
        self.add_firewire_time_sending()
        self.add_firewire_abst_elected()
        self.add_firewire_abst_rounds()
        self.add_firewire_abst_time_max()
        self.add_firewire_abst_time_min()
        self.add_firewire_dl_deadline()
        self.add_ij_stable()
        self.add_pacman_crash()
        self.add_philosophers_mdp_eat()
        self.add_pnueli_zuck_live()
        self.add_rabin_live()
        self.add_random_predicates_goal()
        self.add_rectangle_tireworld_goal()
        self.add_tireworld_goal()
        self.add_triangle_tireworld_goal()
        self.add_wlan_collisions()
        self.add_wlan_cost_max()
        self.add_wlan_cost_min()
        self.add_wlan_num_collisions()
        self.add_wlan_sent()
        self.add_wlan_time_max()
        self.add_wlan_time_min()
        self.add_wlan_dl_deadline()
        self.add_zenotravel_goal()
        self.add_zeroconf_correct_max()
        self.add_zeroconf_correct_min()
        self.add_zeroconf_dl_deadline_max()
        self.add_zeroconf_dl_deadline_min()
        self.add_brp_pta_T_1()
        self.add_brp_pta_T_2()
        self.add_brp_pta_T_A1()
        self.add_brp_pta_T_A2()
        self.add_brp_pta_P_A()
        self.add_brp_pta_P_B()
        self.add_brp_pta_P_1()
        self.add_brp_pta_P_2()
        self.add_brp_pta_P_3()
        self.add_brp_pta_P_4()
        self.add_brp_pta_Emax()
        self.add_brp_pta_Emin()
        self.add_csma_pta_collisions()
        self.add_csma_abst_pta_eventually()
        self.add_firewire_pta_eventually()
        self.add_firewire_abst_pta_eventually()
        self.add_repudiation_honest_eventually()
        self.add_repudiation_malicious_eventually()
        self.add_wlan_large_P_1()
        self.add_wlan_large_P_min()
        self.add_wlan_large_P_max()
        self.add_wlan_large_E_and()
        self.add_wlan_large_E_or()
        self.add_wlan_large_E_1()
        self.add_zeroconf_pta_incorrect()
    
    def add_embedded_actuators(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani","ctmc/embedded/embedded.props","ctmc/embedded/embedded.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "actuators", PropertyType.REACHABILITY, {"MAX_COUNT": 6, "T": 12})
        BenchmarkInstance(sequence, {})
    
    def add_embedded_danger_time(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani","ctmc/embedded/embedded.props","ctmc/embedded/embedded.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "danger_time", PropertyType.EXPECTED_REWARD, {"MAX_COUNT": 4, "T": 12})
        BenchmarkInstance(sequence, {})
    
    def add_embedded_io(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani","ctmc/embedded/embedded.props","ctmc/embedded/embedded.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "io", PropertyType.REACHABILITY, {"MAX_COUNT": 5, "T": 12})
        BenchmarkInstance(sequence, {})
    
    def add_embedded_main(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani","ctmc/embedded/embedded.props","ctmc/embedded/embedded.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "main", PropertyType.REACHABILITY, {"MAX_COUNT": 5, "T": 12})
        BenchmarkInstance(sequence, {})
    
    def add_embedded_sensors(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani","ctmc/embedded/embedded.props","ctmc/embedded/embedded.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "sensors", PropertyType.REACHABILITY, {"MAX_COUNT": 8, "T": 12})
        BenchmarkInstance(sequence, {})
    
    def add_embedded_up_time(self):
        model = BenchmarkModel(self, "ctmc/embedded/embedded.jani","ctmc/embedded/embedded.props","ctmc/embedded/embedded.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "up_time", PropertyType.EXPECTED_REWARD, {"MAX_COUNT": 2, "T": 12})
        BenchmarkInstance(sequence, {})
    
    def add_mapk_cascade_activated_time(self):
        model = BenchmarkModel(self, "ctmc/mapk_cascade/mapk_cascade.jani","ctmc/mapk_cascade/mapk_cascade.props","ctmc/mapk_cascade/mapk_cascade.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "activated_time", PropertyType.EXPECTED_REWARD, {"N": 1, "T": 30})
        BenchmarkInstance(sequence, {})
    
    def add_philosophers_MaxPrReachDeadlock(self):
        model = BenchmarkModel(self, "ctmc/philosophers/philosophers.32.jani","","", ModelType.CTMC,"GreatSPN","small symbolic representation")
        sequence = BenchmarkSequence(model, "MaxPrReachDeadlock", PropertyType.REACHABILITY, {"TIME_BOUND": 1})
        BenchmarkInstance(sequence, {})
    
    def add_philosophers_MinExpTimeDeadlock(self):
        model = BenchmarkModel(self, "ctmc/philosophers/philosophers.20.jani","","", ModelType.CTMC,"GreatSPN","small symbolic representation")
        sequence = BenchmarkSequence(model, "MinExpTimeDeadlock", PropertyType.EXPECTED_TIME, {"TIME_BOUND": 1})
        BenchmarkInstance(sequence, {})
    
    def add_polling_s1_before_s2(self):
        model = BenchmarkModel(self, "ctmc/polling/polling.17.jani","ctmc/polling/polling.props","ctmc/polling/polling.17.prism", ModelType.CTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "s1_before_s2", PropertyType.REACHABILITY, {"T": 16})
        BenchmarkInstance(sequence, {})
    
    def add_bluetooth_time(self):
        model = BenchmarkModel(self, "dtmc/bluetooth/bluetooth.jani","dtmc/bluetooth/bluetooth.props","dtmc/bluetooth/bluetooth.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time", PropertyType.EXPECTED_REWARD, {"mrec": 1})
        BenchmarkInstance(sequence, {})
    
    def add_brp_p1(self):
        model = BenchmarkModel(self, "dtmc/brp/brp.jani","dtmc/brp/brp.props","dtmc/brp/brp.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "p1", PropertyType.REACHABILITY, {"N": 16, "MAX": 2})
        BenchmarkInstance(sequence, {})
    
    def add_brp_p2(self):
        model = BenchmarkModel(self, "dtmc/brp/brp.jani","dtmc/brp/brp.props","dtmc/brp/brp.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "p2", PropertyType.REACHABILITY, {"N": 16, "MAX": 2})
        BenchmarkInstance(sequence, {})
    
    def add_brp_p4(self):
        model = BenchmarkModel(self, "dtmc/brp/brp.jani","dtmc/brp/brp.props","dtmc/brp/brp.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "p4", PropertyType.REACHABILITY, {"N": 32, "MAX": 4})
        BenchmarkInstance(sequence, {})
    
    def add_coupon_collect_all(self):
        model = BenchmarkModel(self, "dtmc/coupon/coupon.7-3.jani","","", ModelType.DTMC,"PGCL","classic probabilistic programming example")
        sequence = BenchmarkSequence(model, "collect_all", PropertyType.REACHABILITY, {"B": 5})
        BenchmarkInstance(sequence, {})
    
    def add_coupon_exp_draws(self):
        model = BenchmarkModel(self, "dtmc/coupon/coupon.5-2.jani","","", ModelType.DTMC,"PGCL","classic probabilistic programming example")
        sequence = BenchmarkSequence(model, "exp_draws", PropertyType.EXPECTED_REWARD, {"B": 5})
        BenchmarkInstance(sequence, {})
    
    def add_crowds_positive(self):
        model = BenchmarkModel(self, "dtmc/crowds/crowds.jani","dtmc/crowds/crowds.props","dtmc/crowds/crowds.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "positive", PropertyType.REACHABILITY, {"TotalRuns": 6, "CrowdSize": 20})
        BenchmarkInstance(sequence, {})
    
    def add_egl_messagesA(self):
        model = BenchmarkModel(self, "dtmc/egl/egl.jani","dtmc/egl/egl.props","dtmc/egl/egl.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "messagesA", PropertyType.EXPECTED_REWARD, {"N": 15, "L": 8})
        BenchmarkInstance(sequence, {})
    
    def add_egl_messagesB(self):
        model = BenchmarkModel(self, "dtmc/egl/egl.jani","dtmc/egl/egl.props","dtmc/egl/egl.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "messagesB", PropertyType.EXPECTED_REWARD, {"N": 10, "L": 8})
        BenchmarkInstance(sequence, {})
    
    def add_egl_unfairA(self):
        model = BenchmarkModel(self, "dtmc/egl/egl.jani","dtmc/egl/egl.props","dtmc/egl/egl.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "unfairA", PropertyType.REACHABILITY, {"N": 15, "L": 4})
        BenchmarkInstance(sequence, {})
    
    def add_egl_unfairB(self):
        model = BenchmarkModel(self, "dtmc/egl/egl.jani","dtmc/egl/egl.props","dtmc/egl/egl.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "unfairB", PropertyType.REACHABILITY, {"N": 20, "L": 4})
        BenchmarkInstance(sequence, {})
    
    def add_haddad_monmege_target(self):
        model = BenchmarkModel(self, "dtmc/haddad-monmege/haddad-monmege.jani","dtmc/haddad-monmege/haddad-monmege.prctl","dtmc/haddad-monmege/haddad-monmege.pm", ModelType.DTMC,"PRISM","adversarial example for value iteration")
        sequence = BenchmarkSequence(model, "target", PropertyType.REACHABILITY, {"N": 20, "p": 0.7})
        BenchmarkInstance(sequence, {})
    
    def add_herman_steps(self):
        model = BenchmarkModel(self, "dtmc/herman/herman.11.jani","dtmc/herman/herman.props","dtmc/herman/herman.11.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "steps", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_leader_sync_eventually_elected(self):
        model = BenchmarkModel(self, "dtmc/leader_sync/leader_sync.4-4.jani","dtmc/leader_sync/leader_sync.props","dtmc/leader_sync/leader_sync.4-4.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually_elected", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_leader_sync_time(self):
        model = BenchmarkModel(self, "dtmc/leader_sync/leader_sync.5-4.jani","dtmc/leader_sync/leader_sync.props","dtmc/leader_sync/leader_sync.5-4.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_nand_reliable(self):
        model = BenchmarkModel(self, "dtmc/nand/nand.jani","dtmc/nand/nand.props","dtmc/nand/nand.prism", ModelType.DTMC,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "reliable", PropertyType.REACHABILITY, {"N": 40, "K": 1})
        BenchmarkInstance(sequence, {})
    
    def add_oscillators_time_to_synch(self):
        model = BenchmarkModel(self, "dtmc/oscillators/oscillators.7-10-0.1-1.jani","dtmc/oscillators/oscillators.props","dtmc/oscillators/oscillators.7-10-0.1-1.prism", ModelType.DTMC,"PRISM","large fan-out from initial state")
        sequence = BenchmarkSequence(model, "time_to_synch", PropertyType.EXPECTED_REWARD, {"mu": 0.1, "lambda": 1.0})
        BenchmarkInstance(sequence, {})
    
    def add_oscillators_power_consumption(self):
        model = BenchmarkModel(self, "dtmc/oscillators/oscillators.8-10-0.1-1.jani","dtmc/oscillators/oscillators.props","dtmc/oscillators/oscillators.8-10-0.1-1.prism", ModelType.DTMC,"PRISM","large fan-out from initial state")
        sequence = BenchmarkSequence(model, "power_consumption", PropertyType.EXPECTED_REWARD, {"mu": 0.1, "lambda": 1.0})
        BenchmarkInstance(sequence, {})
    
    def add_bitcoin_attack_T_MWinMin(self):
        model = BenchmarkModel(self, "ma/bitcoin-attack/bitcoin-attack.jani","","", ModelType.MA,"Modest","")
        sequence = BenchmarkSequence(model, "T_MWinMin", PropertyType.EXPECTED_TIME, {"MALICIOUS": 20, "CD": 6})
        BenchmarkInstance(sequence, {})
    
    def add_breakdown_queues_Min(self):
        model = BenchmarkModel(self, "ma/breakdown-queues/breakdown-queues.jani","","", ModelType.MA,"Modest","")
        sequence = BenchmarkSequence(model, "Min", PropertyType.REACHABILITY, {"K": 64})
        BenchmarkInstance(sequence, {})
    
    def add_breakdown_queues_Max(self):
        model = BenchmarkModel(self, "ma/breakdown-queues/breakdown-queues.jani","","", ModelType.MA,"Modest","")
        sequence = BenchmarkSequence(model, "Max", PropertyType.REACHABILITY, {"K": 16})
        BenchmarkInstance(sequence, {})
    
    def add_dpm_PminQueuesFull(self):
        model = BenchmarkModel(self, "ma/dpm/dpm.jani","","", ModelType.MA,"Modest","scalable nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PminQueuesFull", PropertyType.REACHABILITY, {"N": 6, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_dpm_PmaxQueuesFull(self):
        model = BenchmarkModel(self, "ma/dpm/dpm.jani","","", ModelType.MA,"Modest","scalable nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PmaxQueuesFull", PropertyType.REACHABILITY, {"N": 4, "C": 4, "TIME_BOUND": 25})
        BenchmarkInstance(sequence, {})
    
    def add_dpm_PminQueue1Full(self):
        model = BenchmarkModel(self, "ma/dpm/dpm.jani","","", ModelType.MA,"Modest","scalable nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PminQueue1Full", PropertyType.REACHABILITY, {"N": 6, "C": 8, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_dpm_PmaxQueue1Full(self):
        model = BenchmarkModel(self, "ma/dpm/dpm.jani","","", ModelType.MA,"Modest","scalable nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PmaxQueue1Full", PropertyType.REACHABILITY, {"N": 8, "C": 6, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_dpm_TminQueuesFull(self):
        model = BenchmarkModel(self, "ma/dpm/dpm.jani","","", ModelType.MA,"Modest","scalable nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "TminQueuesFull", PropertyType.EXPECTED_TIME, {"N": 6, "C": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_erlang_PminReach(self):
        model = BenchmarkModel(self, "ma/erlang/erlang.jani","","", ModelType.MA,"Modest","scalable sanity check model")
        sequence = BenchmarkSequence(model, "PminReach", PropertyType.REACHABILITY, {"K": 5000, "R": 100, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_erlang_TminReach(self):
        model = BenchmarkModel(self, "ma/erlang/erlang.jani","","", ModelType.MA,"Modest","scalable sanity check model")
        sequence = BenchmarkSequence(model, "TminReach", PropertyType.EXPECTED_TIME, {"K": 10, "R": 10, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_flexible_manufacturing_M2Fail_E(self):
        model = BenchmarkModel(self, "ma/flexible-manufacturing/flexible-manufacturing.9.jani","","", ModelType.MA,"GreatSPN","small symbolic representation")
        sequence = BenchmarkSequence(model, "M2Fail_E", PropertyType.EXPECTED_TIME, {"T": 1})
        BenchmarkInstance(sequence, {})
    
    def add_flexible_manufacturing_M3Fail_E(self):
        model = BenchmarkModel(self, "ma/flexible-manufacturing/flexible-manufacturing.9.jani","","", ModelType.MA,"GreatSPN","small symbolic representation")
        sequence = BenchmarkSequence(model, "M3Fail_E", PropertyType.EXPECTED_TIME, {"T": 1})
        BenchmarkInstance(sequence, {})
    
    def add_ftwc_ReachMinIsOne(self):
        model = BenchmarkModel(self, "ma/ftwc/ftwc.jani","","", ModelType.MA,"Modest","fault-tolerant queueing system")
        sequence = BenchmarkSequence(model, "ReachMinIsOne", PropertyType.REACHABILITY, {"N": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_ftwc_TimeMin(self):
        model = BenchmarkModel(self, "ma/ftwc/ftwc.jani","","", ModelType.MA,"Modest","fault-tolerant queueing system")
        sequence = BenchmarkSequence(model, "TimeMin", PropertyType.EXPECTED_TIME, {"N": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_ftwc_TimeMax(self):
        model = BenchmarkModel(self, "ma/ftwc/ftwc.jani","","", ModelType.MA,"Modest","fault-tolerant queueing system")
        sequence = BenchmarkSequence(model, "TimeMax", PropertyType.EXPECTED_TIME, {"N": 4, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_jobs_completiontime(self):
        model = BenchmarkModel(self, "ma/jobs/jobs.10-3.jani","","", ModelType.MA,"PRISM-MA","stochastic scheduling problem")
        sequence = BenchmarkSequence(model, "completiontime", PropertyType.EXPECTED_TIME, {})
        BenchmarkInstance(sequence, {})
    
    def add_jobs_avgtime(self):
        model = BenchmarkModel(self, "ma/jobs/jobs.15-3.jani","","", ModelType.MA,"PRISM-MA","stochastic scheduling problem")
        sequence = BenchmarkSequence(model, "avgtime", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_polling_system_PminBothFullIsOne(self):
        model = BenchmarkModel(self, "ma/polling-system/polling-system.jani","","", ModelType.MA,"Modest","small nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PminBothFullIsOne", PropertyType.REACHABILITY, {"JOB_TYPES": 3, "C": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_polling_system_TminBothFull(self):
        model = BenchmarkModel(self, "ma/polling-system/polling-system.jani","","", ModelType.MA,"Modest","small nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "TminBothFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_polling_system_TmaxBothFull(self):
        model = BenchmarkModel(self, "ma/polling-system/polling-system.jani","","", ModelType.MA,"Modest","small nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "TmaxBothFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_readers_writers_pr_many_requests(self):
        model = BenchmarkModel(self, "ma/readers-writers/readers-writers.40.jani","","", ModelType.MA,"GreatSPN","standard GSPN example")
        sequence = BenchmarkSequence(model, "pr_many_requests", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_readers_writers_exp_time_many_requests(self):
        model = BenchmarkModel(self, "ma/readers-writers/readers-writers.40.jani","","", ModelType.MA,"GreatSPN","standard GSPN example")
        sequence = BenchmarkSequence(model, "exp_time_many_requests", PropertyType.EXPECTED_TIME, {})
        BenchmarkInstance(sequence, {})
    
    def add_readers_writers_pr_network(self):
        model = BenchmarkModel(self, "ma/readers-writers/readers-writers.20.jani","","", ModelType.MA,"GreatSPN","standard GSPN example")
        sequence = BenchmarkSequence(model, "pr_network", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_reentrant_queues_PminBothQueuesFullIsOne(self):
        model = BenchmarkModel(self, "ma/reentrant-queues/reentrant-queues.jani","","", ModelType.MA,"Modest","asymmetric nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "PminBothQueuesFullIsOne", PropertyType.REACHABILITY, {"JOB_TYPES": 3, "C_LEFT": 3, "C_RIGHT": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_reentrant_queues_TminBothQueuesFull(self):
        model = BenchmarkModel(self, "ma/reentrant-queues/reentrant-queues.jani","","", ModelType.MA,"Modest","asymmetric nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "TminBothQueuesFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C_LEFT": 3, "C_RIGHT": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_reentrant_queues_TmaxBothQueuesFull(self):
        model = BenchmarkModel(self, "ma/reentrant-queues/reentrant-queues.jani","","", ModelType.MA,"Modest","asymmetric nondeterministic queueing system")
        sequence = BenchmarkSequence(model, "TmaxBothQueuesFull", PropertyType.EXPECTED_TIME, {"JOB_TYPES": 3, "C_LEFT": 3, "C_RIGHT": 3, "TIME_BOUND": 5})
        BenchmarkInstance(sequence, {})
    
    def add_stream_exp_buffertime(self):
        model = BenchmarkModel(self, "ma/stream/stream.jani","","", ModelType.MA,"PRISM-MA","simple scalable planning benchmark")
        sequence = BenchmarkSequence(model, "exp_buffertime", PropertyType.EXPECTED_REWARD, {"N": 10})
        BenchmarkInstance(sequence, {})
    
    def add_stream_exp_restarts(self):
        model = BenchmarkModel(self, "ma/stream/stream.jani","","", ModelType.MA,"PRISM-MA","simple scalable planning benchmark")
        sequence = BenchmarkSequence(model, "exp_restarts", PropertyType.EXPECTED_REWARD, {"N": 100})
        BenchmarkInstance(sequence, {})
    
    def add_stream_pr_underrun(self):
        model = BenchmarkModel(self, "ma/stream/stream.jani","","", ModelType.MA,"PRISM-MA","simple scalable planning benchmark")
        sequence = BenchmarkSequence(model, "pr_underrun", PropertyType.REACHABILITY, {"N": 10})
        BenchmarkInstance(sequence, {})
    
    def add_vgs_MaxPrReachFailed(self):
        model = BenchmarkModel(self, "ma/vgs/vgs.5.jani","","", ModelType.MA,"Galileo","industrial case study")
        sequence = BenchmarkSequence(model, "MaxPrReachFailed", PropertyType.REACHABILITY, {"TIME_BOUND": 10000})
        BenchmarkInstance(sequence, {})
    
    def add_vgs_MinExpTimeFailed(self):
        model = BenchmarkModel(self, "ma/vgs/vgs.4.jani","","", ModelType.MA,"Galileo","industrial case study")
        sequence = BenchmarkSequence(model, "MinExpTimeFailed", PropertyType.EXPECTED_TIME, {"TIME_BOUND": 10000})
        BenchmarkInstance(sequence, {})
    
    def add_beb_LineSeized(self):
        model = BenchmarkModel(self, "mdp/beb/beb.3-4.jani","","", ModelType.MDP,"Modest","")
        sequence = BenchmarkSequence(model, "LineSeized", PropertyType.REACHABILITY, {"N": 3})
        BenchmarkInstance(sequence, {})
    
    def add_beb_GaveUp(self):
        model = BenchmarkModel(self, "mdp/beb/beb.3-4.jani","","", ModelType.MDP,"Modest","")
        sequence = BenchmarkSequence(model, "GaveUp", PropertyType.REACHABILITY, {"N": 3})
        BenchmarkInstance(sequence, {})
    
    def add_blocksworld_goal(self):
        model = BenchmarkModel(self, "mdp/blocksworld/blocksworld.10.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_boxworld_goal(self):
        model = BenchmarkModel(self, "mdp/boxworld/boxworld.10-5.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_cdrive_goal(self):
        model = BenchmarkModel(self, "mdp/cdrive/cdrive.6.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_consensus_c1(self):
        model = BenchmarkModel(self, "mdp/consensus/consensus.2.jani","mdp/consensus/consensus.props","mdp/consensus/consensus.2.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "c1", PropertyType.REACHABILITY, {"K": 4})
        BenchmarkInstance(sequence, {})
    
    def add_consensus_c2(self):
        model = BenchmarkModel(self, "mdp/consensus/consensus.4.jani","mdp/consensus/consensus.props","mdp/consensus/consensus.4.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "c2", PropertyType.REACHABILITY, {"K": 4})
        BenchmarkInstance(sequence, {})
    
    def add_consensus_disagree(self):
        model = BenchmarkModel(self, "mdp/consensus/consensus.10.jani","mdp/consensus/consensus.props","mdp/consensus/consensus.10.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "disagree", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_consensus_steps_max(self):
        model = BenchmarkModel(self, "mdp/consensus/consensus.6.jani","mdp/consensus/consensus.props","mdp/consensus/consensus.6.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "steps_max", PropertyType.EXPECTED_REWARD, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_consensus_steps_min(self):
        model = BenchmarkModel(self, "mdp/consensus/consensus.8.jani","mdp/consensus/consensus.props","mdp/consensus/consensus.8.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "steps_min", PropertyType.EXPECTED_REWARD, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_csma_all_before_max(self):
        model = BenchmarkModel(self, "mdp/csma/csma.4-4.jani","mdp/csma/csma.props","mdp/csma/csma.4-4.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "all_before_max", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_csma_all_before_min(self):
        model = BenchmarkModel(self, "mdp/csma/csma.2-4.jani","mdp/csma/csma.props","mdp/csma/csma.2-4.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "all_before_min", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_csma_some_before(self):
        model = BenchmarkModel(self, "mdp/csma/csma.3-4.jani","mdp/csma/csma.props","mdp/csma/csma.3-4.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "some_before", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_csma_time_max(self):
        model = BenchmarkModel(self, "mdp/csma/csma.3-6.jani","mdp/csma/csma.props","mdp/csma/csma.3-6.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_csma_time_min(self):
        model = BenchmarkModel(self, "mdp/csma/csma.3-2.jani","mdp/csma/csma.props","mdp/csma/csma.3-2.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {})
        BenchmarkInstance(sequence, {})
    
    def add_eajs_ExpUtil(self):
        model = BenchmarkModel(self, "mdp/eajs/eajs.2.jani","mdp/eajs/eajs.props","mdp/eajs/eajs.2.prism", ModelType.MDP,"PRISM","reward-bounded properties")
        sequence = BenchmarkSequence(model, "ExpUtil", PropertyType.EXPECTED_REWARD, {"energy_capacity": 100, "B": 5})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_MinFailed(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MinFailed", PropertyType.REACHABILITY, {"ITERATIONS": 100})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_MinOffline1(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MinOffline1", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_MaxOffline1(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MaxOffline1", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_MinOffline2(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MinOffline2", PropertyType.REACHABILITY, {"ITERATIONS": 2})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_MaxOffline2(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MaxOffline2", PropertyType.REACHABILITY, {"ITERATIONS": 100})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_MinOffline3(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MinOffline3", PropertyType.REACHABILITY, {"ITERATIONS": 50})
        BenchmarkInstance(sequence, {})
    
    def add_echoring_MaxOffline3(self):
        model = BenchmarkModel(self, "mdp/echoring/echoring.jani","","", ModelType.MDP,"Modest","industrial protocol, spurious nondeterminism")
        sequence = BenchmarkSequence(model, "MaxOffline3", PropertyType.REACHABILITY, {"ITERATIONS": 100})
        BenchmarkInstance(sequence, {})
    
    def add_elevators_goal(self):
        model = BenchmarkModel(self, "mdp/elevators/elevators.b-3-3.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_exploding_blocksworld_goal(self):
        model = BenchmarkModel(self, "mdp/exploding-blocksworld/exploding-blocksworld.10.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_elected(self):
        model = BenchmarkModel(self, "mdp/firewire/firewire.true.jani","mdp/firewire/firewire.true.props","mdp/firewire/firewire.true.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "elected", PropertyType.REACHABILITY, {"delay": 36, "deadline": 400})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_time_max(self):
        model = BenchmarkModel(self, "mdp/firewire/firewire.true.jani","mdp/firewire/firewire.true.props","mdp/firewire/firewire.true.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_time_min(self):
        model = BenchmarkModel(self, "mdp/firewire/firewire.true.jani","mdp/firewire/firewire.true.props","mdp/firewire/firewire.true.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {"delay": 3, "deadline": 600})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_time_sending(self):
        model = BenchmarkModel(self, "mdp/firewire/firewire.false.jani","mdp/firewire/firewire.false.props","mdp/firewire/firewire.false.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_sending", PropertyType.EXPECTED_REWARD, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_abst_elected(self):
        model = BenchmarkModel(self, "mdp/firewire_abst/firewire_abst.jani","mdp/firewire_abst/firewire_abst.props","mdp/firewire_abst/firewire_abst.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "elected", PropertyType.REACHABILITY, {"delay": 3})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_abst_rounds(self):
        model = BenchmarkModel(self, "mdp/firewire_abst/firewire_abst.jani","mdp/firewire_abst/firewire_abst.props","mdp/firewire_abst/firewire_abst.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "rounds", PropertyType.EXPECTED_REWARD, {"delay": 36})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_abst_time_max(self):
        model = BenchmarkModel(self, "mdp/firewire_abst/firewire_abst.jani","mdp/firewire_abst/firewire_abst.props","mdp/firewire_abst/firewire_abst.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {"delay": 3})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_abst_time_min(self):
        model = BenchmarkModel(self, "mdp/firewire_abst/firewire_abst.jani","mdp/firewire_abst/firewire_abst.props","mdp/firewire_abst/firewire_abst.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {"delay": 36})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_dl_deadline(self):
        model = BenchmarkModel(self, "mdp/firewire_dl/firewire_dl.jani","mdp/firewire_dl/firewire_dl.props","mdp/firewire_dl/firewire_dl.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "deadline", PropertyType.REACHABILITY, {"delay": 3, "deadline": 200})
        BenchmarkInstance(sequence, {})
    
    def add_ij_stable(self):
        model = BenchmarkModel(self, "mdp/ij/ij.40.jani","mdp/ij/ij.40.props","mdp/ij/ij.40.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "stable", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_pacman_crash(self):
        model = BenchmarkModel(self, "mdp/pacman/pacman.jani","mdp/pacman/pacman.props","mdp/pacman/pacman.nm", ModelType.MDP,"PRISM","learned probabilities")
        sequence = BenchmarkSequence(model, "crash", PropertyType.REACHABILITY, {"MAXSTEPS": 100})
        BenchmarkInstance(sequence, {})
    
    def add_philosophers_mdp_eat(self):
        model = BenchmarkModel(self, "mdp/philosophers-mdp/philosophers-mdp.30.jani","mdp/philosophers-mdp/philosophers-mdp.30.props","mdp/philosophers-mdp/philosophers-mdp.30.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "eat", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_pnueli_zuck_live(self):
        model = BenchmarkModel(self, "mdp/pnueli-zuck/pnueli-zuck.3.jani","mdp/pnueli-zuck/pnueli-zuck.props","mdp/pnueli-zuck/pnueli-zuck.3.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "live", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_rabin_live(self):
        model = BenchmarkModel(self, "mdp/rabin/rabin.3.jani","mdp/rabin/rabin.3.props","mdp/rabin/rabin.3.prism", ModelType.MDP,"PRISM","PRISM case study")
        sequence = BenchmarkSequence(model, "live", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_random_predicates_goal(self):
        model = BenchmarkModel(self, "mdp/random-predicates/random-predicates.a.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_rectangle_tireworld_goal(self):
        model = BenchmarkModel(self, "mdp/rectangle-tireworld/rectangle-tireworld.30.jani.gz","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_tireworld_goal(self):
        model = BenchmarkModel(self, "mdp/tireworld/tireworld.25.jani","","", ModelType.MDP,"PPDDL","IPPC 2006 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_triangle_tireworld_goal(self):
        model = BenchmarkModel(self, "mdp/triangle-tireworld/triangle-tireworld.9.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_collisions(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.2.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.2.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "collisions", PropertyType.REACHABILITY, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_cost_max(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.0.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.0.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "cost_max", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_cost_min(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.4.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.4.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "cost_min", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_num_collisions(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.2.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.2.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "num_collisions", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_sent(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.1.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.1.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "sent", PropertyType.REACHABILITY, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_time_max(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.6.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.6.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_max", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_time_min(self):
        model = BenchmarkModel(self, "mdp/wlan/wlan.6.jani","mdp/wlan/wlan.props","mdp/wlan/wlan.6.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "time_min", PropertyType.EXPECTED_REWARD, {"COL": 0})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_dl_deadline(self):
        model = BenchmarkModel(self, "mdp/wlan_dl/wlan_dl.2.jani","mdp/wlan_dl/wlan_dl.props","mdp/wlan_dl/wlan_dl.2.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "deadline", PropertyType.REACHABILITY, {"deadline": 80})
        BenchmarkInstance(sequence, {})
    
    def add_zenotravel_goal(self):
        model = BenchmarkModel(self, "mdp/zenotravel/zenotravel.6-5-3.jani","","", ModelType.MDP,"PPDDL","IPPC 2008 benchmark")
        sequence = BenchmarkSequence(model, "goal", PropertyType.REACHABILITY, {})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_correct_max(self):
        model = BenchmarkModel(self, "mdp/zeroconf/zeroconf.jani","mdp/zeroconf/zeroconf.props","mdp/zeroconf/zeroconf.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "correct_max", PropertyType.REACHABILITY, {"N": 1000, "K": 2, "reset": False})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_correct_min(self):
        model = BenchmarkModel(self, "mdp/zeroconf/zeroconf.jani","mdp/zeroconf/zeroconf.props","mdp/zeroconf/zeroconf.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "correct_min", PropertyType.REACHABILITY, {"N": 1000, "K": 8, "reset": False})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_dl_deadline_max(self):
        model = BenchmarkModel(self, "mdp/zeroconf_dl/zeroconf_dl.jani","mdp/zeroconf_dl/zeroconf_dl.props","mdp/zeroconf_dl/zeroconf_dl.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "deadline_max", PropertyType.REACHABILITY, {"N": 1000, "K": 1, "reset": True, "deadline": 20})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_dl_deadline_min(self):
        model = BenchmarkModel(self, "mdp/zeroconf_dl/zeroconf_dl.jani","mdp/zeroconf_dl/zeroconf_dl.props","mdp/zeroconf_dl/zeroconf_dl.prism", ModelType.MDP,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "deadline_min", PropertyType.REACHABILITY, {"N": 1000, "K": 1, "reset": True, "deadline": 20})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_T_1(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "T_1", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_T_2(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "T_2", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_T_A1(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "T_A1", PropertyType.REACHABILITY, {"N": 64, "MAX": 12, "TD": 32, "TIME_BOUND": 256})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_T_A2(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "T_A2", PropertyType.REACHABILITY, {"N": 64, "MAX": 12, "TD": 32, "TIME_BOUND": 256})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_P_A(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "P_A", PropertyType.REACHABILITY, {"N": 64, "MAX": 12, "TD": 32, "TIME_BOUND": 256})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_P_B(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "P_B", PropertyType.REACHABILITY, {"N": 64, "MAX": 12, "TD": 32, "TIME_BOUND": 256})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_P_1(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "P_1", PropertyType.REACHABILITY, {"N": 64, "MAX": 12, "TD": 32, "TIME_BOUND": 256})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_P_2(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "P_2", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_P_3(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "P_3", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_P_4(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "P_4", PropertyType.REACHABILITY, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_Emax(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "Emax", PropertyType.EXPECTED_TIME, {"N": 16, "MAX": 2, "TD": 1, "TIME_BOUND": 64})
        BenchmarkInstance(sequence, {})
    
    def add_brp_pta_Emin(self):
        model = BenchmarkModel(self, "pta/brp-pta/brp-pta.jani","","", ModelType.PTA,"Modest","scalable in multiple dimensions")
        sequence = BenchmarkSequence(model, "Emin", PropertyType.EXPECTED_TIME, {"N": 64, "MAX": 12, "TD": 32, "TIME_BOUND": 256})
        BenchmarkInstance(sequence, {})
    
    def add_csma_pta_collisions(self):
        model = BenchmarkModel(self, "pta/csma-pta/csma-pta.jani","pta/csma-pta/csma-pta.props","pta/csma-pta/csma-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "collisions", PropertyType.REACHABILITY, {"K": 4, "COL": 8})
        BenchmarkInstance(sequence, {})
    
    def add_csma_abst_pta_eventually(self):
        model = BenchmarkModel(self, "pta/csma_abst-pta/csma_abst-pta.jani","pta/csma_abst-pta/csma_abst-pta.props","pta/csma_abst-pta/csma_abst-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"K": 1, "T": 3000})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_pta_eventually(self):
        model = BenchmarkModel(self, "pta/firewire-pta/firewire-pta.jani","pta/firewire-pta/firewire-pta.props","pta/firewire-pta/firewire-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"delay": 360, "T": 5000})
        BenchmarkInstance(sequence, {})
    
    def add_firewire_abst_pta_eventually(self):
        model = BenchmarkModel(self, "pta/firewire_abst-pta/firewire_abst-pta.jani","pta/firewire_abst-pta/firewire_abst-pta.props","pta/firewire_abst-pta/firewire_abst-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"delay": 30, "T": 15000})
        BenchmarkInstance(sequence, {})
    
    def add_repudiation_honest_eventually(self):
        model = BenchmarkModel(self, "pta/repudiation_honest/repudiation_honest.jani","pta/repudiation_honest/repudiation_honest.props","pta/repudiation_honest/repudiation_honest.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"T": 80})
        BenchmarkInstance(sequence, {})
    
    def add_repudiation_malicious_eventually(self):
        model = BenchmarkModel(self, "pta/repudiation_malicious/repudiation_malicious.jani","pta/repudiation_malicious/repudiation_malicious.props","pta/repudiation_malicious/repudiation_malicious.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "eventually", PropertyType.REACHABILITY, {"T": 10})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_large_P_1(self):
        model = BenchmarkModel(self, "pta/wlan-large/wlan-large.jani","","", ModelType.PTA,"Modest","")
        sequence = BenchmarkSequence(model, "P_1", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_large_P_min(self):
        model = BenchmarkModel(self, "pta/wlan-large/wlan-large.jani","","", ModelType.PTA,"Modest","")
        sequence = BenchmarkSequence(model, "P_min", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_large_P_max(self):
        model = BenchmarkModel(self, "pta/wlan-large/wlan-large.jani","","", ModelType.PTA,"Modest","")
        sequence = BenchmarkSequence(model, "P_max", PropertyType.REACHABILITY, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_large_E_and(self):
        model = BenchmarkModel(self, "pta/wlan-large/wlan-large.jani","","", ModelType.PTA,"Modest","")
        sequence = BenchmarkSequence(model, "E_and", PropertyType.EXPECTED_TIME, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_large_E_or(self):
        model = BenchmarkModel(self, "pta/wlan-large/wlan-large.jani","","", ModelType.PTA,"Modest","")
        sequence = BenchmarkSequence(model, "E_or", PropertyType.EXPECTED_TIME, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_wlan_large_E_1(self):
        model = BenchmarkModel(self, "pta/wlan-large/wlan-large.jani","","", ModelType.PTA,"Modest","")
        sequence = BenchmarkSequence(model, "E_1", PropertyType.EXPECTED_REWARD, {"K": 2})
        BenchmarkInstance(sequence, {})
    
    def add_zeroconf_pta_incorrect(self):
        model = BenchmarkModel(self, "pta/zeroconf-pta/zeroconf-pta.jani","pta/zeroconf-pta/zeroconf-pta.props","pta/zeroconf-pta/zeroconf-pta.prism", ModelType.PTA,"PRISM","PRISM benchmark")
        sequence = BenchmarkSequence(model, "incorrect", PropertyType.REACHABILITY, {"T": 100})
        BenchmarkInstance(sequence, {})
