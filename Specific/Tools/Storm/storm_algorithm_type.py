from enum import Enum


class StormAlgorithmType(Enum):
    #DTMC CTMC
    JACOBI = "jacobi"
    GMM_PLUS_PLUS = "gmm++"
    GAUSS_SEIDEL = "Gauss-Seidel"
    SUCCESSIVE_OVER_RELAXATION = "successive over relaxation"
    WALKERCHAE = "walkerchae"
    EIGEN = "eigen"
    ELIMINATION = "elimination"
    ACYCLIC = "acyclic"

    #DTMC MDP CTMC MA
    VALUE_ITERATION = "value iteration"
    INTERVAL_ITERATION = "interval iteration"
    SOUND_VALUE_ITERATION = "sound value iteration"
    OPTIMISTIC_VALUE_ITERATION = "optimistic value iteration"
    RATIONAL_SEARCH = "rational search"


    #MDP MA
    POLICY_ITERATION = "policy iteration"
    LINEAR_PROGRAMMING = "linear programming"
    VALUE_ITERATION_TO_POLICY_ITERATION = "value iteration to policy iteration"

    #Extra engines
    EXPLORATION = "exploration"
    ABSTRACTION_REFINEMENT = "abstraction refinement"

