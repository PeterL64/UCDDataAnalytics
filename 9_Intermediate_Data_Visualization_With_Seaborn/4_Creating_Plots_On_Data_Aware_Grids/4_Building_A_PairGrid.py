# Building a PairGrid

# When exploring a dataset, one of the earliest tasks is exploring the relationship between pairs of variables.
# This step is normally a precursor to additional investigation.
# Seaborn supports this pair-wise analysis using the PairGrid.


# Compare "fatal_collisions" to "premiums" by using a scatter plot mapped to a PairGrid().
# Create a PairGrid with a scatter plot for fatal_collisions and premiums.
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map(plt.scatter)

plt.show()
plt.clf()


# Create another PairGrid but plot a histogram on the diagonal and scatter plot on the off diagonal.
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(plt.hist)
g3 = g2.map_offdiag(plt.scatter)

plt.show()
plt.clf()