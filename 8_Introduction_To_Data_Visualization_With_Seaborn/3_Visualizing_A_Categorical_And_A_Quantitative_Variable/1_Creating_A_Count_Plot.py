# Count Plots

# catplot() stands for Categorical Plot

import matplotlib.pyplot as plt
import seaborn as sns

# Use sns.catplot() to create a count plot using the survey_data DataFrame with "Internet usage" on the x-axis.
sns.catplot(data=survey_data, x='Internet usage', kind='count')

plt.show()

# Make the bars horizontal instead of vertical.
sns.catplot(data=survey_data, y='Internet usage', kind='count')

# Create column subplots based on "Age Category", which separates respondents into those that
# are younger than 21 vs. 21 and older.
sns.catplot(data=survey_data, y='Internet usage', kind='count', col='Age Category')

plt.show()