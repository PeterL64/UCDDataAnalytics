# Using a time index to zoom in

import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change['1970-01-01':'1979-12-31']

# Add the data from seventies to the plot: use the DataFrame index for
# the x value and the "co2" column for the y values.
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()