# Point Plots with Subgroups

import matplotlib.pyplot as plt
import seaborn as sns

# Use sns.catplot() and the student_data DataFrame to create a point plot with relationship status ("romantic")
# on the x-axis and number of absences ("absences") on the y-axis.
# Create subgroups based on the school that they attend ("school")
sns.catplot(data=student_data, x='romantic', y='absences', kind='point', hue='school')

# Turn off the confidence intervals for the plot.
sns.catplot(data=student_data, x='romantic', y='absences', kind='point', hue='school', ci=None)

# Since there may be outliers of students with many absences, import the median function from numpy
# and display the median number of absences instead of the average.
from numpy import median
sns.catplot(data=student_data, x='romantic', y='absences', kind='point', hue='school', ci=None, estimator=median)
# In the estimator keyword argument, median above is numpy function median.

plt.show()