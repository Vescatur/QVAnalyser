from Library.storage import Storage
from Specific.Output.Clustering.similarity_clustering_thesis import SimilarityClusteringThesis

storage = Storage()
benchmark = storage.load_latest_benchmark()
SimilarityClusteringThesis(benchmark)