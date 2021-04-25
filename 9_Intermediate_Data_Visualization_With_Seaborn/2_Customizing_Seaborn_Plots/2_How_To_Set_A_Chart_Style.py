# How to use a Style/Background
# Comparing two Styles

# Create a distplot() of the fmr_2 column in df using a dark style. Use plt.clf() to clear the figure.
sns.set_style('dark')
sns.distplot(df['fmr_2'])
plt.show()
plt.clf()

# Create the same distplot() of fmr_2 using a whitegrid style. Clear the plot after showing it.
sns.set_style('whitegrid')
sns.distplot(df['fmr_2'])
plt.show()
plt.clf()