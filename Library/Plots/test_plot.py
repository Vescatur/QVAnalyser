from Library.Results.statistics import Statistics
from Library.storage import Storage
import matplotlib.pyplot as plt
import numpy as np




class TestPlot(object):

    def CreatePlots(self):
        storage = Storage()
        benchmark = storage.load_latest_benchmark()


        self.CreateScatterPlot(benchmark,Statistics.BRANCHES, Statistics.STATES)
        # number of errors per algorithm
        # number of timeouts
        # check if states, transitions and branches are always the same

        # scatter plot with states and transitions

        # plot for a haddad sequence with 4 time statistics.    Each statistic has a different colour
        #   timeouts and errors are not displayed
        # time should be between 0.1 and 600
        # x is number of states

        # plot all sequences
        #   Colour is dependent on algorithm, formal model, sequence
        # wall_time is used for time

        # plots are saved using an increasing number

        # I want the same setup were you can specify the plots in a piece of code.



        # plt.style.use(_mpl-gallery)

        # make data
        # x = np.linspace(0, 10, 100)
        # y = 4 + 2 * np.sin(2 * x)

        # plot
        # fig, ax = plt.subplots()

        # ax.plot(x, y, linewidth=2.0)

        # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        #       ylim=(0, 8), yticks=np.arange(1, 8))

    def CreateScatterPlot(self, benchmark, statisticX, statisticY):

        dataX = []
        dataY = []
        for benchmark_sequence in benchmark.benchmark_sequences:
            for benchmark_instance in benchmark_sequence.benchmark_instances:
                result = benchmark_instance.results[1]
                if not result.threw_error:
                    if statisticX in result.statistics and statisticY in result.statistics:
                        # print(str(result.statistics[statisticX]) + " "+ str(result.statistics[statisticY]))
                        dataX.append(result.statistics[statisticX])
                        dataY.append(result.statistics[statisticY])

        # s = [10, 20, 610, 11]

        # plt.show()

        plt.scatter(dataX, dataY, c="r", alpha=0.5)
        # plt.scatter(dataX, dataY,s=s , c="b", alpha=0.5)

        #plt.title(statistics)
        plt.ylabel("Number of transitions")
        plt.xlabel("Number of choices")
        #plt.grid(True)
        plt.yscale("log")
        plt.xscale("log")
        #plt.axis([1, 40000000 , 1,  40000000])
        #plt.axis([1, 1000, 1, 1000])
        plt.savefig("./../Resources/Plots/test_plot.png")

