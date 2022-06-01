from enum import Enum


class Statistics(Enum):
    STATES = "states"
    TOOL_REPORTED_TIME = "tool_reported_time"
    STATE_SPACE_TIME = "state_space_time"
    PROPERTY_TIME = "property_time"
    PROPERTY_OUTPUT = "property_output"
    WALL_TIME = "wall_time"
