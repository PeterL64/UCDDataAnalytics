# Regression Plot Parameters

# Plot a regression plot of Tuition and PCTPELL.
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL")

plt.show()
plt.clf()

# Create another plot that breaks the PCTPELL column into 5 different bins.
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)

plt.show()
plt.clf()

# Create a final regression plot that includes a 2nd order polynomial regression line.
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5,
            order=2)

plt.show()
plt.clf()