import re

from benchmarking_pmc.modelcheckers.modelchecker import Modelchecker
from benchmarking_pmc.modelcheckers.arguments.engine import Engine, EngineOption


class Prism(Modelchecker):
    """
    Prism modelchecker.
    """

    def __init__(self, name, configuration, binary=None):
        not_supported = [
            "Explicit engine does not yet handle transition rewards for D/CTMCs",
            "Explicit engine does not yet handle the S operator for CTMCs",
            "Explicit engine does not yet handle the S reward operator",
            "Cannot do explicit-state reachability if there are multiple initial states",
            "Parametric engine does not yet handle the C operator in the R operator",
            "Parametric engine does not yet handle the I operator in the R operator",
            "Bounded until operator not supported by parametric engine",
            # make more general
            "cannot handle expression min_backoff_after_success in parametric analysis",
        ]
        memout_messages = [
            "There is insufficient memory",
            "Out of memory",
            "java.lang.OutOfMemoryError"
        ]
        Modelchecker.__init__(self, name, configuration, not_supported_messages=not_supported, memout_messages=memout_messages, binary=binary)

    @staticmethod
    def binary_name():
        return "prism"

    def run_arguments(self, benchmark_run, model_prefix, logfile):
        arguments = [benchmark_run.model_path(model_prefix), benchmark_run.property_path(model_prefix)]
        # Set constants
        if len(benchmark_run.constants()) > 0:
            arguments.extend(["-const", benchmark_run.constants_string()])

        arguments.extend(self.configuration())
        # Convert arguments
        for argument in benchmark_run.arguments():
            if argument.startswith("maxiter"):
                arguments.append("-maxiters")
                arguments.append(Modelchecker.get_value(argument))
            elif argument.startswith("parameter"):
                arguments.append("-param")
                arguments.append(Modelchecker.get_value(argument))
            else:
                # Argument not known
                return None
        return arguments

    def run_benchmark(self, benchmark, config, logfile):
        arguments = self.run_arguments(benchmark, config.model_prefix, logfile)
        arguments = ["-javamaxmem", "{0}m".format(config.memout)] + arguments
        return self._run_benchmark(benchmark, arguments, config, logfile, memout=-1)

    def convert_engine(self, engine):
        """
        Convert engine to cmdline options.
        :param engine: Engine.
        :return: Cmdline options.
        """
        if engine == EngineOption.SPARSE:
            cmdline_args = ["-ex"]
        elif engine == EngineOption.CUDD:
            cmdline_args = ["-m", "-cuddmaxmem", "4096m"]
        elif engine == EngineOption.HYBRID:
            cmdline_args = ["-s", "-cuddmaxmem", "4096m"]
        elif engine == EngineOption.EXACT:
            cmdline_args = ["-exact", "-politer"]
        elif engine == EngineOption.PRISM_HYBRID:
            cmdline_args = ["-h", "-cuddmaxmem", "4096m"]
        else:
            raise NotImplementedError("'{}' not support by Prism.".format(engine))
        return cmdline_args

    def convert_argument(self, argument):
        if isinstance(argument, Engine):
            return self.convert_engine(argument.engine)
        else:
            raise NotImplementedError("Prism does not support argument {}".format(argument))

    def parse_error(self, line):
        match = re.search(r"Error: (.*)", line)
        if match:
            return match.group(1)
        match = re.search(r"Exception in thread \"main\" (.*)", line)
        if match:
            return match.group(1)
        return None

    def parse_result(self, line):
        match = re.search(r"Result: (.*) \((.*)\)", line)
        if match:
            return match.group(1)
        match = re.search(r"Result \(.*\): (.*)", line)
        if match:
            return match.group(1)
        return None

    def parse_building_time(self, line):
        match = re.search(r"Time for model construction: (.*) seconds", line)
        if match:
            return match.group(1)
        return None

    def parse_bisimulation_time(self, line):
        # Prism does not output model properties
        return None

    def parse_modelchecking_time(self, line):
        match = re.search(r"Time for model checking: (.*) seconds", line)
        if match:
            return match.group(1)
        return None

    def parse_no_states(self, line):
        match = re.search(r"States:\s*(\d+)", line)
        if match:
            return match.group(1)
        return None

    def parse_no_transitions(self, line):
        match = re.search(r"Transitions:\s*(\d+)", line)
        if match:
            return match.group(1)
        return None
