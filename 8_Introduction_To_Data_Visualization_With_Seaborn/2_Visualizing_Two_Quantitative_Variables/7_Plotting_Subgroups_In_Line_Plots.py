# Plotting subgroups in line plots

import matplotlib.pyplot as plt
import seaborn as sns

# Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis
# and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
sns.relplot(data=mpg, x='model_year', y='horsepower', kind='line', ci=None)

# Create different lines for each country of origin ("origin") that vary in both line style and color.
sns.relplot(data=mpg, x='model_year', y='horsepower', kind='line', ci=None, style='country_origin', hue='country_origin')

# Add markers for each data point to the lines.
# Use the dashes parameter to use solid lines for all countries, while still allowing
# for different marker styles for each line.
sns.relplot(data=mpg, x='model_year', y='horsepower', kind='line',
            ci=None, style='country_origin', hue='country_origin', markers=True, dashes=False)

plt.show()
