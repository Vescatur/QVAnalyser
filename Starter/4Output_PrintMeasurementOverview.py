from Library.Results.measurements import Measurements
from Library.storage import Storage
from Specific.Output.overview_measurements_printer import OverviewMeasurementPrinter

storage = Storage()
benchmark = storage.load_latest_benchmark()
measurements = [
                Measurements.STATES,
                Measurements.TRANSITIONS,
                Measurements.BRANCHES,
                Measurements.PROPERTY_OUTPUT,
                Measurements.WALL_TIME,
                # Measurements.PARSING_TIME,
                Measurements.STATE_SPACE_TIME,
                Measurements.BISIMULATION_TIME,
                Measurements.PROPERTY_TIME
                ]
OverviewMeasurementPrinter().print_overview_measurements(benchmark, measurements)

