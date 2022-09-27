from Library.storage import Storage
from Specific.Output.overview_measurements import OverviewMeasurements

storage = Storage()
benchmark = storage.load_latest_benchmark()
OverviewMeasurements().print_overview_measurements(benchmark)