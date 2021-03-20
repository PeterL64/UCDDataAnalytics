# The Structure of .mat in Python

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Load and store the MATLAB file into the variable: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the keys of the MATLAB dictionary using the method .keys()
print(mat.keys())   # (To print the keys of a dictionary, d, execute the command print(d.keys())     )

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))  # (To print the datatype of a variable, x, execute the command print(type(x))    )

# Print the shape of the value corresponding to the key 'CYratioCyt', using the numpy function shape()
print(np.shape(mat['CYratioCyt']))  # Pass mat['CYratioCyt'] to np.shape()

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
