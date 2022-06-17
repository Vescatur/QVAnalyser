import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

from benchmarking_pmc.export.exporter import Exporter


class CumulativeTimesPlotlyExporter(Exporter):
    """
    Export cumulative times to plotly webpage.
    """

    def __init__(self, result_info, *measures):
        Exporter.__init__(self, result_info, *measures)

    def export(self, path, *measures):
        df = self.data

        # Keep only specific data points
        #keep = df.index.get_level_values('tool').str.contains("dedicated|eigen|dd-elim")
        #df = df[keep]

        # Order according to tool instead of benchmark
        df = df.swaplevel('tool', 'benchmark').sort_index(0)
        # Convert times to numbers or NaN (for errors)
        df['time_num'] = pd.to_numeric(df['time'], errors='coerce')
        # Sort times in ascending order
        df = df.sort_values(['tool', 'time_num'])
        # Compute cumulative times for each tool
        df['cumulative_time'] = df.groupby('tool')['time_num'].transform(pd.Series.cumsum)

        # Prepare data per tool
        data = list()
        for name, group in df.groupby('tool'):
            data.append(go.Scatter(
                x=group.reset_index().index,  # set number of solved instance
                y=group['cumulative_time'],
                name=name,
                hoverlabel=dict(namelength=-1)
            ))

        # Set layout
        layout = dict(title='Cumulative solving times',
                      xaxis=dict(title='# Solved instances', autorange=True),
                      yaxis=dict(title='Time (s)', type='log', autorange=True),
                      hovermode="closest"
                      )

        # Plot graph
        fig = dict(data=data, layout=layout)
        plot(fig, filename=path, auto_open=False)


class CumulativeTimesPgfplotExporter(Exporter):
    """
    Export cumulative times to pgfplot.
    """

    def __init__(self, result_info, *measures):
        Exporter.__init__(self, result_info, *measures)
        self.tools = list()
        self.xmax = 0
        self.ymax = 0

    def export(self, path, *measures):
        df = self.data
        # Keep only dedicated runs or eigen or symbolic
        #keep = df.index.get_level_values('tool').str.contains("dedicated|eigen|dd-elim")
        #df = df[keep]

        # Order according to tool instead of benchmark
        df = df.swaplevel('tool', 'benchmark').sort_index(0)
        # Convert times to numbers or NaN (for errors)
        df['time_num'] = pd.to_numeric(df['time'], errors='coerce')
        # Sort times in ascending order
        df = df.sort_values(['tool', 'time_num'])
        # Compute cumulative times for each tool
        df['cumulative_time'] = df.groupby('tool')['time_num'].transform(pd.Series.cumsum)
        # Set nan to None again
        df = df.where((pd.notnull(df)), None)

        # Generate CSV file
        csv = pd.DataFrame()
        for name, group in df.groupby('tool'):
            times_list = group['cumulative_time'].to_list()
            csv[name] = times_list
            self.tools.append(name)
            # Find maximal values for x and y
            self.xmax = max(self.xmax, len(times_list))
            for val in reversed(times_list):
                if val is not None:
                    self.ymax = max(self.ymax, val)
                    break
        # Write CSV file
        csv.to_csv(path, index=True, index_label="no", sep=";")

    def write_latex(self, path, csv_path):
        # Write LaTeX file
        with open(path, "w") as f:
            f.write("\\begin{tikzpicture}\n")
            f.write("  \\begin{axis}[\n")
            f.write("    width=\\plotsize, height=\\plotsize, xmin=0, ymin=0.01, xmax={}, ymax={}, ymode=log,\n".format(self.xmax, self.ymax))
            f.write("    axis x line=bottom, axis y line=left,\n")
            f.write("    x label style={at={(axis description cs:0.5,\\xaxisappendix)},anchor=north},\n")
            f.write("    y label style={at={(axis description cs:\\yaxisappendix,0.5)},anchor=south},\n")
            f.write("    xlabel=No. benchmark, ylabel=Time (in seconds),\n")
            f.write("    yticklabel style={font=\\tiny}, xticklabel style={rotate=290, anchor=west, font=\\tiny},\n")
            f.write("    mark repeat={50},\n")
            f.write("    % initialize color scheme:\n")
            f.write("    cycle list/Set1,\n")
            f.write("    % combine it with ’mark list*’:\n")
            f.write("    cycle multiindex* list={\n")
            f.write("        mark list*\\nextlist\n")
            f.write("        Set1\\nextlist\n")
            f.write("    },\n")
            f.write("    legend pos=south east, legend style={font=\\tiny}]\n")
            for name in self.tools:
                f.write("      \\addplot\n")
                f.write("        table [col sep=semicolon, x=no, y={}]\n".format(name))
                f.write("        {" + csv_path + "};\n")
            f.write("      \\legend{" + ",".join(self.tools) + "}\n")
            f.write("  \\end{axis}\n")
            f.write("\\end{tikzpicture}\n")
