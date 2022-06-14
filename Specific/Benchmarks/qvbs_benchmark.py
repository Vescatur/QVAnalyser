from Library.Benchmarks.benchmark import Benchmark
from Library.Benchmarks.benchmark_model import BenchmarkModel
from Library.Benchmarks.benchmark_sequence import BenchmarkSequence
from Library.Benchmarks.benchmark_instance import BenchmarkInstance
from Specific.Tools.modest_tool import ModestTool
from Specific.Tools.storm_tool import StormTool


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
        self.add_model('', '', '')

    def add_embedded(self):
        self.add_model('', '', '')

    def add_fms(self):
        self.add_model('', '', '')

    def add_hill_toggle(self):
        self.add_model('', '', '')

    def add_kanban(self):
        self.add_model('', '', '')

    def add_majority(self):
        self.add_model('', '', '')

    def add_mapk_cascade(self):
        self.add_model('', '', '')

    def add_p53(self):
        self.add_model('', '', '')

    def add_philosophers(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_polling(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_speed_ind(self):
        self.add_model('', '', '')

    def add_tandem(self):
        self.add_model('', '', '')

    def add_toggle_switch(self):
        self.add_model('', '', '')

    def add_bluetooth(self):
        self.add_model('', '', '')

    def add_brp(self):
        self.add_model('', '', '')

    def add_coupon(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_crowds(self):
        self.add_model('', '', '')

    def add_egl(self):
        self.add_model('', '', '')

    def add_haddad_monmege(self):
        self.add_model('', '', '')

    def add_herman(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_leader_sync(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_nand(self):
        self.add_model('', '', '')

    def add_oscillators(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_bitcoin_attack(self):
        self.add_model('', '', '')

    def add_breakdown_queues(self):
        self.add_model('', '', '')

    def add_cabinets(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_dpm(self):
        self.add_model('', '', '')

    def add_erlang(self):
        self.add_model('', '', '')

    def add_flexible_manufacturing(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_ftpp(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_ftwc(self):
        self.add_model('', '', '')

    def add_hecs(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_jobs(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_mcs(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_polling_system(self):
        self.add_model('', '', '')

    def add_readers_writers(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_reentrant_queues(self):
        self.add_model('', '', '')

    def add_sf(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_sms(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_stream(self):
        self.add_model('', '', '')

    def add_vgs(self):
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_beb(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_blocksworld(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_boxworld(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_cdrive(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_consensus(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_csma(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_eajs(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_echoring(self):
        self.add_model('', '', '')

    def add_elevators(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_exploding_blocksworld(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_firewire(self):
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_firewire_abst(self):
        self.add_model('', '', '')

    def add_firewire_dl(self):
        self.add_model('', '', '')

    def add_ij(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_pacman(self):
        self.add_model('', '', '')

    def add_philosophers_mdp(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_pnueli_zuck(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_rabin(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_random_predicates(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_rectangle_tireworld(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_resource_gathering(self):
        self.add_model('', '', '')

    def add_tireworld(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_triangle_tireworld(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_wlan(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_wlan_dl(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_zenotravel(self):
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')
        self.add_model('', '', '')

    def add_zeroconf(self):
        self.add_model('', '', '')

    def add_zeroconf_dl(self):
        self.add_model('', '', '')

    def add_brp_pta(self):
        self.add_model('', '', '')

    def add_csma_pta(self):
        self.add_model('', '', '')

    def add_csma_abst_pta(self):
        self.add_model('', '', '')

    def add_firewire_pta(self):
        self.add_model('', '', '')

    def add_firewire_abst_pta(self):
        self.add_model('', '', '')

    def add_repudiation_honest(self):
        self.add_model('', '', '')

    def add_repudiation_malicious(self):
        self.add_model('', '', '')

    def add_wlan_large(self):
        self.add_model('', '', '')

    def add_zeroconf_pta(self):
        self.add_model('', '', '')

    def add_model(self, file_name, properties, parameter_settings):
        model = BenchmarkModel(self, file_name)
        for property_name in properties:
            for parameters in parameter_settings:
                sequence = BenchmarkSequence(model, property_name, parameters)
                BenchmarkInstance(sequence, {})

