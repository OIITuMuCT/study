from plotly.offline import plot

def generate_scatter_plot(x_axis, y_axis):
    """ Generate a scatter plot for the provided x and y-axis values. """
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=x_axis, y=y_axis)
    return plot(figure, output_type='div')

def generate_scatter_plot(x_axis, y_axis):
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=x_axis, y=y_axis)
    figure.add_trace(scatter)
    return plot(figure, output_type='div')

