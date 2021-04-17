# Omitting Outliers in Box Plots

import matplotlib.pyplot as plt
import seaborn as sns

# Use sns.catplot() to create a box plot with the student_data DataFrame, putting "internet" on the x-axis and "G3" on the y-axis.
# Add subgroups so each box plot is colored based on "location".
# Do not display the outliers.
sns.catplot(data=student_data, x='internet', y='G3', kind='box', col='location', hue='location', sym='')

# Show plot
plt.show()