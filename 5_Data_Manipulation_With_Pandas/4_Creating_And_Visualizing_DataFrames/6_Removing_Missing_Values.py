# Removing Missing Values

import pandas as pd
import matplotlib.pyplot as plt

# Remove the rows of avocados_2016 (DataFrame) that contain missing values and store
# the remaining rows in avocados_complete.
avocados_complete = avocados_2016.dropna()

# Verify that all missing values have been removed from avocados_complete. (Check is any cols contain missing values)
# Calculate each column that has NAs and print.
print(avocados_complete.isna().any().sum())
