from Library.Results.measurements import Measurements
from Library.storage import Storage
from Specific.Output.statistics import StatisticsSprint6

storage = Storage()
benchmark = storage.load_latest_benchmark()
#StatisticsSprint6(benchmark,Measurements.STATE_SPACE_TIME)
StatisticsSprint6(benchmark,Measurements.PROPERTY_TIME)
#StatisticsSprint6(benchmark,Measurements.WALL_TIME)