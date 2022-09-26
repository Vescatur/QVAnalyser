from Library.storage import Storage
from Specific.Output.Matrix.matrices_thesis import MatrixThesis

storage = Storage()
benchmark = storage.load_latest_benchmark()
MatrixThesis(benchmark)