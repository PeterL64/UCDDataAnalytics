# Building a JointGrid and JointPlot

# Seaborn's JointGrid combines univariate plots such as histograms, rug plots and kde plots with bivariate plots
# such as scatter and regression plots. The process for creating these plots should be familiar to you now.
# These plots also demonstrate how Seaborn provides convenient functions to combine multiple plots together.

# Use Seaborn's "whitegrid" style for these plots.
sns.set_style("whitegrid")

# Create a JointGrid() with "hum" on the x-axis and "total_rentals" on the y.
g = sns.JointGrid(x="hum",
            y="total_rentals",
            data=df,
            xlim=(0.1, 1.0))

# Plot a regplot() and distplot() on the margins.
g.plot(sns.regplot, sns.distplot)

plt.show()
plt.clf()


# Re-create the plot using a jointplot()
sns.jointplot(x="hum",
        y="total_rentals",
        kind='reg',
        data=df)

plt.show()
plt.clf()

# For Comparison
# sns.set_style("whitegrid")
# g = sns.JointGrid(x="hum",
#             y="total_rentals",
#             data=df,
#             xlim=(0.1, 1.0))
#
# g.plot(sns.regplot, sns.distplot)
#
# plt.show()
# plt.clf()