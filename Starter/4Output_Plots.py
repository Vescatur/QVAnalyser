from Library.setup_environment import Setup
from Specific.Output.Plot.plot_sprint_6 import PlotSprint6

Setup().setup_resource_folders()
plot = PlotSprint6()
plot.CreatePlots()

# select benchmark
# generate plots
# save plots to the save
