from Library.storage import Storage
from Specific.Output.matrices_sprint_6 import MatrixSprint6
from Specific.Output.statistics_sprint_6 import StatisticsSprint6

storage = Storage()
benchmark = storage.load_latest_benchmark()
StatisticsSprint6(benchmark)