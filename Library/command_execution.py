import os
import signal
import subprocess
import threading
import time


class CommandExecution(object):
    """ Represents the execution of a single command line argument. """
    def __init__(self, command_line_str, time_limit):
        self.time_limit = time_limit
        self.command_line_str = command_line_str
        self.timeout = None
        self.return_code = None
        self.output = None
        self.wall_time = None
        self.proc = None

    def stop(self):
        self.timeout = True
        self.proc.kill()
        self.proc = None

    def stop_after_timeout(self):
        self.timeout = False
        self.proc.send_signal(signal.SIGINT)
        time.sleep(20)
        self.proc.kill()
        self.proc = None

    def run(self):
        command_line_list = self.command_line_str.split()
        command_line_list[0] = os.path.expanduser(command_line_list[0])
        self.proc = subprocess.Popen(command_line_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, encoding='utf-8')
        start_time = time.time()
        timer = threading.Timer(self.time_limit, self.stop)
        self.timeout = False
        self.output = ""
        timer.start()
        stdout = ""
        stderr = ""
        try:
            stdout, stderr = self.proc.communicate()
        except Exception as e:
            self.output = self.output + "Error when executing the command:\n{}\n".format(e)
        finally:
            timer.cancel()
            self.wall_time = time.time() - start_time
            self.return_code = self.proc.returncode
            self.proc = None
        self.output = self.output + stdout
        if len(stderr) > 0:
            self.output = self.output + "\n" + "#"*30 + "Output to stderr" + "#"*30 + "\n" + stderr
        if self.timeout and self.wall_time <= self.time_limit:
            print("WARN: A timeout was triggered although the measured time is {} seconds which is still below the time limit of {} seconds"
                  .format(self.wall_time, self.time_limit))
