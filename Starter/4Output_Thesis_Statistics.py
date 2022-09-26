from Library.storage import Storage
from Specific.Output.statistics_thesis import StatisticsThesis

storage = Storage()
benchmark = storage.load_latest_benchmark()
StatisticsThesis(benchmark)