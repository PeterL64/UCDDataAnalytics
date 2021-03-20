# Subsetting by row/column number

import pandas as pd

# Get 23rd row, 2nd column
print(temperatures.iloc[22:23, 1:2])

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:5,:])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5,2:4])