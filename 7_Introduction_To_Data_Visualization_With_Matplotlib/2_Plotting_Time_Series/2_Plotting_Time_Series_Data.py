# Plot time-series data

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the data from climate_change to the plot: use the DataFrame index for the x value and
# the "relative_temp" column for the y values.
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()