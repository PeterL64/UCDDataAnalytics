# Plot a Histogram with Seaborn

# To create a quick histogram to get a quick overview, use the matplotlib hist function:
# df['Example'].plot.hist()


# Create a distplot, disable the kde and have 20 bins.
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display the plot
plt.show()

# Notes
# The distplot() function has many options for customisation and configuration.
# Eg: distplot(df['xyz'], hist=False, rug=True)

# The distplot() function can use several other functions including, kdeplot and rugplot.
# You can customise a plot further by passing arguments to the underlying function:
# sns.distplot(df['a'], hist=True/False, rug=True, kde_kws={'shade':True'})