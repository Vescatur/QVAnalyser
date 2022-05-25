from Library.storage import Storage


def to_tabs(list):
    list_of_strings = map(str, list)
    return ", ".join(list_of_strings)


storage = Storage()
execution_sequences = storage.load_latest_execution_sequences()

for execution_sequence in execution_sequences:
    print("")
    print(execution_sequence.name)
    print(to_tabs(["states", "wall time", "total time", "state space time", "property time"]))
    for execution in execution_sequence.executions:
        if execution.timeout:
            print("")
        else:
            print(to_tabs([execution.states, execution.wall_time, execution.total_time, execution.state_space_time, execution.property_time]))
