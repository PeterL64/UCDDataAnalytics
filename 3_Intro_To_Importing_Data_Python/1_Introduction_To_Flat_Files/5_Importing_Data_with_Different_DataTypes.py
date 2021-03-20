# Importing data with more than one Type of Data
# The data in this file contains both floats and strings.
# The headers are strings and the rest of the rows are floats.
# Two ways to import the data, one is to set the data type argument, dtype, to strings, dtype = str
# The second way is to skip the first row, i.e. the Headers row and import the data as floats, dtype = float


# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
