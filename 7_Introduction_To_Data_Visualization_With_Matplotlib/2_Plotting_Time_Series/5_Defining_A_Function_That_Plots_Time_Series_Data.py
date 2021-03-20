# Defining a function that plots time-series data

import matplotlib.pyplot as plt

# Define a function called plot_timeseries that takes as input an Axes object (axes), data (x,y),
# a string with the name of a color and strings for x- and y-axis labels.
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

# Plot y as a function of in the color provided as the input color.
    axes.plot(x, y, color=color)

# Set the x- and y-axis labels using the provided input xlabel and ylabel,
# setting the y-axis label color using color.
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)

# Set the y-axis tick parameters using the tick_params method of the Axes object,
# setting the colors key-word to color.
    axes.tick_params('y', colors=color)


# Code all in one go:
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
  axes.plot(x, y, color=color)
  axes.set_xlabel(xlabel)
  axes.set_ylabel(ylabel, color=color)
  axes.tick_params('y', colors=color)
  