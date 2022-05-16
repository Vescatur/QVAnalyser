# https://www.modestchecker.net/Downloads/Version.txt
# https://www.modestchecker.net/Downloads/License.txt
from Library.CommandExecution import CommandExecution


def TestPerformance():

    for size in range(20,40):
        error = False
        timeout = False
        wall_time = 0.0
        logs = []
        time_limit = 60*5

        commands = [1]
        commands[0] = "./../Resources/Tools/Modest/modest.exe check ./../Resources/BenchmarkModels/haddad-monmege.v1.jani -E N={},p=0.7".format(size)

        for command in commands:
            execution = CommandExecution()
            execution.run(command, time_limit)
            log = execution.output
            wall_time_command = execution.wall_time
            if execution.timeout:
                return_code = None
            else:
                return_code = execution.return_code

            wall_time = wall_time + wall_time_command
            logs.append(
                "Command:\t{}\nWallclock time:\t{}\nReturn code:\t{}\nOutput:\n{}\n".format(command, wall_time_command, return_code, log))
            if return_code is None:
                timeout = True
                logs[-1] = logs[-1] + "\n" + "-" * 10 + "\nComputation aborted after {} seconds since the total time limit of {} seconds was exceeded.\n".format(
                    wall_time, time_limit)
                break
            else:
                return_code = return_code
                error = error or return_code != 0
        print(wall_time)
        print(logs)
