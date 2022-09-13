import numpy as np
from Library.Results.measurements import Measurements
from Specific.Output.display_name import algorithm_name_to_display_name
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Prism.prism_tool import PrismTool
from Specific.Tools.Storm.storm_tool import StormTool


class StatisticsSprint6(object):

    def __init__(self, benchmark,time):
        self.benchmark = benchmark

        #self.times = [Measurements.STATE_SPACE_TIME, Measurements.PROPERTY_TIME, Measurements.WALL_TIME]

        self.times = [time]
        self.characteristics = [Measurements.STATES, Measurements.TRANSITIONS, Measurements.BRANCHES]

        self.time_names = {}
        self.time_names[Measurements.STATE_SPACE_TIME] = "State space time"
        self.time_names[Measurements.PROPERTY_TIME] = "Property time"
        self.time_names[Measurements.WALL_TIME] = "Wall-clock time"

        self.characteristic_names = {}
        self.characteristic_names[Measurements.STATES] = "States"
        self.characteristic_names[Measurements.TRANSITIONS] = "Transitions"
        self.characteristic_names[Measurements.BRANCHES] = "Branches"

        self.print_top_row()
        self.print_body()
        self.print_bottom_row()

    def print_top_row(self):
        print("\\begin{table}[htbp]")
        print("\centering")
        allignments = "l" * (len(self.times) * len(self.characteristics)*2 + 1)
        print("\\begin{tabular}{" + allignments + "}")
        print("\\toprule")
        line1 = ""
        line2 = ""
        first = True
        for time in self.times:
            line1 += "\t& \multicolumn{3}{l}{" + self.time_names[time] + "}"
            for characteristic in self.characteristics:
                line2 += "\t& \multicolumn{2}{l}{" + self.characteristic_names[characteristic] + "}"
        print(line1 + "\\\\")
        print(line2 + "\\\\")
        print("\cmidrule(r){1-1} \cmidrule{2-7} ")

    def print_body(self):
        results = {}
        for algorithm in self.benchmark.algorithms:
            results[algorithm.name] = []

        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    results[result.algorithm_name].append(result)

        for algorithm in self.get_algorithms():
            line = algorithm_name_to_display_name(algorithm.name)
            for time in self.times:
                for characteristic in self.characteristics:
                    time_measurements = []
                    characteristic_measurements = []
                    for result in results[algorithm.name]:
                        if time in result.measurements and characteristic in result.measurements:
                            time_measurements.append(result.measurements[time])
                            characteristic_measurements.append(result.measurements[characteristic])
                    if len(time_measurements) >= 3 and not self.all_equal(time_measurements):
                        R2 = np.corrcoef(time_measurements, characteristic_measurements)
                        correlation_number = R2[0][1]
                        round_correlation = round(correlation_number * 100) / 100
                        color = self.generate_color(correlation_number)
                        line += "\t& " + color + str(round_correlation)

                        if correlation_number >=0.7:
                            correlated_line = np.polyfit(characteristic_measurements, time_measurements, 1)
                            divider = 100
                            step_size = 1000000
                            start_number = round(correlated_line[1] * divider) / (divider)
                            ramp_number = round(correlated_line[0] * divider*step_size) / divider
                            if start_number >= 0:
                                line += "\t& \m{" + str(ramp_number) + "x + " + str(start_number) + "}"
                            else:
                                start_number = start_number * -1
                                line += "\t& \m{" + str(ramp_number) + "x - " + str(start_number) + "}"
                        else:
                            line += "\t& "
                        '''print(correlation_number)
                        print(correlated_line)
                        print(characteristic_measurements)
                        print(time_measurements)

                        for i in range(0, len(time_measurements)):
                            print(str(characteristic_measurements[i]).replace(".", ",") + "\t" + str(time_measurements[i]).replace(".", ","))
                        return '''
                    else:
                        line += "\t& No data \t&"
            print(line + " \\\\")

    def print_bottom_row(self):
        print("\\bottomrule")
        print("\\end{tabular}")
        print("\\caption{??}")
        print("\\label{table:??}")
        print("\\end{table}")

    def all_equal(self, measurements):
        for measurement in measurements:
            if measurement != measurements[0]:
                return False
        return True

    def generate_color(self, metric):
        color = None
        white = np.array([255, 255, 255])
        if metric >= 0:
            green = np.array([87, 187, 138])
            factor = metric
            color = green * factor + white * (1 - factor)
        else:
            red = np.array([230, 124, 115])
            factor = 1 + metric
            color = white * factor + red * (1 - factor)

        hex_color = self.number_to_hex(color[0]) + self.number_to_hex(color[1]) + self.number_to_hex(color[2])
        return "\cellcolor[HTML]{" + hex_color + "}"

    def number_to_hex(self, number):
        text = format(round(number), "X")
        if len(text) == 1:
            return "0" + text
        else:
            return text

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