from enum import Enum


class Measurements(Enum):
    STATES = "states"
    TRANSITIONS = "transitions"
    BRANCHES = "branches"
    STATES_AFTER_BISIMULATION = "states_after_bisimulation"
    TRANSITIONS_AFTER_BISIMULATION = "transitions_after_bisimulation"
    BRANCHES_AFTER_BISIMULATION = "branches_after_bisimulation"

    WALL_TIME = "wall_time"
    TOOL_REPORTED_TIME = "tool_reported_time"
    PARSING_TIME = "parsing_time"
    STATE_SPACE_TIME = "state_space_time"
    BISIMULATION_TIME = "bisimulation_time"
    PROPERTY_TIME = "property_time"

    PROPERTY_OUTPUT = "property_output"
