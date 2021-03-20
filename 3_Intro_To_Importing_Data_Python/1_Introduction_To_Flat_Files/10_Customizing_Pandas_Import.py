# Importing a slightly corrupted file using Pandas

# Pandas will deal with most of the issues while importing data as a data scientist.
# Some issues are comments occurring in flat files, empty lines and missing values, often referred to as NA or NaN


# Import matplotlib.pyplot as plt, pandas as pd, numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')
# sep is the pandas version of delimiter
# comment takes characters that comments occur after the file
# na_values takes a list of strings to recognize as NA/NaN, in this case 'Nothing'

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()