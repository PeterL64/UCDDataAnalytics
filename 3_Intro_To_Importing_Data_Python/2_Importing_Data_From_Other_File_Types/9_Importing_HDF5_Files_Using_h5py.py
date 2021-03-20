# Importing HDF5 Files using h5py

# Import packages
import numpy as np
import h5py

# Assign filename to the variable: file
file = 'LIGO_data.hdf5' # name of the file used

# Load the file as read only into the variable: data
data = h5py.File(file, 'r') # 'r' is read-only

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file (Print the names of the groups in the HDF5 file
for key in data['meta'].keys(): # iterate over data.keys()
    print(key)
