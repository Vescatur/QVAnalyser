import numpy as np

from Library.Output.matrix import Matrix
from Library.Results.measurements import Measurements
from Specific.Output.display_name import algorithm_name_to_display_name


def first_element(item):
    return item[0]

class MatrixWins(Matrix):

    def __init__(self, benchmark, algorithms, instance_filter, use_latex):
        self.benchmark = benchmark
        self.instance_filter = instance_filter
        sorted_algorithms = self.order_algorithms_by_wins(algorithms)

        super().__init__(benchmark, sorted_algorithms, instance_filter, use_latex)

    def print_top_row(self, algorithms):
        if self.use_latex:
            print("\\begin{table}[htbp]")
            print("\centering")
            allignments = "l"*(len(algorithms)+3)
            print("\\begin{tabular}{"+allignments+"}")
            print("\\toprule")
            line = ""
            for alg in algorithms:
                display_name = algorithm_name_to_display_name(alg.name)
                line += "\t& \\fonttopsimilar \\rotatebox{90}{"+display_name + "} "
            line += "\t& \\rotatebox{90}{Wins} "
            line += "\t& \\rotatebox{90}{Best} "
            print(line + "\\\\")
        else:
            line = "\t"
            for alg in algorithms:
                display_name = algorithm_name_to_display_name(alg.name)
                line += display_name + "\t"
            print(line)


    def order_algorithms_by_wins(self, algorithms):
        fast_results = {}
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if self.instance_filter(instance):
                    fast_result = None
                    for result in instance.results:
                        if Measurements.WALL_TIME in result.measurements:
                            if not result.timed_out and not result.not_supported and not result.threw_error:
                                if fast_result == None:
                                    fast_result = result
                                elif result.measurements[Measurements.WALL_TIME] > fast_result.measurements[Measurements.WALL_TIME]:
                                    fast_result = result
                                elif result.measurements[Measurements.WALL_TIME] == fast_result.measurements[Measurements.WALL_TIME]:
                                    raise Exception("Code assumes no Wall time being equal")
                    fast_results[instance] = fast_result


        self.wins_per_algorithm = {}
        self.best_per_algorithm = {}
        algorithms_with_wins = []
        for algorithm in algorithms:
            total_best = 0
            wins = 0
            for sequence in self.benchmark.benchmark_sequences:
                for instance in sequence.benchmark_instances:
                    if self.instance_filter(instance):
                        if not fast_results[instance] is None:
                            if fast_results[instance].algorithm_name == algorithm.name:
                                total_best+=1
                        for algorithm_opponent in algorithms:
                            result_left = self.find_result_with_algorithm(instance, algorithm)
                            result_top = self.find_result_with_algorithm(instance, algorithm_opponent)
                            if not result_left.not_supported and not result_top.not_supported:
                                time_left = self.get_time(result_left)
                                time_top = self.get_time(result_top)
                                if time_left < time_top:
                                    wins += 1

            self.wins_per_algorithm[algorithm] = wins
            self.best_per_algorithm[algorithm] = total_best
            algorithms_with_wins.append((wins,algorithm))

        sorted_win_algorithms = sorted(algorithms_with_wins,key=first_element,reverse=True)
        sorted_algorithms = []
        for win_algorithm in sorted_win_algorithms:
            sorted_algorithms.append(win_algorithm[1])
        return sorted_algorithms

    def print_body_line(self, algorithms, algorithm_left):
        display_name = algorithm_name_to_display_name(algorithm_left.name)
        if self.use_latex:
            line = display_name
            for algorithm_top in algorithms:
                line += "\t& " + str(self.generate_cell_text(algorithm_left, algorithm_top))
            line += "\t& " + str(self.wins_per_algorithm[algorithm_left])
            line += "\t& " + str(self.best_per_algorithm[algorithm_left])
            print(line + " \\\\")
        else:
            line = display_name + "\t"
            for algorithm_top in algorithms:
                line += str(self.generate_cell_text(algorithm_left, algorithm_top)) + "\t"
            print(line)

    def generate_cell_text(self, algorithm_left, algorithm_top):
        wins = 0
        draws = 0
        loss = 0
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if self.instance_filter(instance):
                    result_left = self.find_result_with_algorithm(instance, algorithm_left)
                    result_top = self.find_result_with_algorithm(instance, algorithm_top)
                    if not result_left.not_supported and not result_top.not_supported:
                        time_left = self.get_time(result_left)
                        time_top = self.get_time(result_top)
                        if time_left < time_top:
                            wins += 1
                        elif time_left == time_top:
                            draws += 1
                        elif time_left > time_top:
                            loss += 1
        win_ratio = 0
        if wins+loss != 0:
            win_ratio = wins/(wins+loss)

        display_metric = round(win_ratio*10)
        cell_content = ""
        if display_metric == 10:
            cell_content = "+"
        else:
            cell_content = str(display_metric)
        color = self.generate_color(win_ratio)
        return "\\fontcellsimilar " + color + cell_content

    def generate_color(self, metric):
        color = None
        white = np.array([255, 255, 255])
        if metric >= 0.5:
            green = np.array([87, 187, 138])
            factor = (metric-0.5)/0.5
            color = green*factor+white*(1-factor)
        else:
            red = np.array([230, 124, 115])
            factor = metric/0.5
            color = white*factor+red*(1-factor)

        hex_color = self.number_to_hex(color[0]) + self.number_to_hex(color[1]) + self.number_to_hex(color[2])
        return "\cellcolor[HTML]{" + hex_color + "}"

    def number_to_hex(self, number):
        text = format(round(number), "X")
        if len(text) == 1:
            return "0" + text
        else:
            return text

    def get_time(self, result):
        if not result.not_supported and not result.threw_error and not result.timed_out:
            if Measurements.WALL_TIME in result.measurements:
                return result.measurements[Measurements.WALL_TIME]
        return self.benchmark.time_limit*2

