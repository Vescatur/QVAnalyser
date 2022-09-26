from Library.storage import Storage
from Specific.Output.results_printer import ResultsPrinter

storage = Storage()
benchmark = storage.load_latest_benchmark()
ResultsPrinter().print_error_information_per_algorithm(benchmark)