# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter = '\t', skiprows = 1, usecols = [0,2])
# The delimiter '\t' means the data is delimited by tabs.
# skiprows = 1 skips one row. You write it like this and not a 0 because you are skipping 1 row, not tge first row
# usecols = [0, 2] Is using columns 1 and 3. They are in square brackets because it is a list of columns to use.

# Print data
print(data)