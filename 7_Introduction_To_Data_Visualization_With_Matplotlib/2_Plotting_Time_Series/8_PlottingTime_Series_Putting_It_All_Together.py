# Plotting time-series: putting it all together



# Will be using the function I previously defined: plot_timeseries(axes, x, y, color, xlabel, ylabel)

import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

# Use the plot_timeseries function to plot CO2 levels against time.
# Set xlabel to "Time (years)" ylabel to "CO2 levels" and color to 'blue'.
plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time (years)', 'CO2 levels')

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# In ax2, plot temperature against time, setting the color ylabel
# to "Relative temp (Celsius)" and color to 'red'.
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', 'Time (years)', 'Relative temp (Celsius)')

# Annotate the data using the ax2.annotate method. Place the text ">1 degree" in
# x=pd.Timestamp('2008-10-06'),y=-0.2 pointing with a gray thin arrow
# to x=pd.Timestamp('2015-10-06'), y = 1.
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'),1), xytext=(pd.Timestamp('2008-10-06 00:00:00'), -0.2), arrowprops={'arrowstyle':'->','color':'gray'})

# Show the plot
plt.show()