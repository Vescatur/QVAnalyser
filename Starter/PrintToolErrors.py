from Library.Plots.results_printer import ResultsPrinter
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()
ResultsPrinter().print_tool_errors(benchmark)