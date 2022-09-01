from Library.Output.matrix_wins import MatrixWins
from Library.Output.results_printer import ResultsPrinter
from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()
MatrixWins(benchmark)