from Library.Tools.result_parser import ResultParser
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()
ResultParser(benchmark)
storage.save_result_benchmark(benchmark)