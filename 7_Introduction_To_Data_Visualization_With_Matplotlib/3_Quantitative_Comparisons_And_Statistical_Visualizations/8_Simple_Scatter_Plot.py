# Simple Scatter Plot

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Using the ax.scatter method, add the data to the plot: "co2" on the x-axis
# and "relative_temp" on the y-axis.
ax.scatter(climate_change['co2'], climate_change['relative_temp'])

# Set the x-axis label to "CO2 (ppm)".
ax.set_xlabel('CO2 (ppm)')

# Set the y-axis label to "Relative temperature (C)".
ax.set_ylabel('Relative temperature (Celsius)')
plt.show()