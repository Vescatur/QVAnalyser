from enum import Enum


class PrismEngineType(Enum):
    PTA = "pta"
    SPARSE_MATRICES = "sparse"
    EXPLICIT = "explicit"
    HYBRID = "hybrid"
    MT_BINARY_DECISION_DIAGRAM = "mtbdd"
    SIMULATOR = "simulator"
