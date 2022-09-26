import numpy as np

from Specific.Output.Matrix.algorithm_matrix import AlgorithmMatrix
from Library.Results.measurements import Measurements


class MatrixSimilar(AlgorithmMatrix):

    def generate_cell_text(self, algorithm_left, algorithm_top):
        use_correlation = False

        time_limit = self.benchmark.time_limit
        total = 0
        differences = 0

        times_left = []
        times_top = []
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if self.instance_filter(instance):
                    result_left = self.find_result_with_algorithm(instance, algorithm_left)
                    result_top = self.find_result_with_algorithm(instance, algorithm_top)
                    if not result_left.not_supported and not result_top.not_supported:
                        total += time_limit*2
                        time_left = self.get_time(result_left, time_limit)
                        time_top = self.get_time(result_top, time_limit)
                        differences += abs(time_left-time_top)
                        times_left.append(time_left)
                        times_top.append(time_top)

        if total <= 3:
            return ""
        if use_correlation:
            R2 = np.corrcoef(times_left,times_top)
            return str(round(R2[0][1]*100))
        else:
            if self.use_latex:
                similarity_metric = 1-(differences/total)
                display_metric = round(similarity_metric*10)
                cell_content = ""
                if display_metric == 10:
                    cell_content = "+"
                else:
                    cell_content = str(display_metric)
                color = None
                white = np.array([255, 255, 255])
                if similarity_metric >= 0.8:
                    green = np.array([87, 187, 138])
                    factor = (similarity_metric-0.8)/0.2
                    color = green*factor+white*(1-factor)
                else:
                    red = np.array([230, 124, 115])
                    factor = similarity_metric/0.8
                    color = white*factor+red*(1-factor)

                hex_color = self.number_to_hex(color[0]) + self.number_to_hex(color[1]) + self.number_to_hex(color[2])
                return "\\fontcellsimilar \cellcolor[HTML]{"+hex_color+"}"+cell_content
            else:
                similarity_metric = 1-(differences/total)
                return str(round(similarity_metric*1000))

    def get_time(self, result_top, time_limit):
        time_top = time_limit * 2
        if not result_top.threw_error and not result_top.timed_out:
            if Measurements.WALL_TIME in result_top.measurements:
                time_top = result_top.measurements[Measurements.WALL_TIME]
        return time_top

    def number_to_hex(self, number):
        text = format(round(number),"X")
        if len(text) == 1:
            return "0"+text
        else:
            return text


