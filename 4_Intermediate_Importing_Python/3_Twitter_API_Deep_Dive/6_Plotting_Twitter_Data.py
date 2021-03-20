# Plotting Twitter Data

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot the bar chart.
# The first argument of sns.barplot should be the list of labels to appear
# on the x-axis (created in the previous step).
# The second argument should be a list of the variables you wish to plot,
# as produced in the previous exercise (i.e. a list containing clinton, trump, etc).
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
