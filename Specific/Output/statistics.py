import numpy as np
from Library.Results.measurements import Measurements
from Specific.Output.Matrix.text_file_printer import TextFileWriter
from Specific.Output.display_name import algorithm_name_to_display_name
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Prism.prism_tool import PrismTool
from Specific.Tools.Storm.storm_tool import StormTool
from scipy import stats

class Statistics(object):

    def __init__(self, benchmark,characteristics,time,name):
        with TextFileWriter(name) as self.writer:
            self.benchmark = benchmark

            self.times = [time]
            self.characteristics = characteristics
    
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
        self.writer.print("\\begin{table}[htbp]")
        self.writer.print("\centering")
        allignments = "l" * (len(self.times) * len(self.characteristics)*3 + 1)
        self.writer.print("\\begin{tabular}{" + allignments + "}")
        self.writer.print("\\toprule")
        line1 = ""
        line2 = ""
        line3 = ""
        for time in self.times:
            line1 += "\t& \multicolumn{9}{l}{" + self.time_names[time] + "}"
            for characteristic in self.characteristics:
                line2 += "\t& \multicolumn{3}{l}{" + self.characteristic_names[characteristic] + "}"
                line3 += "\t& r-value \t& p-value \t& \multicolumn{1}{l}{formula} "
        self.writer.print(line1 + "\\\\")
        self.writer.print(line2 + "\\\\")
        self.writer.print(line3 + "\\\\")
        self.writer.print("\cmidrule(r){1-1} \cmidrule{2-10} ")

    def print_body(self):
        results = {}
        for algorithm in self.benchmark.algorithms:
            results[algorithm.name] = []

        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    results[result.algorithm_name].append(result)
        index = 0
        for algorithm in self.get_algorithms():
            index += 1
            line = str(index) + " " + algorithm_name_to_display_name(algorithm.name)
            for time in self.times:
                for characteristic in self.characteristics:
                    time_measurements = []
                    characteristic_measurements = []
                    for result in results[algorithm.name]:
                        if time in result.measurements and characteristic in result.measurements:
                            time_measurements.append(result.measurements[time])
                            characteristic_measurements.append(result.measurements[characteristic])
                    if len(time_measurements) >= 3 and not self.all_equal(time_measurements):
                        result = stats.linregress(characteristic_measurements,time_measurements)
                        round_correlation = round(result.rvalue * 100) / 100
                        colorR = self.generate_color_r_value(result.rvalue)
                        line += "\t& " + colorR + str(round_correlation)
                        round_pvalue = round(result.pvalue * 100) / 100
                        colorP = self.generate_color_p_value(result.pvalue)
                        line += "\t& " + colorP + "{:.2f}".format(round_pvalue)

                        if result.pvalue <= 0.05:
                            divider = 100
                            step_size = 1000000
                            intercept_display = round(result.intercept * divider) / (divider)
                            slope_display = round(result.slope * divider*step_size) / divider
                            if intercept_display >= 0:
                                line += "\t& \m{" + str(slope_display) + "x + " + str(intercept_display) + "}"
                            else:
                                intercept_display = intercept_display * -1
                                line += "\t& \m{" + str(slope_display) + "x - " + str(intercept_display) + "}"
                        else:
                            line += "\t& "
                    else:
                        line += "\t& No data \t& \t&"
            self.writer.print(line + " \\\\")

    def print_bottom_row(self):
        self.writer.print("\\bottomrule")
        self.writer.print("\\end{tabular}")
        self.writer.print("\\caption{??}")
        self.writer.print("\\label{table:??}")
        self.writer.print("\\end{table}")

    def all_equal(self, measurements):
        for measurement in measurements:
            if measurement != measurements[0]:
                return False
        return True

    def generate_color_r_value(self, metric):
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


    def generate_color_p_value(self, metric):
        color = None
        white = np.array([255, 255, 255])
        if metric <= 0.05:
            green = np.array([87, 187, 138])
            factor = metric/0.05
            color = green * (1 - factor) + white * factor
        else:
            red = np.array([230, 124, 115])
            factor = (metric-0.05)/0.95
            factor = (factor+1)/2
            color = white * (1 - factor) + red * factor

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