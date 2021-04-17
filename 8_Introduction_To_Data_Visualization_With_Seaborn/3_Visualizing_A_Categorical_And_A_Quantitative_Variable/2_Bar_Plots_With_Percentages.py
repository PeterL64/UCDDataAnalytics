# Bar plots With Percentages

# Will use catplot() as it will be a categorical analysis.

import matplotlib.pyplot as plt
import seaborn as sns

# Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis
# and "Interested in Math" on the y-axis.
sns.catplot(data=survey_data, x='Gender', y='Interested in Math', kind='bar')

# Show plot
plt.show()