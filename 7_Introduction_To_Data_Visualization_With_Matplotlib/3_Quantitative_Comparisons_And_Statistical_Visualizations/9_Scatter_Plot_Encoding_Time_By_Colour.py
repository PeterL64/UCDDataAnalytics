# Scatter Plot Encoding Time by Color

import matplotlib.pyplot as plt
fig, ax = plt.subplots()


# Using the ax.scatter method add a scatter plot of the "co2" column (x-axis) against
# the "relative_temp" column.
ax.scatter(climate_change['co2'], climate_change['relative_temp'], c = climate_change.index)

# Use the c key-word argument to pass in the index of the DataFrame as input to
# color each point according to its date.
ax.set_xlabel('CO2 (ppm)')

# Set the x-axis label to "CO2 (ppm)" and the y-axis label to "Relative temperature (C)".
ax.set_ylabel('Relative temperature (C)')

plt.show()