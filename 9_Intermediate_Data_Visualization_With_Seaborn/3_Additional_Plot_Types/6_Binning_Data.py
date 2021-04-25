# Binning Data

# Create a regplot of Tuition and UG and set the fit_reg parameter to False to disable the regression line.
sns.regplot(data=df, y='Tuition', x="UG", fit_reg=False)

plt.show()
plt.clf()

# Create another plot with the UG data divided into 5 bins.
sns.regplot(data=df, y='Tuition', x="UG", x_bins=5)

plt.show()
plt.clf()

# Create a regplot() with the data divided into 8 bins.
sns.regplot(data=df, y='Tuition', x="UG", x_bins=8)

plt.show()
plt.clf()
