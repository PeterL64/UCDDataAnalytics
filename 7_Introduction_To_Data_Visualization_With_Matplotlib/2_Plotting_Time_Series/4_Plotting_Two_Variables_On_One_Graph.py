# Plotting two variables on one graph

import matplotlib.pyplot as plt

# Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.
# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the carbon dioxide variable, co2, in blue using the Axes plot method.
ax.plot(climate_change.index, climate_change['co2'], color='blue')

# Use the Axes twinx method to create a twin Axes that shares the x-axis.
ax2 = ax.twinx()

# Plot the relative temperature variable, relative_temp, in the twin Axes using its plot method.
ax2.plot(climate_change.index, climate_change['relative_temp'], color='red')

plt.show()