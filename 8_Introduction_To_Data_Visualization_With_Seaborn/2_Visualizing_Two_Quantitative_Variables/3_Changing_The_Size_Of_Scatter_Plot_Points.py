# Changing the size of scatter plot points

# Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis.
# Vary the size of the points by the number of cylinders in the car ("cylinders").
sns.relplot(data=mpg, x='horsepower', y='mpg', kind='scatter', size='cylinders')    # mpg is dataframe, 'mpg' is column

# Show plot
plt.show()

# To make this plot easier to read, use hue to vary the color of the points by
# the number of cylinders in the car ("cylinders").
sns.relplot(data=mpg, x='horsepower', y='mpg', kind='scatter', size='cylinders', hue='cylinders')