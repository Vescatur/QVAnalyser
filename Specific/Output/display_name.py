
algorithm_to_display_name_array = {}


algorithm_to_display_name_array["modest apmc"] = "M modes APMC"
algorithm_to_display_name_array["modest adaptive"] = "M modes adaptive"
algorithm_to_display_name_array["modest confidence interval"] = "M modes CI"
algorithm_to_display_name_array["modest glrtdp"] = "M GLRTDP"

algorithm_to_display_name_array["modest interval iteration"] = "M mcsta II"
algorithm_to_display_name_array["modest sequential interval iteration"] = "M mcsta SII"
algorithm_to_display_name_array["modest sound value iteration"] = "M mcsta SVI"
algorithm_to_display_name_array["modest optimistic value iteration"] = "M mcsta OVI"
algorithm_to_display_name_array["modest linear programming"] = "M mcsta LP"

algorithm_to_display_name_array["Prism confidence interval simulator"] = "P simulator CI"
algorithm_to_display_name_array["Prism asymptotic confidence interval simulator"] = "P simulator ACI"
algorithm_to_display_name_array["Prism approximate probabilistic model checking simulator"] = "P simulator APMC"

algorithm_to_display_name_array["Prism Jacobi explicit"] = "P explicit GS"
algorithm_to_display_name_array["Prism Gauss-Seidel explicit"] = "P explicit back GS"
algorithm_to_display_name_array["Prism backwards Gauss-Seidel explicit"] = "P explicit SOR"
algorithm_to_display_name_array["Prism Jacobi with over-relaxation explicit"] = "P explicit back SOR"
algorithm_to_display_name_array["Prism successive over-relaxation explicit"] = "P explicit J"
algorithm_to_display_name_array["Prism backwards successive over-relaxation explicit"] = "P explicit JOR"
algorithm_to_display_name_array["Prism policy iteration explicit"] = "P explicit PI"
algorithm_to_display_name_array["Prism modified policy iteration explicit"] = "P explicit MPI"

algorithm_to_display_name_array["Prism stochastic games pta"] = "P stochastic games"
algorithm_to_display_name_array["Prism digital clocks pta"] = "P digital clocks"
algorithm_to_display_name_array["Prism backwards reachability pta"] = "P back reachability"

algorithm_to_display_name_array["Storm abstraction refinement abstraction refinement"] = "S abs "
algorithm_to_display_name_array["Storm gmm++ sparse matrices"] = "S sparse gmm++"
algorithm_to_display_name_array["Storm jacobi sparse matrices"] = "S sparse J"
algorithm_to_display_name_array["Storm Gauss-Seidel sparse matrices"] = "S sparse GS"
algorithm_to_display_name_array["Storm successive over relaxation sparse matrices"] = "S sparse SOR"
algorithm_to_display_name_array["Storm walkerchae sparse matrices"] = "S sparse walkerchae"
algorithm_to_display_name_array["Storm sound value iteration sparse matrices"] = "S sparse SVI"
algorithm_to_display_name_array["Storm optimistic value iteration sparse matrices"] = "S sparse OVI"
algorithm_to_display_name_array["Storm interval iteration sparse matrices"] = "S sparse II"
algorithm_to_display_name_array["Storm rational search sparse matrices"] = "S sparse rational"
algorithm_to_display_name_array["Storm eigen sparse matrices"] = "S sparse eigen"
algorithm_to_display_name_array["Storm elimination sparse matrices"] = "S sparse elimination"
algorithm_to_display_name_array["Storm policy iteration sparse matrices"] = "S sparse PI"
algorithm_to_display_name_array["Storm value iteration to policy iteration sparse matrices"] = "S sparse VI to PI"
algorithm_to_display_name_array["Storm linear programming sparse matrices"] = "S sparse LP"




algorithm_to_display_name_array["Storm value iteration sparse matrices"] = "S sparse VI"
algorithm_to_display_name_array["Storm value iteration decision diagram to sparse matrices"] = "S dd to sparse VI"
algorithm_to_display_name_array["Storm value iteration hybrid"] = "S hybrid VI"
algorithm_to_display_name_array["Storm value iteration decision diagram"] = "S dd VI"

algorithm_to_display_name_array["Storm topological value iteration sparse matrices"] = "S sparse TVI"
algorithm_to_display_name_array["Storm topological value iteration decision diagram to sparse matrices"] = "S dd to sparse TVI"
algorithm_to_display_name_array["Storm topological value iteration hybrid"] = "S hybrid TVI"

algorithm_to_display_name_array["Storm bisimulation value iteration sparse matrices"] = "S sparse bis VI"
algorithm_to_display_name_array["Storm bisimulation value iteration decision diagram to sparse matrices"] = "S dd to sparse bis VI"
algorithm_to_display_name_array["Storm bisimulation value iteration hybrid"] = "S hybrid bis VI"
algorithm_to_display_name_array["Storm bisimulation value iteration decision diagram"] = "S dd bis VI"

algorithm_to_display_name_array["Storm topological bisimulation value iteration sparse matrices"] = "S sparse bis TVI"
algorithm_to_display_name_array["Storm topological bisimulation value iteration decision diagram to sparse matrices"] = "S dd to sparse bis TVI"
algorithm_to_display_name_array["Storm topological bisimulation value iteration hybrid"] = "S hybrid bis TVI"

algorithm_to_display_name_array["Prism value iteration sparse"] = "P sparse VI"
algorithm_to_display_name_array["Prism value iteration explicit"] = "P explicit VI"
algorithm_to_display_name_array["Prism value iteration hybrid"] = "P hybrid VI"
algorithm_to_display_name_array["Prism value iteration mtbdd"] = "P mtbdd VI"
algorithm_to_display_name_array["Prism topological value iteration sparse"] = "P sparse TVI"
algorithm_to_display_name_array["Prism topological value iteration explicit"] = "P explicit TVI"
algorithm_to_display_name_array["Prism topological value iteration hybrid"] = "P hybrid TVI"
algorithm_to_display_name_array["Prism topological value iteration mtbdd"] = "P mtbdd TVI"

algorithm_to_display_name_array["modest value iteration"] = "M mcsta VI"



def algorithm_name_to_display_name(algorithm_name):
    return algorithm_to_display_name_array[algorithm_name]