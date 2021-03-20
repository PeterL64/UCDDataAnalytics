# Using a plotting function


# In previous exercise I defined a function called plot_timeseries:
#   -   plot_timeseries(axes, x, y, color, xlabel, ylabel)    -
# that takes an Axes object (as the argument axes), time-series data (as x and y arguments)
# the name of a color (as a string, provided as the color argument)
# and x-axis and y-axis labels (as xlabel and ylabel arguments).


import matplotlib.pyplot as plt

# In the provided ax object, use the function plot_timeseries to plot the "co2" column in blue,
# with the x-axis label "Time (years)" and y-axis label "CO2 levels".
plot_timeseries(ax,climate_change.index, climate_change['co2'], "blue", 'Time (years)', 'CO2 levels')

# Use the ax.twinx method to add an Axes object to the figure that shares the x-axis with ax.
ax2 = ax.twinx()

# Use the function plot_timeseries to add the data in the "relative_temp" column in red
# to the twin Axes object,with the x-axis label "Time (years)" and
# y-axis label "Relative temperature (Celsius)".
plot_timeseries(ax, climate_change.index, climate_change['relative_temp'], "red", 'Time (years)', 'Relative temperature (Celsius)')

plt.show()
