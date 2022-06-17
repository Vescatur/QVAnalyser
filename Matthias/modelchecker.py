from abc import abstractmethod

from benchmarking_pmc.modelcheckers.tool import Tool
from benchmarking_pmc.results.run_result import ModelCheckingResult


class Modelchecker(Tool):
    """
    An abstraction of probabilistic model checkers for concrete systems
    """

    def __init__(self, name, configuration, not_supported_messages=[], memout_messages=[], binary=None):
        """
        Constructor.
        :param name: Suffix name of model checker (uniquely identifies this model checker and its configuration).
        :param binary: Path to binary of the tool.
        :param configuration: Configuration as a list of arguments.
        :param not_supported_messages: List of key phrases indicating not supported functionality.
            If any of these strings occur in the output the given functionality is not supported.
        :param memout_messages: List of key phrases indicating that the memory limit was reached.
            If any of these strings occur in the output the result will be MemOut.
        """
        Tool.__init__(self, name, configuration, not_supported_messages=not_supported_messages, memout_messages=memout_messages, binary=binary)

    @abstractmethod
    def parse_building_time(self, line):
        """
        Parse the given line for the time needed to build the model.
        :param line Current line to parse.
        :return The building time if one was found else None
        """
        raise NotImplementedError

    def parse_bisimulation_time(self, line):
        """
        Parse the given line for the time needed to compute the bisimulation quotient of the model.
        :param line Current line to parse.
        :return The bisimulation time if one was found else None
        """
        raise NotImplementedError

    @abstractmethod
    def parse_modelchecking_time(self, line):
        """
        Parse the given line for the time needed to check the model.
        :param line Current line to parse.
        :return The modelchecking time if one was found else None
        """
        raise NotImplementedError

    @abstractmethod
    def parse_no_states(self, line):
        """
        Parse the given line for the number of states in the model.
        :param line Current line to parse.
        :return The number of states in the model if they were found else None
        """
        raise NotImplementedError

    @abstractmethod
    def parse_no_transitions(self, line):
        """
        Parse the given line for the number of transitions in the model.
        :param line Current line to parse.
        :return The number of transitions in the model if they were found else None
        """
        raise NotImplementedError

    def analyze_result(self, benchmark_run, log_file, mc_result=None):
        """
        Analyzes the benchmark run and returns the model checking result.
        :param benchmark_run: The benchmark which was run
        :param log_file: The log file of the benchmark run
        :param mc_result: Model checking result which should be filled
        :return: ModelCheckingResult
        """
        if mc_result is None:
            mc_result = ModelCheckingResult()
        mc_result = Tool.analyze_result(self, benchmark_run, log_file, mc_result)

        # Parse log file
        for line in open(log_file, 'r').readlines():
            # Building Times
            building_time = self.parse_building_time(line)
            if building_time is not None:
                mc_result.building_time = building_time
                continue
            # Bisimulation Times
            bisimulation_time = self.parse_bisimulation_time(line)
            if bisimulation_time is not None:
                mc_result.bisimulation_time = bisimulation_time
                continue
            # Modelchecking Times
            mc_time = self.parse_modelchecking_time(line)
            if mc_time is not None:
                mc_result.modelchecking_time = mc_time
                continue

            # No. states in model
            states = self.parse_no_states(line)
            if states is not None:
                mc_result.no_states = states
                continue
            # No. transitions in model
            transitions = self.parse_no_transitions(line)
            if transitions is not None:
                mc_result.no_transitions = transitions
                continue

        return mc_result

    def __str__(self):
        return self.get_name() + " with config: " + ", ".join(self.configuration())
