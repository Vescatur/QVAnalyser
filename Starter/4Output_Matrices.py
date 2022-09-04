from Library.storage import Storage
from Specific.Output.matrices_sprint_6 import MatrixSprint6

storage = Storage()
benchmark = storage.load_latest_benchmark()
MatrixSprint6(benchmark)