import re

import numpy as np

from Library.Results.measurements import Measurements
from Specific.Output.Matrix.text_file_printer import TextFileWriter


def first_element(item):
    return item[0]

class MatrixBenchmarkInstances(object):

    def __init__(self, benchmark,instance_filter,use_latex,name):
        with TextFileWriter(name) as self.writer:
            self.benchmark = benchmark
            self.use_latex = use_latex
    
            unsorted_instances = self.get_instances(benchmark,instance_filter)
            self.instances = self.order_instance_by_time(unsorted_instances)
            self.print_top_row()
            self.print_body()
            self.print_bottom_row()

    def get_instances(self, benchmark,instance_filter):
        instances = []
        for sequence in self.benchmark.benchmark_sequences:
            for instance in sequence.benchmark_instances:
                if instance_filter(instance):
                    instances.append(instance)
        return instances

    def order_instance_by_time(self, unsorted_instances):
        instances_with_time = []
        for instance in unsorted_instances:
            total = 0
            total_time = 0
            for result in instance.results:
                if  not (result.algorithm_name == "Prism Jacobi with over-relaxation explicit" or result.algorithm_name == "Prism successive over-relaxation explicit" or result.algorithm_name == "Prism backwards successive over-relaxation explicit"):
                    if not result.not_supported:
                        total += 1
                        time = self.benchmark.time_limit*2
                        if not result.threw_error and not result.timed_out:
                            if Measurements.WALL_TIME in result.measurements:
                                time = result.measurements[Measurements.WALL_TIME]
                        total_time += time
            instances_with_time.append((total_time/total,instance))
        sorted_time_instances = sorted(instances_with_time,key=first_element)
        sorted_instances = []
        for time_instance in sorted_time_instances:
            sorted_instances.append(time_instance[1])
        return sorted_instances


    def instance_to_display_name(self,instance):
        benchmark_name = instance.benchmark_sequence.benchmark_model.name
        regex = r"\/[a-zA-Z-]*"
        match = re.search(regex, benchmark_name)
        short_name1 = match.group(0)
        short_name2 = short_name1[1:] # Removes first character
        display_name = short_name2.replace("_", " ").replace("-", " ")
        property_name = instance.benchmark_sequence.property_name
        return display_name + " " + property_name.replace("_","\_")

    def print_top_row(self):
        if self.use_latex:
            self.writer.print("\\begin{table}[htbp]")
            self.writer.print("\centering")
            allignments = "l"*(len(self.instances)+1+3)
            self.writer.print("\\begin{tabular}{"+allignments+"}")
            self.writer.print("\\toprule")
            line = ""
            for instance in self.instances:
                display_name = self.instance_to_display_name(instance)
                line += "\t& \\fonttopsimilar \\rotatebox{90}{"+display_name + "}"

            line += "\t& \\rotatebox{90}{Average time}"
            line += "\t& \\rotatebox{90}{Average states}"

            self.writer.print(line + " \\\\")
        else:
            line = "\t"
            for instance in self.instances:
                line += self.instance_to_display_name(instance) + "\t"
            self.writer.print(line)

    def print_body(self):
        index = 1
        for instance in self.instances:
            self.print_body_line(instance, index)
            index += 1

    def print_body_line(self, instance_left,index):
        display_name = self.instance_to_display_name(instance_left)

        if self.use_latex:
            line = str(index) + " " + display_name
            for instance_top in self.instances:
                line += "\t& " + str(self.generate_cell_text(instance_left, instance_top))

        else:
            line = str(index) + " " + display_name + "\t"
            for instance_top in self.instances:
                line += str(self.generate_cell_text(instance_left, instance_top)) + "\t"

        total = 0
        total_time = 0

        total2 = 0
        total_states = 0
        for result in instance_left.results:
            if not result.not_supported:
                total += 1
                time = self.benchmark.time_limit*2
                if not result.threw_error and not result.timed_out:
                    if Measurements.WALL_TIME in result.measurements:
                        time = result.measurements[Measurements.WALL_TIME]
                total_time += time
                if Measurements.STATES in result.measurements:
                    total2 += 1
                    total_states += result.measurements[Measurements.STATES]

        if self.use_latex:
            line += "\t& " + str(round(total_time/total)).replace(".",",")
            if total2 != 0:
                line += "\t& " + str(round(total_states/total2)).replace(".",",")
            else:
                line += "\t& "
        else:
            line += "\t" + str(round(total_time/total)).replace(".",",")
            if total2 != 0:
                line += "\t" + str(round(total_states/total2)).replace(".",",")
            else:
                line += "\t"

        if self.use_latex:
            self.writer.print(line + " \\\\")
        else:
            self.writer.print(line)

    def generate_cell_text(self, instance_left, instance_top):
        time_limit = self.benchmark.time_limit
        total = 0
        differences = 0
        for algorithm in self.benchmark.algorithms:
            if algorithm.name == "Prism Jacobi with over-relaxation explicit" or algorithm.name == "Prism successive over-relaxation explicit" or algorithm.name == "Prism backwards successive over-relaxation explicit":
                continue
            result_left = self.find_result_with_algorithm(instance_left, algorithm)
            result_top = self.find_result_with_algorithm(instance_top, algorithm)
            if not result_left.not_supported and not result_top.not_supported:
                total += time_limit*2
                time_left = time_limit*2
                if not result_left.threw_error and not result_left.timed_out:
                    if Measurements.WALL_TIME in result_left.measurements:
                        time_left = result_left.measurements[Measurements.WALL_TIME]
                time_top = time_limit*2
                if not result_top.threw_error and not result_top.timed_out:
                    if Measurements.WALL_TIME in result_top.measurements:
                        time_top = result_top.measurements[Measurements.WALL_TIME]
                differences += abs(time_left-time_top)
        if total == 0:
            return ""
        similarity_metric = 1-(differences/total)
        if self.use_latex:
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
            return str(round(similarity_metric*1000))

    def find_result_with_algorithm(self, instance, algorithm):
        for result in instance.results:
            if result.algorithm_name == algorithm.name:
                return result

    def print_bottom_row(self):
        if self.use_latex:
            self.writer.print("\\bottomrule")
            self.writer.print("\\end{tabular}")
            self.writer.print("\\caption{??}")
            self.writer.print("\\label{table:??}")
            self.writer.print("\\end{table}")

    def number_to_hex(self, number):
        text = format(round(number),"X")
        if len(text) == 1:
            return "0"+text
        else:
            return text
