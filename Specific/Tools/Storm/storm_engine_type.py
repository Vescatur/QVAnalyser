from enum import Enum


class StormEngineType(Enum):
    DECISION_DIAGRAM = "decision diagram"
    SPARSE_MATRICES = "sparse matrices"
    DECISION_DIAGRAM_TO_SPARSE_MATRICES = "decision diagram to sparse matrices"
    HYBRID = "hybrid"
    EXPLORATION = "exploration"
    ABSTRACTION_REFINEMENT = "abstraction refinement"
