# Changing the Style of Scatter Plot Points

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration" on the x-axis and "mpg" on
# the y-axis. Vary the style and color of the plot points by country of origin ("origin").
sns.relplot(x='acceleration', y='mpg', data=mpg, kind='scatter', hue='origin', style='origin')
