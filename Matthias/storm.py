import re

from benchmarking_pmc.modelcheckers.modelchecker import Modelchecker
from benchmarking_pmc.modelcheckers.arguments.engine import Engine, EngineOption
from benchmarking_pmc.results.run_result import StormModelCheckingResult
from benchmarking_pmc.utility.os_functions import get_file_extension


class Storm(Modelchecker):
    """
    Storm modelchecker.
    """

    def __init__(self, name, configuration, not_supported_messages=None, memout_messages=None, binary=None):
        if not_supported_messages is None:
            not_supported_messages = []
        not_supported = not_supported_messages + [
            "NotSupportedException:",
            "This functionality is not yet implemented",
            "Computing cumulative rewards is unsupported for this value type.",
            "Computing instantaneous rewards is unsupported for this value type.",
            "Computing bounded until probabilities is unsupported for this value type.",
            "Currently exploration-based verification is only available for DTMCs and MDPs.",
            "skipped, because the formula cannot be handled by the selected engine/method",
            "Bisimulation is currently supported for models with state rewards only.",
            "property is unsupported by selected engine/settings",
            "Property is unsupported by selected engine/settings",
            "Can only use sparse engine with explicit input.",
            "Dd engine cannot verify MDPs with this data type."
        ]
        if memout_messages is None:
            memout_messages = []
        memout_messages += [
            "std::bad_alloc",
            "Out of virtual memory",
            "GNU MP: Cannot allocate memory",
            "Maximum memory exceeded"
        ]
        Modelchecker.__init__(self, name, configuration, not_supported_messages=not_supported, memout_messages=memout_messages, binary=binary)
        self.result_in_next_line = False
        self.status = "start"

    @staticmethod
    def binary_name():
        return "storm"

    def run_arguments(self, benchmark_run, model_prefix, logfile):
        is_jani = False
        # Set correct model parser
        model_path = benchmark_run.model_path(model_prefix)
        if get_file_extension(model_path) == ".jani":
            is_jani = True
            arguments = ["--jani", model_path]
        else:
            if get_file_extension(model_path) == ".drn":
                arguments = ["-drn", model_path]
            else:
                arguments = ["--prism", model_path]
        # Set property
        if is_jani:
            arguments.extend(["--janiproperty", benchmark_run.property_string()])
        else:
            arguments.extend(["--prop", benchmark_run.property_path(model_prefix)])
        # Set constants
        if len(benchmark_run.constants()) > 0:
            arguments.extend(["-const", benchmark_run.constants_string()])

        arguments.extend(self.configuration())
        # Convert arguments
        for argument in benchmark_run.arguments():
            if argument.startswith("maxiter"):
                arguments.append("--maxiter")
                arguments.append(Modelchecker.get_value(argument))
            else:
                # Argument not known
                return None
        if not is_jani:
            arguments.append("-pc")
        return arguments

    def run_benchmark(self, benchmark, config, logfile):
        arguments = self.run_arguments(benchmark, config.model_prefix, logfile)
        return self._run_benchmark(benchmark, arguments, config, logfile)

    def convert_engine(self, engine):
        """
        Convert engine to cmdline options.
        :param engine: Engine.
        :return: Cmdline options.
        """
        cmdline_args = ["-e"]
        if engine == EngineOption.SPARSE:
            cmdline_args.append("sparse")
        elif engine == EngineOption.CUDD:
            cmdline_args.append("dd")
            cmdline_args += ["--ddlib", "cudd", "--cudd:maxmem", "4096"]
        elif engine == EngineOption.SYLVAN:
            cmdline_args.append("dd")
            cmdline_args += ["--ddlib", "sylvan", "--sylvan:maxmem", "4096", "--sylvan:threads", "8"]
        elif engine == EngineOption.HYBRID:
            cmdline_args.append("hybrid")
            cmdline_args += ["--cudd:maxmem", "4096"]
        elif engine == EngineOption.EXACT:
            cmdline_args.append("sparse")
            cmdline_args += ["--exact", "--minmax:method", "pi"]
        elif engine == EngineOption.EXPLORATION:
            cmdline_args.append("expl")
        else:
            raise NotImplementedError("'{}' not support by Storm.".format(engine))
        return cmdline_args

    def convert_argument(self, argument):
        if isinstance(argument, Engine):
            return self.convert_engine(argument.engine)
        else:
            raise NotImplementedError("Storm does not support argument {}".format(argument))

    def analyze_result(self, benchmark_run, log_file, mc_result=None):
        """
        Analyzes the benchmark run and returns the model checking result.
        :param benchmark_run: The benchmark which was run
        :param log_file: The log file of the benchmark run
        :param mc_result: Model checking result which should be filled
        :return: ModelCheckingResult
        """
        if mc_result is None:
            mc_result = StormModelCheckingResult()
        mc_result = Modelchecker.analyze_result(self, benchmark_run, log_file, mc_result)

        # Parse log file
        for line in open(log_file, 'r').readlines():
            # Update status in log file
            match = re.search(r"Time for model construction", line)
            if match:
                self.status = "build"
            match = re.search(r"Time for model preprocessing", line)
            if match:
                self.status = "bisim"
            match = re.search(r"Model checking property", line)
            if match:
                self.status = "modelchecking"

            # No. states in model
            states = self.parse_no_states(line)
            if states is not None:
                mc_result.no_states = states
            # No. transitions in model
            transitions = self.parse_no_transitions(line)
            if transitions is not None:
                mc_result.no_transitions = transitions

            # No. states in bisimulation model
            states = self.parse_no_states_bisim(line)
            if states is not None:
                mc_result.no_states_bisim = states
            # No. transitions in bisimulation model
            transitions = self.parse_no_transitions_bisim(line)
            if transitions is not None:
                mc_result.no_transitions_bisim = transitions

        return mc_result

    def parse_error(self, line):
        match = re.search(r"ERROR (.*)", line)
        if match:
            return match.group(1)
        match = re.search(r"ERROR: (.*)", line)
        if match:
            return match.group(1)
        return None

    def parse_result(self, line):
        if self.result_in_next_line:
            self.result_in_next_line = False
            return line.strip()

        match = re.search(r"Result (.*): (.*)", line)
        if match:
            if match.group(2) == "":
                # Workaround if the result is in the next line
                self.result_in_next_line = True
                return None

            # Check for exact result
            match_exact = re.search(r"(.*) \(approx. .*\)", match.group(2))
            if match_exact:
                return match_exact.group(1)
            else:
                return match.group(2)
        return None

    def parse_building_time(self, line):
        match = re.search(r"Time for model construction: (.*)s", line)
        if match:
            return match.group(1)
        return None

    def parse_bisimulation_time(self, line):
        match = re.search(r"Time for model preprocessing: (.*)s", line)
        if match:
            return match.group(1)
        return None

    def parse_modelchecking_time(self, line):
        match = re.search(r"Time for model checking: (.*)s", line)
        if match:
            return match.group(1)
        return None

    def parse_no_states(self, line):
        if self.status == "build":
            # Only search after model was build
            match = re.search(r"States:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_no_transitions(self, line):
        if self.status == "build":
            # Only search after model was build
            match = re.search(r"Transitions:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_no_states_bisim(self, line):
        """
        Parse the given line for the number of states in the bisimulation model.
        :param line Current line to parse.
        :return The number of states in the bisimulation model if they were found else None
        """
        if self.status == "bisim":
            # Only search after bisimulation was applied
            match = re.search(r"States:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None

    def parse_no_transitions_bisim(self, line):
        """
        Parse the given line for the number of transitions in the bisimulation model.
        :param line Current line to parse.
        :return The number of transitions in the bisimulation model if they were found else None
        """
        if self.status == "bisim":
            # Only search after bisimulation was applied
            match = re.search(r"Transitions:\s*(\d+)", line)
            if match:
                return match.group(1)
        return None
