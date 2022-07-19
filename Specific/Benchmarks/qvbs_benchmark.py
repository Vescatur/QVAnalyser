from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Storm.storm_tool import StormTool

# This class has been generated using _GenerateBenchmarkFromQVBS.py
class QvbsBenchmark(Benchmark):
    def __init__(self):
        super().__init__()
        
        self.add_benchmark_instances()
        
        stormTool = StormTool()
        self.tools.append(stormTool)
        self.algorithms.append(stormTool.interval_iteration)
        
        modestTool = ModestTool()
        self.tools.append(modestTool)
        self.algorithms.append(modestTool.interval_iteration)
    
    def add_benchmark_instances(self):
        self.add_cluster()
        self.add_embedded()
        self.add_fms()
        self.add_hill_toggle()
        self.add_kanban()
        self.add_majority()
        self.add_mapk_cascade()
        self.add_p53()
        self.add_philosophers()
        self.add_polling()
        self.add_speed_ind()
        self.add_tandem()
        self.add_toggle_switch()
        self.add_bluetooth()
        self.add_brp()
        self.add_coupon()
        self.add_crowds()
        self.add_egl()
        self.add_haddad_monmege()
        self.add_herman()
        self.add_leader_sync()
        self.add_nand()
        self.add_oscillators()
        self.add_bitcoin_attack()
        self.add_breakdown_queues()
        self.add_cabinets()
        self.add_dpm()
        self.add_erlang()
        self.add_flexible_manufacturing()
        self.add_ftpp()
        self.add_ftwc()
        self.add_hecs()
        self.add_jobs()
        self.add_mcs()
        self.add_polling_system()
        self.add_readers_writers()
        self.add_reentrant_queues()
        self.add_sf()
        self.add_sms()
        self.add_stream()
        self.add_vgs()
        self.add_beb()
        self.add_blocksworld()
        self.add_boxworld()
        self.add_cdrive()
        self.add_consensus()
        self.add_csma()
        self.add_eajs()
        self.add_echoring()
        self.add_elevators()
        self.add_exploding_blocksworld()
        self.add_firewire()
        self.add_firewire_abst()
        self.add_firewire_dl()
        self.add_ij()
        self.add_pacman()
        self.add_philosophers_mdp()
        self.add_pnueli_zuck()
        self.add_rabin()
        self.add_random_predicates()
        self.add_rectangle_tireworld()
        self.add_resource_gathering()
        self.add_tireworld()
        self.add_triangle_tireworld()
        self.add_wlan()
        self.add_wlan_dl()
        self.add_zenotravel()
        self.add_zeroconf()
        self.add_zeroconf_dl()
        self.add_brp_pta()
        self.add_csma_pta()
        self.add_csma_abst_pta()
        self.add_firewire_pta()
        self.add_firewire_abst_pta()
        self.add_repudiation_honest()
        self.add_repudiation_malicious()
        self.add_wlan_large()
        self.add_zeroconf_pta()
    
    def add_cluster(self):
        properties = [['below_min','exp-reward-time-bounded'], ['operational','exp-reward-time-instant'], ['premium_steady','steady-state-prob'], ['qos1','prob-reach-time-bounded'], ['qos2','prob-reach-time-bounded'], ['qos3','prob-reach-time-bounded'], ['qos4','prob-reach-time-bounded'], ['repairs','exp-reward-time-bounded']]
        self.add_model('ctmc/cluster/cluster.jani',"cluster.props","cluster.prism","ctmc","PRISM","PRISM benchmark", properties, [{'N': 2, 'T': 2000, 't': 20},{'N': 4, 'T': 2000, 't': 20},{'N': 8, 'T': 2000, 't': 20},{'N': 16, 'T': 2000, 't': 20},{'N': 32, 'T': 2000, 't': 20},{'N': 64, 'T': 2000, 't': 20},{'N': 128, 'T': 2000, 't': 20},{'N': 256, 'T': 2000, 't': 20},{'N': 512, 'T': 2000, 't': 20}])
    
    def add_embedded(self):
        properties = [['actuators','prob-reach'], ['actuators_T','prob-reach-time-bounded'], ['danger_T','exp-reward-time-bounded'], ['danger_time','exp-reward'], ['down_T','exp-reward-time-bounded'], ['failure_T','prob-reach-time-bounded'], ['io','prob-reach'], ['io_T','prob-reach-time-bounded'], ['main','prob-reach'], ['main_T','prob-reach-time-bounded'], ['sensors','prob-reach'], ['sensors_T','prob-reach-time-bounded'], ['up_T','exp-reward-time-bounded'], ['up_time','exp-reward']]
        self.add_model('ctmc/embedded/embedded.jani',"embedded.props","embedded.prism","ctmc","PRISM","PRISM benchmark", properties, [{'MAX_COUNT': 2, 'T': 12},{'MAX_COUNT': 3, 'T': 12},{'MAX_COUNT': 4, 'T': 12},{'MAX_COUNT': 5, 'T': 12},{'MAX_COUNT': 6, 'T': 12},{'MAX_COUNT': 7, 'T': 12},{'MAX_COUNT': 8, 'T': 12}])
    
    def add_fms(self):
        properties = [['productivity','steady-state-reward']]
        self.add_model('ctmc/fms/fms.jani',"fms.props","fms.prism","ctmc","PRISM","PRISM benchmark", properties, [{'n': 1},{'n': 2},{'n': 3},{'n': 4},{'n': 5},{'n': 6},{'n': 7},{'n': 8},{'n': 9},{'n': 10}])
    
    def add_hill_toggle(self):
        properties = [['Switching','prob-reach-step-bounded'], ['RareEvent','prob-reach-step-bounded']]
        self.add_model('ctmc/hill-toggle/hill-toggle.jani',"","","ctmc","PRISM-∞","infinite-state biological model", properties, [{}])
    
    def add_kanban(self):
        properties = [['throughput','steady-state-reward']]
        self.add_model('ctmc/kanban/kanban.jani',"kanban.props","kanban.prism","ctmc","PRISM","PRISM benchmark", properties, [{'t': 1},{'t': 2},{'t': 3},{'t': 4},{'t': 5},{'t': 6},{'t': 7}])
    
    def add_majority(self):
        properties = [['change_state','prob-reach-time-bounded']]
        self.add_model('ctmc/majority/majority.jani',"majority.props","majority.prism","ctmc","PRISM","biological model", properties, [{'T': 2100}])
    
    def add_mapk_cascade(self):
        properties = [['activated_T','exp-reward-time-instant'], ['activated_time','exp-reward'], ['reactions','exp-reward-time-bounded']]
        self.add_model('ctmc/mapk_cascade/mapk_cascade.jani',"mapk_cascade.props","mapk_cascade.prism","ctmc","PRISM","PRISM benchmark", properties, [{'N': 1, 'T': 30},{'N': 2, 'T': 30},{'N': 3, 'T': 30},{'N': 4, 'T': 30},{'N': 5, 'T': 30},{'N': 6, 'T': 30},{'N': 7, 'T': 30},{'N': 8, 'T': 30}])
    
    def add_p53(self):
        properties = [['RareEvent1','prob-reach-step-bounded'], ['RareEvent2','prob-reach-step-bounded'], ['RareEvent3','prob-reach-step-bounded'], ['Steady1','steady-state-prob']]
        self.add_model('ctmc/p53/p53.jani',"","","ctmc","PRISM-∞","infinite-state biological model", properties, [{}])
    
    def add_philosophers(self):
        properties = [['MaxPrReachDeadlock','prob-reach'], ['MaxPrReachDeadlockTB','prob-reach-time-bounded'], ['MinExpTimeDeadlock','exp-time']]
        self.add_model('ctmc/philosophers/philosophers.4.jani',"","","ctmc","GreatSPN","small symbolic representation", properties, [{'TIME_BOUND': 1}])
        self.add_model('ctmc/philosophers/philosophers.12.jani',"","","ctmc","GreatSPN","small symbolic representation", properties, [{'TIME_BOUND': 1}])
        self.add_model('ctmc/philosophers/philosophers.16.jani',"","","ctmc","GreatSPN","small symbolic representation", properties, [{'TIME_BOUND': 1}])
        self.add_model('ctmc/philosophers/philosophers.20.jani',"","","ctmc","GreatSPN","small symbolic representation", properties, [{'TIME_BOUND': 1}])
        self.add_model('ctmc/philosophers/philosophers.24.jani',"","","ctmc","GreatSPN","small symbolic representation", properties, [{'TIME_BOUND': 1}])
        self.add_model('ctmc/philosophers/philosophers.28.jani',"","","ctmc","GreatSPN","small symbolic representation", properties, [{'TIME_BOUND': 1}])
        self.add_model('ctmc/philosophers/philosophers.32.jani',"","","ctmc","GreatSPN","small symbolic representation", properties, [{'TIME_BOUND': 1}])
    
    def add_polling(self):
        properties = [['s1','steady-state-prob'], ['s1_before_s2','prob-reach'], ['served','exp-reward-time-bounded'], ['station1_polled','prob-reach-time-bounded'], ['waiting','exp-reward-time-bounded']]
        self.add_model('ctmc/polling/polling.3.jani',"polling.props","polling.3.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.4.jani',"polling.props","polling.4.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.5.jani',"polling.props","polling.5.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.6.jani',"polling.props","polling.6.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.7.jani',"polling.props","polling.7.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.8.jani',"polling.props","polling.8.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.9.jani',"polling.props","polling.9.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.10.jani',"polling.props","polling.10.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.11.jani',"polling.props","polling.11.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.12.jani',"polling.props","polling.12.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.13.jani',"polling.props","polling.13.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.14.jani',"polling.props","polling.14.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.15.jani',"polling.props","polling.15.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.16.jani',"polling.props","polling.16.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.17.jani',"polling.props","polling.17.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.18.jani',"polling.props","polling.18.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.19.jani',"polling.props","polling.19.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
        self.add_model('ctmc/polling/polling.20.jani',"polling.props","polling.20.prism","ctmc","PRISM","PRISM benchmark", properties, [{'T': 16}])
    
    def add_speed_ind(self):
        properties = [['change_state','prob-reach-time-bounded']]
        self.add_model('ctmc/speed-ind/speed-ind.jani',"speed-ind.props","speed-ind.prism","ctmc","PRISM","biological model", properties, [{'T': 2100}])
    
    def add_tandem(self):
        properties = [['customers','steady-state-reward'], ['customers_T','exp-reward-time-instant'], ['first_queue','prob-reach-time-bounded'], ['network','prob-reach-time-bounded'], ['second_queue','prob-reach-time-bounded']]
        self.add_model('ctmc/tandem/tandem.jani',"tandem.props","tandem.prism","ctmc","PRISM","PRISM benchmark", properties, [{'c': 5, 'T': 1000, 't': 0.2},{'c': 7, 'T': 1000, 't': 0.2},{'c': 15, 'T': 1000, 't': 0.2},{'c': 31, 'T': 1000, 't': 0.2},{'c': 63, 'T': 1000, 't': 0.2},{'c': 127, 'T': 1000, 't': 0.2},{'c': 255, 'T': 1000, 't': 0.2},{'c': 511, 'T': 1000, 't': 0.2},{'c': 1023, 'T': 1000, 't': 0.2},{'c': 2047, 'T': 1000, 't': 0.2},{'c': 4095, 'T': 1000, 't': 0.2}])
    
    def add_toggle_switch(self):
        properties = [['change_state','prob-reach-time-bounded']]
        self.add_model('ctmc/toggle-switch/toggle-switch.jani',"toggle-switch.props","toggle-switch.prism","ctmc","PRISM","biological model", properties, [{'T': 2100}])
    
    def add_bluetooth(self):
        properties = [['time','exp-reward']]
        self.add_model('dtmc/bluetooth/bluetooth.jani',"bluetooth.props","bluetooth.prism","dtmc","PRISM","PRISM benchmark", properties, [{'mrec': 1},{'mrec': 2}])
    
    def add_brp(self):
        properties = [['p1','prob-reach'], ['p2','prob-reach'], ['p4','prob-reach']]
        self.add_model('dtmc/brp/brp.jani',"brp.props","brp.prism","dtmc","PRISM","PRISM benchmark", properties, [{'N': 16, 'MAX': 2},{'N': 16, 'MAX': 3},{'N': 16, 'MAX': 4},{'N': 16, 'MAX': 5},{'N': 32, 'MAX': 2},{'N': 32, 'MAX': 3},{'N': 32, 'MAX': 4},{'N': 32, 'MAX': 5},{'N': 64, 'MAX': 2},{'N': 64, 'MAX': 3},{'N': 64, 'MAX': 4},{'N': 64, 'MAX': 5}])
    
    def add_coupon(self):
        properties = [['collect_all','prob-reach'], ['exp_draws','exp-reward'], ['collect_all_bounded','prob-reach-reward-bounded']]
        self.add_model('dtmc/coupon/coupon.5-2.jani',"","","dtmc","PGCL","classic probabilistic programming example", properties, [{'B': 5}])
        self.add_model('dtmc/coupon/coupon.7-3.jani',"","","dtmc","PGCL","classic probabilistic programming example", properties, [{'B': 5}])
        self.add_model('dtmc/coupon/coupon.9-4.jani',"","","dtmc","PGCL","classic probabilistic programming example", properties, [{'B': 5}])
        self.add_model('dtmc/coupon/coupon.15-4.jani',"","","dtmc","PGCL","classic probabilistic programming example", properties, [{'B': 5}])
    
    def add_crowds(self):
        properties = [['positive','prob-reach']]
        self.add_model('dtmc/crowds/crowds.jani',"crowds.props","crowds.prism","dtmc","PRISM","PRISM benchmark", properties, [{'TotalRuns': 3, 'CrowdSize': 5},{'TotalRuns': 4, 'CrowdSize': 5},{'TotalRuns': 5, 'CrowdSize': 5},{'TotalRuns': 6, 'CrowdSize': 5},{'TotalRuns': 3, 'CrowdSize': 10},{'TotalRuns': 4, 'CrowdSize': 10},{'TotalRuns': 5, 'CrowdSize': 10},{'TotalRuns': 6, 'CrowdSize': 10},{'TotalRuns': 3, 'CrowdSize': 15},{'TotalRuns': 4, 'CrowdSize': 15},{'TotalRuns': 5, 'CrowdSize': 15},{'TotalRuns': 6, 'CrowdSize': 15},{'TotalRuns': 3, 'CrowdSize': 20},{'TotalRuns': 4, 'CrowdSize': 20},{'TotalRuns': 5, 'CrowdSize': 20},{'TotalRuns': 6, 'CrowdSize': 20}])
    
    def add_egl(self):
        properties = [['messagesA','exp-reward'], ['messagesB','exp-reward'], ['unfairA','prob-reach'], ['unfairB','prob-reach']]
        self.add_model('dtmc/egl/egl.jani',"egl.props","egl.prism","dtmc","PRISM","PRISM benchmark", properties, [{'N': 5, 'L': 2},{'N': 5, 'L': 4},{'N': 5, 'L': 6},{'N': 5, 'L': 8},{'N': 10, 'L': 2},{'N': 10, 'L': 4},{'N': 10, 'L': 6},{'N': 10, 'L': 8},{'N': 15, 'L': 2},{'N': 15, 'L': 4},{'N': 15, 'L': 6},{'N': 15, 'L': 8},{'N': 20, 'L': 2},{'N': 20, 'L': 4},{'N': 20, 'L': 6},{'N': 20, 'L': 8}])
    
    def add_haddad_monmege(self):
        properties = [['target','prob-reach'], ['exp_steps','exp-steps']]
        self.add_model('dtmc/haddad-monmege/haddad-monmege.jani',"haddad-monmege.prctl","haddad-monmege.pm","dtmc","PRISM","adversarial example for value iteration", properties, [{'N': 20, 'p': 0.7},{'N': 100, 'p': 0.7},{'N': 300, 'p': 0.7}])
    
    def add_herman(self):
        properties = [['steps','exp-reward']]
        self.add_model('dtmc/herman/herman.3.jani',"herman.props","herman.3.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.5.jani',"herman.props","herman.5.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.7.jani',"herman.props","herman.7.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.9.jani',"herman.props","herman.9.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.11.jani',"herman.props","herman.11.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.13.jani',"herman.props","herman.13.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.15.jani',"herman.props","herman.15.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.17.jani',"herman.props","herman.17.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.19.jani',"herman.props","herman.19.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/herman/herman.21.jani',"herman.props","herman.21.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
    
    def add_leader_sync(self):
        properties = [['eventually_elected','prob-reach'], ['time','exp-reward']]
        self.add_model('dtmc/leader_sync/leader_sync.3-2.jani',"leader_sync.props","leader_sync.3-2.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.3-3.jani',"leader_sync.props","leader_sync.3-3.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.3-4.jani',"leader_sync.props","leader_sync.3-4.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.4-2.jani',"leader_sync.props","leader_sync.4-2.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.4-3.jani',"leader_sync.props","leader_sync.4-3.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.4-4.jani',"leader_sync.props","leader_sync.4-4.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.5-2.jani',"leader_sync.props","leader_sync.5-2.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.5-3.jani',"leader_sync.props","leader_sync.5-3.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('dtmc/leader_sync/leader_sync.5-4.jani',"leader_sync.props","leader_sync.5-4.prism","dtmc","PRISM","PRISM benchmark", properties, [{}])
    
    def add_nand(self):
        properties = [['reliable','prob-reach']]
        self.add_model('dtmc/nand/nand.jani',"nand.props","nand.prism","dtmc","PRISM","PRISM benchmark", properties, [{'N': 20, 'K': 1},{'N': 20, 'K': 2},{'N': 20, 'K': 3},{'N': 20, 'K': 4},{'N': 40, 'K': 1},{'N': 40, 'K': 2},{'N': 40, 'K': 3},{'N': 40, 'K': 4},{'N': 60, 'K': 1},{'N': 60, 'K': 2},{'N': 60, 'K': 3},{'N': 60, 'K': 4}])
    
    def add_oscillators(self):
        properties = [['time_to_synch','exp-reward'], ['power_consumption','exp-reward']]
        self.add_model('dtmc/oscillators/oscillators.3-6-0.1-1.jani',"oscillators.props","oscillators.3-6-0.1-1.prism","dtmc","PRISM","large fan-out from initial state", properties, [{'mu': 0.1, 'lambda': 1.0}])
        self.add_model('dtmc/oscillators/oscillators.6-6-0.1-1.jani',"oscillators.props","oscillators.6-6-0.1-1.prism","dtmc","PRISM","large fan-out from initial state", properties, [{'mu': 0.1, 'lambda': 1.0}])
        self.add_model('dtmc/oscillators/oscillators.6-8-0.1-1.jani',"oscillators.props","oscillators.6-8-0.1-1.prism","dtmc","PRISM","large fan-out from initial state", properties, [{'mu': 0.1, 'lambda': 1.0}])
        self.add_model('dtmc/oscillators/oscillators.6-10-0.1-1.jani',"oscillators.props","oscillators.6-10-0.1-1.prism","dtmc","PRISM","large fan-out from initial state", properties, [{'mu': 0.1, 'lambda': 1.0}])
        self.add_model('dtmc/oscillators/oscillators.7-10-0.1-1.jani',"oscillators.props","oscillators.7-10-0.1-1.prism","dtmc","PRISM","large fan-out from initial state", properties, [{'mu': 0.1, 'lambda': 1.0}])
        self.add_model('dtmc/oscillators/oscillators.8-8-0.1-1.jani',"oscillators.props","oscillators.8-8-0.1-1.prism","dtmc","PRISM","large fan-out from initial state", properties, [{'mu': 0.1, 'lambda': 1.0}])
        self.add_model('dtmc/oscillators/oscillators.8-10-0.1-1.jani',"oscillators.props","oscillators.8-10-0.1-1.prism","dtmc","PRISM","large fan-out from initial state", properties, [{'mu': 0.1, 'lambda': 1.0}])
    
    def add_bitcoin_attack(self):
        properties = [['T_MWinMin','exp-time'], ['P_MWinMax','prob-reach-time-bounded']]
        self.add_model('ma/bitcoin-attack/bitcoin-attack.jani',"","","ma","Modest","", properties, [{'MALICIOUS': 20, 'CD': 6}])
    
    def add_breakdown_queues(self):
        properties = [['Min','prob-reach'], ['Max','prob-reach']]
        self.add_model('ma/breakdown-queues/breakdown-queues.jani',"","","ma","Modest","", properties, [{'K': 8},{'K': 16},{'K': 32},{'K': 64}])
    
    def add_cabinets(self):
        properties = [['Unreliability','prob-reach-time-bounded'], ['Unavailability','steady-state-prob']]
        self.add_model('ma/cabinets/cabinets.2-1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.2-1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.2-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.2-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.2-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.2-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.3-1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.3-1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.3-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.3-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.3-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.3-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.4-1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.4-1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.4-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.4-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.4-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/cabinets/cabinets.4-3-true.jani',"","","ma","Galileo","", properties, [{}])
    
    def add_dpm(self):
        properties = [['PminQueuesFull','prob-reach'], ['PmaxQueuesFull','prob-reach'], ['PminQueue1Full','prob-reach'], ['PmaxQueue1Full','prob-reach'], ['TminQueuesFull','exp-time'], ['PmaxQueuesFullBound','prob-reach-time-bounded'], ['SmaxQueuesFull','steady-state-prob']]
        self.add_model('ma/dpm/dpm.jani',"","","ma","Modest","scalable nondeterministic queueing system", properties, [{'N': 4, 'C': 4, 'TIME_BOUND': 5},{'N': 4, 'C': 4, 'TIME_BOUND': 25},{'N': 4, 'C': 6, 'TIME_BOUND': 25},{'N': 4, 'C': 6, 'TIME_BOUND': 50},{'N': 4, 'C': 6, 'TIME_BOUND': 100},{'N': 4, 'C': 8, 'TIME_BOUND': 5},{'N': 4, 'C': 8, 'TIME_BOUND': 25},{'N': 4, 'C': 8, 'TIME_BOUND': 100},{'N': 6, 'C': 4, 'TIME_BOUND': 5},{'N': 6, 'C': 6, 'TIME_BOUND': 5},{'N': 6, 'C': 8, 'TIME_BOUND': 5},{'N': 8, 'C': 4, 'TIME_BOUND': 5},{'N': 8, 'C': 6, 'TIME_BOUND': 5},{'N': 8, 'C': 8, 'TIME_BOUND': 5}])
    
    def add_erlang(self):
        properties = [['PminReach','prob-reach'], ['TminReach','exp-time'], ['PmaxReachBound','prob-reach-time-bounded'], ['SmaxNotReach','steady-state-prob']]
        self.add_model('ma/erlang/erlang.jani',"","","ma","Modest","scalable sanity check model", properties, [{'K': 10, 'R': 10, 'TIME_BOUND': 5},{'K': 5000, 'R': 10, 'TIME_BOUND': 5},{'K': 5000, 'R': 100, 'TIME_BOUND': 5},{'K': 5000, 'R': 100, 'TIME_BOUND': 50}])
    
    def add_flexible_manufacturing(self):
        properties = [['M2Fail_S','steady-state-prob'], ['M3Fail_S','steady-state-prob'], ['M2Fail_E','exp-time'], ['M3Fail_E','exp-time'], ['M2Fail_Pb','prob-reach-time-bounded'], ['M3Fail_Pb','prob-reach-time-bounded']]
        self.add_model('ma/flexible-manufacturing/flexible-manufacturing.3.jani',"","","ma","GreatSPN","small symbolic representation", properties, [{'T': 1}])
        self.add_model('ma/flexible-manufacturing/flexible-manufacturing.9.jani',"","","ma","GreatSPN","small symbolic representation", properties, [{'T': 1}])
        self.add_model('ma/flexible-manufacturing/flexible-manufacturing.21.jani',"","","ma","GreatSPN","small symbolic representation", properties, [{'T': 1}])
    
    def add_ftpp(self):
        properties = [['Unreliability','prob-reach-time-bounded'], ['Unavailability','steady-state-prob']]
        self.add_model('ma/ftpp/ftpp.1-1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.1-1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.1-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.1-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.2-1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.2-1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.2-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.2-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.3-1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.3-1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.3-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.3-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.4-1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.4-1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.4-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/ftpp/ftpp.4-2-true.jani',"","","ma","Galileo","", properties, [{}])
    
    def add_ftwc(self):
        properties = [['ReachMinIsOne','prob-reach'], ['TimeMin','exp-time'], ['TimeMax','exp-time'], ['PmaxReachBound','prob-reach-time-bounded'], ['SmaxReach','steady-state-prob']]
        self.add_model('ma/ftwc/ftwc.jani',"","","ma","Modest","fault-tolerant queueing system", properties, [{'N': 4, 'TIME_BOUND': 5},{'N': 8, 'TIME_BOUND': 5}])
    
    def add_hecs(self):
        properties = [['Unreliability','prob-reach-time-bounded'], ['Unavailability','steady-state-prob']]
        self.add_model('ma/hecs/hecs.false-1-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-2-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-2-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-3-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-3-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-3-3.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-4-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-4-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-4-3.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-4-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-5-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-5-5.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-6-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-6-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-7-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-7-7.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-8-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.false-8-8.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-1-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-2-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-2-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-3-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-3-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-3-3.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-4-1.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-4-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-4-3.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/hecs/hecs.true-4-4.jani',"","","ma","Galileo","", properties, [{}])
    
    def add_jobs(self):
        properties = [['completiontime','exp-time'], ['avgtime','exp-reward'], ['prhalfdone','prob-reach-time-bounded']]
        self.add_model('ma/jobs/jobs.5-2.jani',"","","ma","PRISM-MA","stochastic scheduling problem", properties, [{}])
        self.add_model('ma/jobs/jobs.10-3.jani',"","","ma","PRISM-MA","stochastic scheduling problem", properties, [{}])
        self.add_model('ma/jobs/jobs.15-3.jani',"","","ma","PRISM-MA","stochastic scheduling problem", properties, [{}])
    
    def add_mcs(self):
        properties = [['Unreliability','prob-reach-time-bounded'], ['Unavailability','steady-state-prob']]
        self.add_model('ma/mcs/mcs.1-1-10-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-10-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-11-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-11-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-12-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-12-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-13-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-13-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-14-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-14-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-4-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-4-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-5-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-5-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-6-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-6-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-7-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-7-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-8-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-8-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-9-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.1-1-9-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-1-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-1-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-1-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-1-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-1-4-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-1-4-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-2-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-2-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-2-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-2-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-2-4-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.2-2-4-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-1-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-1-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-1-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-1-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-1-4-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-1-4-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-2-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-2-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-2-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-2-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-2-4-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-2-4-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-3-2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-3-2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-3-3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-3-3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-3-4-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/mcs/mcs.3-3-4-true.jani',"","","ma","Galileo","", properties, [{}])
    
    def add_polling_system(self):
        properties = [['PminBothFullIsOne','prob-reach'], ['TminBothFull','exp-time'], ['TmaxBothFull','exp-time'], ['PmaxBothFullBound','prob-reach-time-bounded'], ['SmaxBothFull','steady-state-prob']]
        self.add_model('ma/polling-system/polling-system.jani',"","","ma","Modest","small nondeterministic queueing system", properties, [{'JOB_TYPES': 3, 'C': 3, 'TIME_BOUND': 5}])
    
    def add_readers_writers(self):
        properties = [['pr_many_requests','prob-reach'], ['exp_time_many_requests','exp-time'], ['pr_network','prob-reach'], ['prtb_many_requests','prob-reach-time-bounded']]
        self.add_model('ma/readers-writers/readers-writers.5.jani',"","","ma","GreatSPN","standard GSPN example", properties, [{}])
        self.add_model('ma/readers-writers/readers-writers.20.jani',"","","ma","GreatSPN","standard GSPN example", properties, [{}])
        self.add_model('ma/readers-writers/readers-writers.35.jani',"","","ma","GreatSPN","standard GSPN example", properties, [{}])
        self.add_model('ma/readers-writers/readers-writers.40.jani',"","","ma","GreatSPN","standard GSPN example", properties, [{}])
    
    def add_reentrant_queues(self):
        properties = [['PminBothQueuesFullIsOne','prob-reach'], ['TminBothQueuesFull','exp-time'], ['TmaxBothQueuesFull','exp-time'], ['PmaxBothQueuesFullBound','prob-reach-time-bounded'], ['SmaxBothQueuesFull','steady-state-prob']]
        self.add_model('ma/reentrant-queues/reentrant-queues.jani',"","","ma","Modest","asymmetric nondeterministic queueing system", properties, [{'JOB_TYPES': 3, 'C_LEFT': 3, 'C_RIGHT': 3, 'TIME_BOUND': 5}])
    
    def add_sf(self):
        properties = [['Unreliability','prob-reach-time-bounded']]
        self.add_model('ma/sf/sf.1-10.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.1-12.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.1-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.1-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.1-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.1-8.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.2-10.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.2-12.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.2-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.2-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.2-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.2-8.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.3-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.3-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.3-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.4-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.4-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.4-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.5-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.5-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.5-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.6-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.6-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.6-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.7-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.7-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.7-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.8-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.8-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.8-6.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.9-2.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.9-4.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sf/sf.9-6.jani',"","","ma","Galileo","", properties, [{}])
    
    def add_sms(self):
        properties = [['Unreliability','prob-reach-time-bounded'], ['Unavailability','steady-state-prob']]
        self.add_model('ma/sms/sms.1-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.1-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.10-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.10-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.11-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.11-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.12-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.12-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.2-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.2-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.3-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.3-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.4-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.4-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.5-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.5-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.6-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.6-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.7-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.7-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.8-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.8-true.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.9-false.jani',"","","ma","Galileo","", properties, [{}])
        self.add_model('ma/sms/sms.9-true.jani',"","","ma","Galileo","", properties, [{}])
    
    def add_stream(self):
        properties = [['exp_buffertime','exp-reward'], ['exp_restarts','exp-reward'], ['pr_underrun','prob-reach'], ['pr_underrun_tb','prob-reach-time-bounded']]
        self.add_model('ma/stream/stream.jani',"","","ma","PRISM-MA","simple scalable planning benchmark", properties, [{'N': 10},{'N': 100},{'N': 500},{'N': 1000}])
    
    def add_vgs(self):
        properties = [['MaxPrReachFailed','prob-reach'], ['MaxPrReachFailedTB','prob-reach-time-bounded'], ['MinExpTimeFailed','exp-time']]
        self.add_model('ma/vgs/vgs.4.jani',"","","ma","Galileo","industrial case study", properties, [{'TIME_BOUND': 10000}])
        self.add_model('ma/vgs/vgs.5.jani',"","","ma","Galileo","industrial case study", properties, [{'TIME_BOUND': 10000}])
    
    def add_beb(self):
        properties = [['LineSeized','prob-reach'], ['GaveUp','prob-reach']]
        self.add_model('mdp/beb/beb.3-4.jani',"","","mdp","Modest","", properties, [{'N': 3}])
        self.add_model('mdp/beb/beb.4-8.jani',"","","mdp","Modest","", properties, [{'N': 7}])
        self.add_model('mdp/beb/beb.5-16.jani',"","","mdp","Modest","", properties, [{'N': 15}])
        self.add_model('mdp/beb/beb.6-16.jani',"","","mdp","Modest","", properties, [{'N': 15}])
    
    def add_blocksworld(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/blocksworld/blocksworld.5.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/blocksworld/blocksworld.10.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/blocksworld/blocksworld.14.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/blocksworld/blocksworld.18.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
    
    def add_boxworld(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/boxworld/boxworld.10-5.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/boxworld/boxworld.10-10.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/boxworld/boxworld.15-10.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/boxworld/boxworld.15-15.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/boxworld/boxworld.20-20.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
    
    def add_cdrive(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/cdrive/cdrive.2.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/cdrive/cdrive.3.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/cdrive/cdrive.6.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/cdrive/cdrive.10.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
    
    def add_consensus(self):
        properties = [['c1','prob-reach'], ['c2','prob-reach'], ['disagree','prob-reach'], ['steps_max','exp-reward'], ['steps_min','exp-reward']]
        self.add_model('mdp/consensus/consensus.2.jani',"consensus.props","consensus.2.prism","mdp","PRISM","PRISM benchmark", properties, [{'K': 2},{'K': 4},{'K': 8},{'K': 16}])
        self.add_model('mdp/consensus/consensus.4.jani',"consensus.props","consensus.4.prism","mdp","PRISM","PRISM benchmark", properties, [{'K': 2},{'K': 4}])
        self.add_model('mdp/consensus/consensus.6.jani',"consensus.props","consensus.6.prism","mdp","PRISM","PRISM benchmark", properties, [{'K': 2}])
        self.add_model('mdp/consensus/consensus.8.jani',"consensus.props","consensus.8.prism","mdp","PRISM","PRISM benchmark", properties, [{'K': 2}])
        self.add_model('mdp/consensus/consensus.10.jani',"consensus.props","consensus.10.prism","mdp","PRISM","PRISM benchmark", properties, [{'K': 2}])
    
    def add_csma(self):
        properties = [['all_before_max','prob-reach'], ['all_before_min','prob-reach'], ['some_before','prob-reach'], ['time_max','exp-reward'], ['time_min','exp-reward']]
        self.add_model('mdp/csma/csma.2-2.jani',"csma.props","csma.2-2.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.2-4.jani',"csma.props","csma.2-4.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.2-6.jani',"csma.props","csma.2-6.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.3-2.jani',"csma.props","csma.3-2.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.3-4.jani',"csma.props","csma.3-4.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.3-6.jani',"csma.props","csma.3-6.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.4-2.jani',"csma.props","csma.4-2.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.4-4.jani',"csma.props","csma.4-4.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
        self.add_model('mdp/csma/csma.4-6.jani',"csma.props","csma.4-6.prism","mdp","PRISM","PRISM benchmark", properties, [{}])
    
    def add_eajs(self):
        properties = [['ExpUtil','exp-reward'], ['ProbUtil','prob-reach-reward-bounded']]
        self.add_model('mdp/eajs/eajs.2.jani',"eajs.props","eajs.2.prism","mdp","PRISM","reward-bounded properties", properties, [{'energy_capacity': 100, 'B': 5}])
        self.add_model('mdp/eajs/eajs.3.jani',"eajs.props","eajs.3.prism","mdp","PRISM","reward-bounded properties", properties, [{'energy_capacity': 150, 'B': 7}])
        self.add_model('mdp/eajs/eajs.4.jani',"eajs.props","eajs.4.prism","mdp","PRISM","reward-bounded properties", properties, [{'energy_capacity': 200, 'B': 9}])
        self.add_model('mdp/eajs/eajs.5.jani',"eajs.props","eajs.5.prism","mdp","PRISM","reward-bounded properties", properties, [{'energy_capacity': 250, 'B': 11}])
        self.add_model('mdp/eajs/eajs.6.jani',"eajs.props","eajs.6.prism","mdp","PRISM","reward-bounded properties", properties, [{'energy_capacity': 300, 'B': 13}])
    
    def add_echoring(self):
        properties = [['MinFailed','prob-reach'], ['MinOffline1','prob-reach'], ['MaxOffline1','prob-reach'], ['MinOffline2','prob-reach'], ['MaxOffline2','prob-reach'], ['MinOffline3','prob-reach'], ['MaxOffline3','prob-reach']]
        self.add_model('mdp/echoring/echoring.jani',"","","mdp","Modest","industrial protocol, spurious nondeterminism", properties, [{'ITERATIONS': 2},{'ITERATIONS': 50},{'ITERATIONS': 100}])
    
    def add_elevators(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/elevators/elevators.a-3-3.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/elevators/elevators.b-3-3.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/elevators/elevators.a-11-9.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/elevators/elevators.b-11-9.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
    
    def add_exploding_blocksworld(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/exploding-blocksworld/exploding-blocksworld.5.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/exploding-blocksworld/exploding-blocksworld.10.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/exploding-blocksworld/exploding-blocksworld.15.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/exploding-blocksworld/exploding-blocksworld.17.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
    
    def add_firewire(self):
        properties = [['elected','prob-reach'], ['time_max','exp-reward'], ['time_min','exp-reward'], ['time_sending','exp-reward'], ['deadline','prob-reach-reward-bounded']]
        self.add_model('mdp/firewire/firewire.false.jani',"firewire.false.props","firewire.false.prism","mdp","PRISM","PRISM benchmark", properties, [{'delay': 3, 'deadline': 200},{'delay': 3, 'deadline': 400},{'delay': 3, 'deadline': 600},{'delay': 3, 'deadline': 800},{'delay': 36, 'deadline': 200},{'delay': 36, 'deadline': 400},{'delay': 36, 'deadline': 600},{'delay': 36, 'deadline': 800}])
        self.add_model('mdp/firewire/firewire.true.jani',"firewire.true.props","firewire.true.prism","mdp","PRISM","PRISM benchmark", properties, [{'delay': 3, 'deadline': 200},{'delay': 3, 'deadline': 400},{'delay': 3, 'deadline': 600},{'delay': 3, 'deadline': 800},{'delay': 36, 'deadline': 200},{'delay': 36, 'deadline': 400},{'delay': 36, 'deadline': 600},{'delay': 36, 'deadline': 800}])
    
    def add_firewire_abst(self):
        properties = [['elected','prob-reach'], ['rounds','exp-reward'], ['time_max','exp-reward'], ['time_min','exp-reward']]
        self.add_model('mdp/firewire_abst/firewire_abst.jani',"firewire_abst.props","firewire_abst.prism","mdp","PRISM","PRISM benchmark", properties, [{'delay': 3},{'delay': 36}])
    
    def add_firewire_dl(self):
        properties = [['deadline','prob-reach']]
        self.add_model('mdp/firewire_dl/firewire_dl.jani',"firewire_dl.props","firewire_dl.prism","mdp","PRISM","PRISM benchmark", properties, [{'delay': 3, 'deadline': 200},{'delay': 3, 'deadline': 400},{'delay': 3, 'deadline': 600},{'delay': 3, 'deadline': 800},{'delay': 36, 'deadline': 200},{'delay': 36, 'deadline': 400},{'delay': 36, 'deadline': 600},{'delay': 36, 'deadline': 800}])
    
    def add_ij(self):
        properties = [['stable','prob-reach']]
        self.add_model('mdp/ij/ij.3.jani',"ij.3.props","ij.3.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/ij/ij.10.jani',"ij.10.props","ij.10.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/ij/ij.20.jani',"ij.20.props","ij.20.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/ij/ij.30.jani',"ij.30.props","ij.30.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/ij/ij.40.jani',"ij.40.props","ij.40.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/ij/ij.50.jani',"ij.50.props","ij.50.prism","mdp","PRISM","PRISM case study", properties, [{}])
    
    def add_pacman(self):
        properties = [['crash','prob-reach']]
        self.add_model('mdp/pacman/pacman.jani',"pacman.props","pacman.nm","mdp","PRISM","learned probabilities", properties, [{'MAXSTEPS': 5},{'MAXSTEPS': 60},{'MAXSTEPS': 100}])
    
    def add_philosophers_mdp(self):
        properties = [['eat','prob-reach']]
        self.add_model('mdp/philosophers-mdp/philosophers-mdp.3.jani',"philosophers-mdp.3.props","philosophers-mdp.3.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/philosophers-mdp/philosophers-mdp.10.jani',"philosophers-mdp.10.props","philosophers-mdp.10.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/philosophers-mdp/philosophers-mdp.20.jani',"philosophers-mdp.20.props","philosophers-mdp.20.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/philosophers-mdp/philosophers-mdp.30.jani',"philosophers-mdp.30.props","philosophers-mdp.30.prism","mdp","PRISM","PRISM case study", properties, [{}])
    
    def add_pnueli_zuck(self):
        properties = [['live','prob-reach']]
        self.add_model('mdp/pnueli-zuck/pnueli-zuck.3.jani',"pnueli-zuck.props","pnueli-zuck.3.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/pnueli-zuck/pnueli-zuck.5.jani',"pnueli-zuck.props","pnueli-zuck.5.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/pnueli-zuck/pnueli-zuck.10.jani',"pnueli-zuck.props","pnueli-zuck.10.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/pnueli-zuck/pnueli-zuck.15.jani',"pnueli-zuck.props","pnueli-zuck.15.prism","mdp","PRISM","PRISM case study", properties, [{}])
    
    def add_rabin(self):
        properties = [['live','prob-reach']]
        self.add_model('mdp/rabin/rabin.3.jani',"rabin.3.props","rabin.3.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/rabin/rabin.5.jani',"rabin.5.props","rabin.5.prism","mdp","PRISM","PRISM case study", properties, [{}])
        self.add_model('mdp/rabin/rabin.10.jani',"rabin.10.props","rabin.10.prism","mdp","PRISM","PRISM case study", properties, [{}])
    
    def add_random_predicates(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/random-predicates/random-predicates.a.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/random-predicates/random-predicates.b.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/random-predicates/random-predicates.c.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/random-predicates/random-predicates.d.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
    
    def add_rectangle_tireworld(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/rectangle-tireworld/rectangle-tireworld.5.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/rectangle-tireworld/rectangle-tireworld.11.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/rectangle-tireworld/rectangle-tireworld.30.jani.gz',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
    
    def add_resource_gathering(self):
        properties = [['expgold','exp-reward-step-bounded'], ['expsteps','exp-steps'], ['prgoldgem','prob-reach-step-bounded']]
        self.add_model('mdp/resource-gathering/resource-gathering.jani',"resource-gathering.prctl","resource-gathering.pm","mdp","PRISM","", properties, [{'B': 200, 'GOLD_TO_COLLECT': 15, 'GEM_TO_COLLECT': 15},{'B': 400, 'GOLD_TO_COLLECT': 30, 'GEM_TO_COLLECT': 30},{'B': 1300, 'GOLD_TO_COLLECT': 100, 'GEM_TO_COLLECT': 100},{'B': 1000000, 'GOLD_TO_COLLECT': 0, 'GEM_TO_COLLECT': 0}])
    
    def add_tireworld(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/tireworld/tireworld.17.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/tireworld/tireworld.25.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/tireworld/tireworld.35.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
        self.add_model('mdp/tireworld/tireworld.45.jani',"","","mdp","PPDDL","IPPC 2006 benchmark", properties, [{}])
    
    def add_triangle_tireworld(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/triangle-tireworld/triangle-tireworld.9.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/triangle-tireworld/triangle-tireworld.441.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/triangle-tireworld/triangle-tireworld.1681.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/triangle-tireworld/triangle-tireworld.3721.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/triangle-tireworld/triangle-tireworld.6561.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
    
    def add_wlan(self):
        properties = [['collisions','prob-reach'], ['cost_max','exp-reward'], ['cost_min','exp-reward'], ['num_collisions','exp-reward'], ['sent','prob-reach'], ['time_max','exp-reward'], ['time_min','exp-reward']]
        self.add_model('mdp/wlan/wlan.0.jani',"wlan.props","wlan.0.prism","mdp","PRISM","PRISM benchmark", properties, [{'COL': 0}])
        self.add_model('mdp/wlan/wlan.1.jani',"wlan.props","wlan.1.prism","mdp","PRISM","PRISM benchmark", properties, [{'COL': 0}])
        self.add_model('mdp/wlan/wlan.2.jani',"wlan.props","wlan.2.prism","mdp","PRISM","PRISM benchmark", properties, [{'COL': 0}])
        self.add_model('mdp/wlan/wlan.3.jani',"wlan.props","wlan.3.prism","mdp","PRISM","PRISM benchmark", properties, [{'COL': 0}])
        self.add_model('mdp/wlan/wlan.4.jani',"wlan.props","wlan.4.prism","mdp","PRISM","PRISM benchmark", properties, [{'COL': 0}])
        self.add_model('mdp/wlan/wlan.5.jani',"wlan.props","wlan.5.prism","mdp","PRISM","PRISM benchmark", properties, [{'COL': 0}])
        self.add_model('mdp/wlan/wlan.6.jani',"wlan.props","wlan.6.prism","mdp","PRISM","PRISM benchmark", properties, [{'COL': 0}])
    
    def add_wlan_dl(self):
        properties = [['deadline','prob-reach']]
        self.add_model('mdp/wlan_dl/wlan_dl.0.jani',"wlan_dl.props","wlan_dl.0.prism","mdp","PRISM","PRISM benchmark", properties, [{'deadline': 80}])
        self.add_model('mdp/wlan_dl/wlan_dl.1.jani',"wlan_dl.props","wlan_dl.1.prism","mdp","PRISM","PRISM benchmark", properties, [{'deadline': 80}])
        self.add_model('mdp/wlan_dl/wlan_dl.2.jani',"wlan_dl.props","wlan_dl.2.prism","mdp","PRISM","PRISM benchmark", properties, [{'deadline': 80}])
        self.add_model('mdp/wlan_dl/wlan_dl.3.jani',"wlan_dl.props","wlan_dl.3.prism","mdp","PRISM","PRISM benchmark", properties, [{'deadline': 80}])
        self.add_model('mdp/wlan_dl/wlan_dl.4.jani',"wlan_dl.props","wlan_dl.4.prism","mdp","PRISM","PRISM benchmark", properties, [{'deadline': 80}])
        self.add_model('mdp/wlan_dl/wlan_dl.5.jani',"wlan_dl.props","wlan_dl.5.prism","mdp","PRISM","PRISM benchmark", properties, [{'deadline': 80}])
        self.add_model('mdp/wlan_dl/wlan_dl.6.jani',"wlan_dl.props","wlan_dl.6.prism","mdp","PRISM","PRISM benchmark", properties, [{'deadline': 80}])
    
    def add_zenotravel(self):
        properties = [['goal','prob-reach']]
        self.add_model('mdp/zenotravel/zenotravel.4-2-2.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/zenotravel/zenotravel.6-5-3.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/zenotravel/zenotravel.10-5-3.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
        self.add_model('mdp/zenotravel/zenotravel.20-10-6.jani',"","","mdp","PPDDL","IPPC 2008 benchmark", properties, [{}])
    
    def add_zeroconf(self):
        properties = [['correct_max','prob-reach'], ['correct_min','prob-reach']]
        self.add_model('mdp/zeroconf/zeroconf.jani',"zeroconf.props","zeroconf.prism","mdp","PRISM","PRISM benchmark", properties, [{'N': 20, 'K': 2, 'reset': True},{'N': 20, 'K': 4, 'reset': True},{'N': 20, 'K': 6, 'reset': True},{'N': 20, 'K': 8, 'reset': True},{'N': 1000, 'K': 2, 'reset': True},{'N': 1000, 'K': 4, 'reset': True},{'N': 1000, 'K': 6, 'reset': True},{'N': 1000, 'K': 8, 'reset': True},{'N': 20, 'K': 2, 'reset': False},{'N': 20, 'K': 4, 'reset': False},{'N': 20, 'K': 6, 'reset': False},{'N': 20, 'K': 8, 'reset': False},{'N': 1000, 'K': 2, 'reset': False},{'N': 1000, 'K': 4, 'reset': False},{'N': 1000, 'K': 6, 'reset': False},{'N': 1000, 'K': 8, 'reset': False}])
    
    def add_zeroconf_dl(self):
        properties = [['deadline_max','prob-reach'], ['deadline_min','prob-reach']]
        self.add_model('mdp/zeroconf_dl/zeroconf_dl.jani',"zeroconf_dl.props","zeroconf_dl.prism","mdp","PRISM","PRISM benchmark", properties, [{'N': 1000, 'K': 1, 'reset': True, 'deadline': 10},{'N': 1000, 'K': 1, 'reset': True, 'deadline': 20},{'N': 1000, 'K': 1, 'reset': True, 'deadline': 30},{'N': 1000, 'K': 1, 'reset': True, 'deadline': 40},{'N': 1000, 'K': 1, 'reset': True, 'deadline': 50},{'N': 1000, 'K': 1, 'reset': False, 'deadline': 10},{'N': 1000, 'K': 1, 'reset': False, 'deadline': 20},{'N': 1000, 'K': 1, 'reset': False, 'deadline': 30},{'N': 1000, 'K': 1, 'reset': False, 'deadline': 40},{'N': 1000, 'K': 1, 'reset': False, 'deadline': 50}])
    
    def add_brp_pta(self):
        properties = [['T_1','prob-reach'], ['T_2','prob-reach'], ['T_A1','prob-reach'], ['T_A2','prob-reach'], ['P_A','prob-reach'], ['P_B','prob-reach'], ['P_1','prob-reach'], ['P_2','prob-reach'], ['P_3','prob-reach'], ['P_4','prob-reach'], ['Dmax','prob-reach-time-bounded'], ['Dmin','prob-reach-time-bounded'], ['Emax','exp-time'], ['Emin','exp-time']]
        self.add_model('pta/brp-pta/brp-pta.jani',"","","pta","Modest","scalable in multiple dimensions", properties, [{'N': 16, 'MAX': 2, 'TD': 1, 'TIME_BOUND': 64},{'N': 64, 'MAX': 12, 'TD': 32, 'TIME_BOUND': 256}])
    
    def add_csma_pta(self):
        properties = [['collisions','prob-reach']]
        self.add_model('pta/csma-pta/csma-pta.jani',"csma-pta.props","csma-pta.prism","pta","PRISM","PRISM benchmark", properties, [{'K': 2, 'COL': 4},{'K': 2, 'COL': 8},{'K': 4, 'COL': 4},{'K': 4, 'COL': 8}])
    
    def add_csma_abst_pta(self):
        properties = [['deadline_max','prob-reach-time-bounded'], ['deadline_min','prob-reach-time-bounded'], ['eventually','prob-reach']]
        self.add_model('pta/csma_abst-pta/csma_abst-pta.jani',"csma_abst-pta.props","csma_abst-pta.prism","pta","PRISM","PRISM benchmark", properties, [{'K': 1, 'T': 1000},{'K': 1, 'T': 1750},{'K': 1, 'T': 1800},{'K': 1, 'T': 2000},{'K': 1, 'T': 3000}])
    
    def add_firewire_pta(self):
        properties = [['deadline','prob-reach-time-bounded'], ['eventually','prob-reach']]
        self.add_model('pta/firewire-pta/firewire-pta.jani',"firewire-pta.props","firewire-pta.prism","pta","PRISM","PRISM benchmark", properties, [{'delay': 30, 'T': 2500},{'delay': 30, 'T': 5000},{'delay': 30, 'T': 7500},{'delay': 360, 'T': 2500},{'delay': 360, 'T': 5000},{'delay': 360, 'T': 7500}])
    
    def add_firewire_abst_pta(self):
        properties = [['deadline_max','prob-reach-time-bounded'], ['deadline_min','prob-reach-time-bounded'], ['eventually','prob-reach']]
        self.add_model('pta/firewire_abst-pta/firewire_abst-pta.jani',"firewire_abst-pta.props","firewire_abst-pta.prism","pta","PRISM","PRISM benchmark", properties, [{'delay': 30, 'T': 50},{'delay': 30, 'T': 500},{'delay': 30, 'T': 5000},{'delay': 30, 'T': 10000},{'delay': 30, 'T': 15000},{'delay': 360, 'T': 50},{'delay': 360, 'T': 500},{'delay': 360, 'T': 5000},{'delay': 360, 'T': 10000},{'delay': 360, 'T': 15000}])
    
    def add_repudiation_honest(self):
        properties = [['deadline','prob-reach-time-bounded'], ['eventually','prob-reach']]
        self.add_model('pta/repudiation_honest/repudiation_honest.jani',"repudiation_honest.props","repudiation_honest.prism","pta","PRISM","PRISM benchmark", properties, [{'T': 40},{'T': 80},{'T': 100}])
    
    def add_repudiation_malicious(self):
        properties = [['deadline','prob-reach-time-bounded'], ['eventually','prob-reach']]
        self.add_model('pta/repudiation_malicious/repudiation_malicious.jani',"repudiation_malicious.props","repudiation_malicious.prism","pta","PRISM","PRISM benchmark", properties, [{'T': 5},{'T': 10},{'T': 20}])
    
    def add_wlan_large(self):
        properties = [['P_1','prob-reach'], ['P_min','prob-reach'], ['P_max','prob-reach'], ['D_and','prob-reach-time-bounded'], ['D_or','prob-reach-time-bounded'], ['D_1','prob-reach-time-bounded'], ['E_and','exp-time'], ['E_or','exp-time'], ['E_1','exp-reward']]
        self.add_model('pta/wlan-large/wlan-large.jani',"","","pta","Modest","", properties, [{'K': 2}])
    
    def add_zeroconf_pta(self):
        properties = [['deadline','prob-reach-time-bounded'], ['incorrect','prob-reach']]
        self.add_model('pta/zeroconf-pta/zeroconf-pta.jani',"zeroconf-pta.props","zeroconf-pta.prism","pta","PRISM","PRISM benchmark", properties, [{'T': 100},{'T': 150},{'T': 200}])
    
    def add_model(self, file_name_jani,file_name_prism_model,file_name_prism_props,formal_model_type,original_model_format,notes, properties, parameter_settings):
        model = BenchmarkModel(self, file_name_jani,file_name_prism_model,file_name_prism_props,formal_model_type,original_model_format,notes)
        for property in properties:
            for parameters in parameter_settings:
                sequence = BenchmarkSequence(model, property[0], property[1], parameters)
                BenchmarkInstance(sequence, {})

