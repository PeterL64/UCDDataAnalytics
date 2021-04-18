# FacetGrids vs. AxesSubplot

# Seaborn plots create two different types of objects: FacetGrid and AxesSubplot.
# To figure out which it is, you first need to assign the plot output to a variable, typically g, (as seen below).
# Then find the type of the variable: type(g)

# A FacetGrid consists of one or more AxesSublpots, which is how it supports subplots.

# Object type       Plot Types                              Characteristics
# FacetGrid         relplot() and catplot()                 both support making subplots.
# AxesSubplot       scatterplot() and countplot(), etc.     only creates a single plot.

# Identify what type of object plot g is and assign it to the variable type_of_g.
# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)