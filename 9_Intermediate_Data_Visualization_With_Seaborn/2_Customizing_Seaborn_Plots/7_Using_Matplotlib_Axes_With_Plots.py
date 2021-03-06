# Using Matplotlib Axes

# Seaborn uses matplotlib as the underlying library for creating plots.
# Most of the time, you can use the Seaborn API to modify your visualizations but sometimes
# it is helpful to use matplotlib's functions to customize your plots.
# The most important object in this case is matplotlib's axes.

# Once you have an axes object, you can perform a lot of customization of your plot.

# Create a figure and axes
fig, ax = plt.subplots()

# Plot a distplot() of column fmr_3 on the axes.
sns.distplot(df['fmr_3'], ax=ax)

# Set a more useful label on the x axis of "3 Bedroom Fair Market Rent".
ax.set(xlabel="3 Bedroom Fair Market Rent")

# Show the plot
plt.show()
