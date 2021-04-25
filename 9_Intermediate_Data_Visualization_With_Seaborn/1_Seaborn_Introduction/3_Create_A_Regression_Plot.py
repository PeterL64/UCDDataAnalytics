# Create a Regression Plot
# Here, we will look at the difference between the regression plotting functions.

# The regplot() function generates a scatter plot with a regression line.
# Usage is similar to the distplot
# The 'data' and 'x' and 'y' variables must be defined.
# Eg: sns.regplot(x='alcohol', y='pH', data=df)

# Create a regression plot of 'premiums' vs. 'insurance_losses'
# Create a regression plot using regplot() with "insurance_losses" on the x axis and "premiums" on the y axis.
sns.regplot(x='insurance_losses', y='premiums', data=df)

# Display the plot
plt.show()


# Create a regression plot of "premiums" versus "insurance_losses" using lmplot().
sns.lmplot(x='insurance_losses', y='premiums', data=df)

# Display the second plot
plt.show()