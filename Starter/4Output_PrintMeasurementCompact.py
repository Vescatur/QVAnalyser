from Specific.Output.compact_measurement_printer import CompactMeasurementPrinter
from Library.Results.measurements import Measurements
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()
measurements = [
                Measurements.STATES, Measurements.TRANSITIONS, Measurements.BRANCHES,
                Measurements.PROPERTY_OUTPUT,
                Measurements.WALL_TIME,
                # Measurements.PARSING_TIME,
                Measurements.STATE_SPACE_TIME,
                Measurements.BISIMULATION_TIME,
                Measurements.PROPERTY_TIME]
#MeasurementPrinter().print_measurements(benchmark, measurements,"Modest")
CompactMeasurementPrinter().print_measurements(benchmark, measurements, "Storm")
#MeasurementPrinter().print_measurements(benchmark, measurements,"Prism")

