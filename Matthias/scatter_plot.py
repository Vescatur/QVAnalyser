import pandas as pd

from benchmarking_pmc.export.exporter import Exporter
from benchmarking_pmc.export.utility.csv_export import next_cell
from benchmarking_pmc.results.run_result import ErrorType


class ScatterPlotPgfplotExporter(Exporter):
    """
    Export scatter plot in pgfplot.
    """

    def __init__(self, result_info, *measures):
        Exporter.__init__(self, result_info, *measures)
        #self.tools = list()
        self.TO = self.result_info.general_config.timeout
        self.MO = self.TO*2
        self.Err = self.MO*2
        self.max = self.Err*2

    def export(self, path, *measures):
        df = self.data
        # Keep only dedicated runs
        #keep = df.index.get_level_values('tool').str.contains("dedicated|eigen|dd-elim")
        #df = df[keep]

        # Replace errors by corresponding values for scatter plot
        df.loc[df.time == ErrorType.TIMEOUT, 'time']=self.TO
        df.loc[df.time == ErrorType.MEMOUT, 'time']=self.MO
        df.loc[df.time == ErrorType.ERROR, 'time']=self.Err
        df.loc[df.time == ErrorType.NOT_SUPPORTED, 'time']=self.Err
        df.loc[df.time == ErrorType.NOT_AVAILABLE, 'time']=self.Err

        # Make 'tool' column header
        df = df.unstack('tool')

        # Set type of benchmark
        # (Select first column of 'run' and get model name from there)
        df['type'] = df['run'].iloc[:,0].apply(lambda run: run.benchmark.model_name())
        # Remove column 'run'
        df = df.drop('run', 1)

        # Merge column headers into one: 'toolname-measure'
        df.columns = ["{}-{}".format(measure, tool) if tool else measure for measure, tool in df.columns]

        # Remove semicolon from benchmark names to avoid problems
        df = df.rename(index=lambda s: s.replace(';', ''))

        # Write CSV file
        df.to_csv(path, sep=";")


    def write_latex(self, path, csv_path):
        # Write LaTeX file
        with open(path, "w") as f:
            f.write("\\begin{tikzpicture}\n")
            f.write("  \\begin{axis}[\n")
            f.write("    width=\\plotsize, height=\\plotsize, xmin=0.01, ymin=0.01, xmax={0}, ymax={0}, xmode=log, ymode=log,\n".format(self.max))
            f.write("    axis x line=bottom, axis y line=left,\n")
            f.write("    x label style={at={(axis description cs:0.5,\\xaxisappendix)},anchor=north},\n")
            f.write("    y label style={at={(axis description cs:\\yaxisappendix,0.5)},anchor=south},\n")
            f.write("    xlabel={}, ylabel={},\n".format(self.tools[0], self.tools[1]))
            f.write("    yticklabel style={font=\\tiny}, xticklabel style={rotate=290, anchor=west, font=\\tiny},\n")
            f.write("    xtick={1, 60, 600, 1800}, xticklabels={1, 60, 600, 1800},\n")
            f.write("    extra x ticks = {{{}, {}, {}}}, extra x tick labels = {{TO, MO, Err}}, extra x tick style = {{grid = major}},\n".format(self.TO, self.MO, self.Err))
            f.write("    ytick={1, 60, 600, 1800}, yticklabels={1, 60, 600, 1800},\n")
            f.write("    extra y ticks = {{{}, {}, {}}}, extra y tick labels = {{TO, MO, Err}}, extra y tick style = {{grid = major}},\n".format(self.TO, self.MO, self.Err))
            f.write("    legend pos=south east, legend style={font=\\tiny}]\n")
            f.write("  \\addplot[\n")
            f.write("    scatter,only marks,\n")
            f.write("    scatter/classes={\n")
            f.write("      dtmcs={mark=square*,blue,mark size=1.30},\n")
            f.write("      mdps={mark=triangle*,red,mark size=1.30},\n")
            f.write("      ctmcs={mark=*,brown, mark size=1.30}\n")
            f.write("      %ma={mark=diamond*,purple, mark size=1.30}\n")
            f.write("      %more1={mark=+,black, mark size=1.30},\n")
            f.write("      %more2={mark=star,gray, mark size=1.30}\n")
            f.write("    },\n")
            f.write("    scatter src=explicit symbolic]\n")
            f.write("    table [col sep=semicolon, x=time-{}, y=time-{}, meta=type]\n".format(self.tools[0], self.tools[1]))
            f.write("    {" + csv_path + "};\n")
            f.write("  \\legend{DTMC,MDP,CTMC} %MA,MORE1,MORE2\n")
            # Diagonal lines indicating one order of magnitude
            f.write("  \\addplot[no marks] coordinates\n")
            f.write("    {(0.01,0.01) (1800,1800) };\n")
            f.write("  \\addplot[no marks, dashed] coordinates\n")
            f.write("    {(0.01,0.1) (180,1800) };\n")
            f.write("  \\addplot[no marks, dashed] coordinates\n")
            f.write("    {(0.01,1) (18,1800) };\n")
            f.write("  \\end{axis}\n")
            f.write("\\end{tikzpicture}\n")
