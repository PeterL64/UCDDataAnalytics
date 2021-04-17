# Create a Box Plot

import matplotlib.pyplot as plt
import seaborn as sns

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Use sns.catplot() and the student_data DataFrame to create a box plot with "study_time" on the x-axis
# and "G3" on the y-axis. Set the ordering of the categories to study_time_order.
sns.catplot(data=student_data, x='study_time', y='G3', kind='box', order= study_time_order)

plt.show()