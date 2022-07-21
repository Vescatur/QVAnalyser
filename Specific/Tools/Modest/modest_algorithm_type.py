
from enum import Enum


class ModestAlgorithmType(Enum):
    ValueIteration = "ValueIteration"
    IntervalIteration = "IntervalIteration"
    SequentialIntervalIteration = "SequentialIntervalIteration"
    SoundValueIteration = "SoundValueIteration"
    OptimisticValueIteration = "OptimisticValueIteration"
    LinearProgramming = "LinearProgramming"
    SymblicitStateElimination = "SymblicitStateElimination"
    ConfidenceInterval = "ConfidenceInterval"
    APMC = "APMC"
    Adaptive = "Adaptive"
    GeneralLabeledRealTimeDynamicProgramming = "GeneralLabeledRealTimeDynamicProgramming"


