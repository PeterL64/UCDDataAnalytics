# Regression and Residual Plots

# Linear regression is a useful tool for understanding the relationship between numerical variables.
# Seaborn has simple but powerful tools for examining these relationships.

# Plot a regression plot comparing Tuition and average SAT scores(SAT_AVG_ALL).
# Make sure the values are shown as green triangles.
sns.regplot(data=df, y='Tuition', x="SAT_AVG_ALL", marker='^', color='g')

plt.show()
plt.clf()

# Use a residual plot to determine if the relationship looks linear.
sns.residplot(data=df, y='Tuition', x="SAT_AVG_ALL", color='g')

plt.show()
plt.clf()