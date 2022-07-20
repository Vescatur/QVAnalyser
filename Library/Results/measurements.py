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

    def to_label_text(self) -> str:
        if self == Measurements.TRANSITIONS:
            return "Number of transitions"
        if self == Measurements.BRANCHES:
            return "Number of branches"
        if self == Measurements.STATES:
            return "Number of states"
        if self == Measurements.PARSING_TIME:
            return "Time to parse file"
        if self == Measurements.STATE_SPACE_TIME:
            return "Time to generate state space"
        if self == Measurements.PROPERTY_TIME:
            return "Time to calculate result"
        if self == Measurements.TOOL_REPORTED_TIME:
            return "Time reported by tool"
        if self == Measurements.WALL_TIME:
            return "Wall time"

    def is_characteristic(self) -> bool:
        if self == Measurements.TRANSITIONS:
            return True
        if self == Measurements.BRANCHES:
            return True
        if self == Measurements.STATES:
            return True
        return False