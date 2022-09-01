from Library.Output.results_printer import ResultsPrinter
from Library.Tools.benchmark_result_parser import BenchmarkResultParser
from Library.storage import Storage
from Specific.Tools.Modest.modest_tool import ModestTool
from Specific.Tools.Storm.storm_tool import StormTool

storage = Storage()
benchmark = storage.load_latest_benchmark()
ResultsPrinter().print_error_information_per_instance(benchmark)