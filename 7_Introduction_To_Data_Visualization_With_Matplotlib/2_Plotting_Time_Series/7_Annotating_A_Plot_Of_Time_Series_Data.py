# Annotating a plot of time-series data


import matplotlib.pyplot as plt
import pandas as pd
fig, ax = plt.subplots()

# Use the ax.plot method to plot the DataFrame index against the relative_temp column.
ax.plot(climate_change.index, climate_change['relative_temp'])

# Use the annotate method to add the text '>1 degree' in the location (pd.Timestamp('2015-10-06'), 1).
ax.annotate('>1 degree', xy=[pd.Timestamp("2015-10-06"), 1])

# Show the plot
plt.show()