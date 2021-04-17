# Creating and Customizing Point Plots

import matplotlib.pyplot as plt
import seaborn as sns

# Use sns.catplot() and the student_data DataFrame to create a point plot with "famrel" on the x-axis
# and number of absences ("absences") on the y-axis.
sns.catplot(x='famrel', y='absences', data= student_data, kind='point')
plt.show()

# Add "caps" to the end of the confidence intervals with size 0.2.
sns.catplot(x='famrel', y='absences', data= student_data, kind='point', capsize=0.2)
plt.show()

# Remove the lines joining the points in each category.
sns.catplot(x='famrel', y='absences', data= student_data, kind='point', capsize=0.2, join=False)
plt.show()
