# Hue and Scatter Plots

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using
# the DataFrame student_data. Color the plot points based on "location" (urban vs. rural).
sns.scatterplot(x='absences', y='G3', data=student_data, hue='location', hue_order=['Rural','Urban'])

# Show plot
plt.show()