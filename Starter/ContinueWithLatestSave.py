from Library.storage import Storage

storage = Storage()
benchmark = storage.load_latest_benchmark()
benchmark.continue_run()


# select benchmark
# generate plots
# save plots to the save
