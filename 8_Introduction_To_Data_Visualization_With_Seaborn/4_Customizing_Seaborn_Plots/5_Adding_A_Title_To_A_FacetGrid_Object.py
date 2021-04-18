# Adding a title to a FacetGrid object


# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle('Car Weight vs. Horsepower')
# You can use the y parameter to adjust the height of the title, as it is usually set quite low.
# g.fig.suptitle('New Title', y=1.03)'  It is set at 1 by default.

# Show plot
plt.show()
