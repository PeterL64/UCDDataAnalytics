# Finding Missing Values

# Using Sample DataFrame, avocados_2016, a subset of avocados that contains only sales from 2016.

import pandas as pd
import matplotlib.pyplot as plt

# Check individual values for missing values
# Print a DataFrame that shows whether each value in avocados_2016 is missing or not.
print(avocados_2016.isna())

# Check each column for missing values
# Print a summary that shows whether any value in each column is missing or not.
print(avocados_2016.isna().any())
# The .any() method will take a DataFrame of Booleans and flatten it to
# indicate if there are any True values in each column.

# Bar plot of missing values by variable
# Create a bar plot of the total number of missing values in each column.
avocados_2016.isna().sum().plot(kind='bar')
# The .sum() method can be used on a DataFrame of Booleans to count
# the number of True values in each column.

# Show plot
plt.show()