import numpy as np
from Library.Results.measurements import Measurements
from Specific.Output.display_name import algorithm_name_to_display_name


class StatisticsSprint6(object):

    def __init__(self, benchmark):
        self.benchmark = benchmark

        self.times = [Measurements.STATE_SPACE_TIME, Measurements.PROPERTY_TIME, Measurements.WALL_TIME]
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
        allignments = "l"*(len(self.times)*len(self.characteristics)+1)
        print("\\begin{tabular}{"+allignments+"}")
        print("\\toprule")
        line1 = ""
        line2 = ""
        first = True
        for time in self.times:
            line1 += "\t& \multicolumn{3}{l}{"+self.time_names[time]+"}"
            for characteristic in self.characteristics:
                line2 += "\t& "
                line2 += self.characteristic_names[characteristic]
        print(line1 + "\\\\")
        print(line2 + "\\\\")
        print("\cmidrule(r){1-1} \cmidrule{2-10} ")

    def print_body(self):
        results = {}
        for algorithm in self.benchmark.algorithms:
            results[algorithm.name] = []

        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                for result in instance.results:
                    results[result.algorithm_name].append(result)

        for algorithm in self.benchmark.algorithms:
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
                        R2 = np.corrcoef(time_measurements,characteristic_measurements)
                        correlation_number = R2[0][1]
                        round_correlation = round(correlation_number*100)/100
                        color = self.generate_color(correlation_number)
                        line += "\t& "+ color + str(round_correlation).replace(".",",")
                    else:
                        line += "\t& No data"
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

    def generate_color(self,metric):
        color = None
        white = np.array([255, 255, 255])
        if metric >= 0:
            green = np.array([87, 187, 138])
            factor = metric
            color = green * factor + white * (1 - factor)
        else:
            red = np.array([230, 124, 115])
            factor = 1+metric
            color = white * factor + red * (1 - factor)

        hex_color = self.number_to_hex(color[0]) + self.number_to_hex(color[1]) + self.number_to_hex(color[2])
        return "\cellcolor[HTML]{" + hex_color + "}"

    def number_to_hex(self, number):
        text = format(round(number),"X")
        if len(text) == 1:
            return "0"+text
        else:
            return text