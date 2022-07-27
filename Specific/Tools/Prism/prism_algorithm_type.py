from enum import Enum


class PrismAlgorithmType(Enum):
    #DTMC CTMC MDP
    VALUE_ITERATION = "value iteration"
    GAUSS_SEIDEL = "Gauss-Seidel"

    #DTMC CTMC
    JACOBI = "Jacobi"
    BACKWARDS_GAUSS_SEIDEL = "backwards Gauss-Seidel"
    PSEUDO_GAUSS_SEIDEL = "pseudo Gauss-Seidel"
    BACKWARDS_PSEUDO_GAUSS_SEIDEL = "backwards pseudo Gauss-Seidel"
    JACOBI_WITH_OVER_RELAXATION = "Jacobi with over-relaxation"
    SUCCESSIVE_OVER_RELAXATION = "successive over-relaxation"
    BACKWARDS_SUCCESSIVE_OVER_RELAXATION = "backwards successive over-relaxation"
    PSEUDO_SUCCESSIVE_OVER_RELAXATION = "pseudo successive over-relaxation"
    BACKWARDS_PSEUDO_SUCCESSIVE_OVER_RELAXATION = "backwards pseudo successive over-relaxation"

    #MDP
    POLICY_ITERATION = "policy iteration"
    MODIFIED_POLICY_ITERATION = "modified policy iteration"

    #PTA
    STOCHASTIC_GAMES = "stochastic games"
    DIGITAL_CLOCKS = "digital clocks"
    BACKWARDS_REACHABILITY = "backwards reachability"

    #SIMULATOR DTMC CTMC
    CONFIDENCE_INTERVAL = "confidence interval"
    ASYMPTOTIC_CONFIDENCE_INTERVAL = "asymptotic confidence interval"
    APPROXIMATE_PROBABILISTIC_MODEL_CHECKING = "approximate probabilistic model checking"
