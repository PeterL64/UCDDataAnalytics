# Facetting Multiple Regressions

# lmplot() allows us to facet the data across multiple rows and columns.
# In the previous plot, the multiple lines were difficult to read in one plot.
# We can try creating multiple plots by Region to see if that is a more useful visualization.

# Use lmplot() to look at the relationship between insurance_losses and premiums.
# Create a plot for each Region of the country.
# Display the plots across multiple rows.
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Display the plots across multiple columns instead of rows.
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           col="Region")
