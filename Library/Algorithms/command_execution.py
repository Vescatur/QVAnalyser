import os
import subprocess
import threading
import time

from Library.Results.command_result import CommandResult


class CommandExecution(object):
    """ Represents the execution of a single command line argument. """

    def __init__(self, command_line_str, benchmark):
        self.command_line_str = command_line_str
        self.benchmark = benchmark
        self.result = CommandResult(command_line_str)
        self.process = None
        self.run()

    def run(self):
        self.process = self.create_process()
        start_time = time.time()
        timer = threading.Timer(self.benchmark.time_limit, self.stop_after_timeout)
        timer.start()
        try:
            self.result.output_log, self.result.error_log = self.process.communicate()
        except Exception as e:
            self.result.exception = e
        finally:
            timer.cancel()
            self.result.wall_time = time.time() - start_time
            self.result.return_code = self.process.returncode

    def create_process(self):
        command_line_list = self.command_line_str.split()
        command_line_list[0] = os.path.expanduser(command_line_list[0])
        return subprocess\
            .Popen(command_line_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, encoding='utf-8')

    def stop_after_timeout(self):
        self.result.timed_out = True
        self.process.kill()