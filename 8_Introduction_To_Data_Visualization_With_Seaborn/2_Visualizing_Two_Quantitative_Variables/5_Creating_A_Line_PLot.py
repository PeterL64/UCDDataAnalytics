# Creating A Line Plot

import matplotlib.pyplot as plt
import seaborn as sns

# Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.
sns.relplot(data=mpg,  x='model_year', y='mpg', kind='line')


# Show plot
plt.show()