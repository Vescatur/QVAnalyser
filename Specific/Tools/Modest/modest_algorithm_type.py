
from enum import Enum


class ModestAlgorithmType(Enum):
    VALUE_ITERATION = "ValueIteration"
    INTERVAL_ITERATION = "IntervalIteration"
    SEQUENTIAL_INTERVAL_ITERATION = "SequentialIntervalIteration"
    SOUND_VALUE_ITERATION = "SoundValueIteration"
    OPTIMISTIC_VALUE_ITERATION = "OptimisticValueIteration"
    LINEAR_PROGRAMMING = "LinearProgramming"
    SYMBLICIT_STATE_ELIMINATION = "SymblicitStateElimination"
    CONFIDENCE_INTERVAL = "ConfidenceInterval"
    APMC = "APMC"
    ADAPTIVE = "Adaptive"
    GENERAL_LABELED_REAL_TIME_DYNAMIC_PROGRAMMING = "GeneralLabeledRealTimeDynamicProgramming"


