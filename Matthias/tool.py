import re
from abc import ABC, abstractmethod

from benchmarking_pmc.modelcheckers.arguments.base import Flag, Setting
from benchmarking_pmc.results.run_result import ErrorType, RunResult
from benchmarking_pmc.utility import os_functions
from benchmarking_pmc.utility.exceptions import ToolNotFoundError, ResultError


class Tool(ABC):
    """
    An abstraction of tools used for benchmarking
    """

    def __init__(self, name, configuration, not_supported_messages=[], memout_messages=[], binary=None):
        """
        Constructor.
        :param name: Suffix name of tool (uniquely identifies this tool and its configuration).
        :param configuration: Configuration as a list of arguments.
        :param not_supported_messages: List of key phrases indicating not supported functionality.
            If any of these strings occur in the output the given functionality is not supported.
        :param memout_messages: List of key phrases indicating that the memory limit was reached.
            If any of these strings occur in the output the result will be MemOut.
        :param binary: Path to binary of the tool.
        """
        # Construct name from base class name + suffix
        self.name = name
        self.tool_binary = binary
        self.config = self.convert_arguments(configuration)
        # Construct regexes for specific error messages
        self._regex_not_supported = "|".join([re.escape(m) for m in not_supported_messages])
        self._regex_memout = "|".join([re.escape(m) for m in memout_messages])

    def get_name(self):
        """
        Get the name of the tool.
        :return: A string with the name of the tool
        """
        return "{}-{}".format(self.__class__.__name__, self.name)

    @staticmethod
    def binary_name():
        """
        Get name of the binary.
        :return: Name of binary.
        """
        raise NotImplementedError

    def binary(self, tool_paths):
        """
        Get the binary for the tool.
        If no binary was given in the constructor, the binary is looked up in the tool paths.
        :return: Path of the binary
        """
        if self.tool_binary is not None:
            return self.tool_binary
        else:
            tool_name = self.__class__.__name__
            if tool_name in tool_paths:
                return tool_paths[tool_name]
            else:
                raise ToolNotFoundError(tool_name)

    def configuration(self):
        """
        Get the configuration, i.e. the arguments for the tool.
        :return: List of arguments
        """
        return self.config

    @abstractmethod
    def convert_argument(self, argument):
        """
        Convert the given argument in the format supported by the tool.
        :param argument: Tool argument.
        :return: List of strings representing the cmdline arguments.
        """
        raise NotImplementedError

    def convert_arguments(self, arguments):
        """
        Convert the given arguments in the format supported by the tool.
        :param arguments: Tool arguments.
        :return: List of strings representing the cmdline arguments.
        """
        cmdline_args = []
        for argument in arguments:
            if isinstance(argument, str):
                cmdline_args.append(argument)
            elif isinstance(argument, Flag):
                cmdline_args += argument.get_arguments()
            elif isinstance(argument, Setting):
                cmdline_args += argument.get_arguments()
            else:
                cmdline_args += self.convert_argument(argument)
        return cmdline_args

    @staticmethod
    def get_value(argument):
        """
        Get value of argument.
        :param argument: Complete argument.
        :return: Everything after first '='.
        """
        return argument.split('=', 1)[1]

    @abstractmethod
    def run_arguments(self, benchmark, model_prefix, logfile):
        """
        Get the arguments for running the given benchmark.
        :param benchmark: The benchmark to run.
        :param model_prefix: The path prefix for the model file.
        :param logfile: The log file.
        :return: List of arguments to run
        """
        raise NotImplementedError

    @abstractmethod
    def run_benchmark(self, benchmark, config, logfile):
        """
        Run the given benchmark.
        :param benchmark: The benchmark to run
        :param config: General configuration.
        :param logfile: Log file for tool output.
        :return: Exit code of the benchmark run.
        """
        raise NotImplementedError

    def _run_benchmark(self, benchmark, arguments, config, logfile, timeout=None, memout=None, model_prefix=None):
        """
        Run the given benchmark.
        :param benchmark: The benchmark to run
        :param arguments: Arguments to pass on
        :param config: General configuration.
        :param logfile: Log file.
        :param timeout: The timeout in seconds. -1 means no timeout.
        :param memout: The memory limit in MB. -1 means no limit.
        :param log_prefix: The path prefix for log files.
        :param model_prefix: The path prefix for the model file.
        :return: Exit code of the benchmark run.
        """
        with open(logfile, "w") as f:
            # Write benchmark information
            f.write(benchmark.csv_string(model_prefix if model_prefix is not None else config.model_prefix) + ";" + self.get_name() + "\n")

        tout = timeout if timeout is not None else config.timeout
        mout = memout if memout is not None else config.memout
        return os_functions.run_process(self.binary(config.paths), arguments, logfile, tout, mout)

    @abstractmethod
    def parse_error(self, line):
        """
        Parse the given line for an error.
        :param line Current line to parse.
        :return The error message if one was found else None
        """
        raise NotImplementedError

    @abstractmethod
    def parse_result(self, line):
        """
        Parse the given line for a result.
        :param line Current line to parse.
        :return The tool result if one was found else None
        """
        raise NotImplementedError

    def _analyze_result_general(self, benchmark_run, log_file, benchmark_result=None):
        """
        Perform first (general) pass of parsing.
        Analyzes the benchmark run and returns the basic benchmark results.
        :param benchmark_run: The benchmark which was run
        :param log_file: The log file of the benchmark run
        :param benchmark_result: Benchmark result which should be filled
        :return BenchmarkResult
        """
        if benchmark_result is None:
            benchmark_result = RunResult()
        benchmark_result.benchmark = benchmark_run
        benchmark_result.modelchecker = self.get_name()
        benchmark_result.logfile_path = log_file

        # Parse log file and fill general information
        for line in open(log_file, 'r').readlines():
            # Wall time
            match_time = re.search(r"Wall time: (.*)s", line)
            if match_time:
                if match_time.group(1) != "%e": # Ignore original call
                    benchmark_result.total_time = match_time.group(1)
                continue
            # User time
            match_time = re.search(r"User time: (.*)s", line)
            if match_time:
                if match_time.group(1) != "%U": # Ignore original call
                    benchmark_result.user_time = match_time.group(1)
                continue
            # System time
            match_time = re.search(r"System time: (.*)s", line)
            if match_time:
                if match_time.group(1) != "%S": # Ignore original call
                    benchmark_result.system_time = match_time.group(1)
                continue

            # Not supported
            if self._regex_not_supported:
                match_not_supported = re.search(self._regex_not_supported, line)
                if match_not_supported:
                    benchmark_result.error = ErrorType.NOT_SUPPORTED.name
                    continue

            # MemOut
            if self._regex_memout:
                match_memout = re.search(self._regex_memout, line)
                if match_memout:
                    benchmark_result.error = ErrorType.MEMOUT.name
                    continue

            # External error
            match_error = re.search(r"BenchmarkingCode: (.*)", line)
            if match_error:
                if match_error.group(1) == "Timeout":
                    benchmark_result.error = ErrorType.TIMEOUT.name
                elif match_error.group(1) == "Memout":
                    benchmark_result.error = ErrorType.MEMOUT.name
                else:
                    benchmark_result.error = "BenchmarkingCode: " + match_error.group(1)
                continue
        if benchmark_result.total_time is None:
            # No timing information written
            # -> We assume a timeout
            benchmark_result.error = ErrorType.TIMEOUT.name
            benchmark_result.total_time = 0
            benchmark_result.user_time = 0
            benchmark_result.system_time = 0
        return benchmark_result

    def analyze_result(self, benchmark_run, log_file, benchmark_result=None):
        """
        Analyzes the benchmark run and returns the basic benchmark results.
        :param benchmark_run: The benchmark which was run
        :param log_file: The log file of the benchmark run
        :param benchmark_result: Benchmark result which should be filled
        :return BenchmarkResult
        """

        # Perform the first pass for general information
        benchmark_result = self._analyze_result_general(benchmark_run, log_file, benchmark_result=benchmark_result)

        # Parse log file
        has_error = False
        expect_error = benchmark_result.is_error() and benchmark_result.error.startswith("BenchmarkingCode")
        for line in open(log_file, 'r').readlines():
            # Error
            if not has_error:
                error = self.parse_error(line)
                if error is not None:
                    benchmark_result.error = error
                    has_error = True
                    continue

            # Result
            result = self.parse_result(line)
            if result is not None:
                benchmark_result.result = result
                continue

        if expect_error and not has_error:
            raise ResultError("Expected error but none found for {}".format(log_file))
        if not benchmark_result.is_error() and benchmark_result.result is None:
            raise ResultError("Neither result nor error found for {}".format(log_file))
        return benchmark_result

    def __str__(self):
        return self.get_name() + " with config: " + ", ".join(self.configuration())
