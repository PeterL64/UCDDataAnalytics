# Customizing bar plots

import matplotlib.pyplot as plt
import seaborn as sns

# Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis,
# using the student_data DataFrame.
sns.catplot(x='study_time', y='G3', data=student_data, kind='bar')

# Using the order parameter, rearrange the categories so that they are in order from lowest study time to highest.
sns.catplot(x='study_time', y='G3', data=student_data, \
            kind='bar', order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"])

# Update the plot so that it no longer displays confidence intervals.
sns.catplot(x='study_time', y='G3', data=student_data, kind='bar',\
            order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"], ci=None)

plt.show()