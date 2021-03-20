# Creating a Loop for a 1-D Numpy Array and a 2_D Numpy Array

# Import numpy as np
import numpy as np
np_height = np.array([1.73,1.68,1.71,1.89,1.79,1.70,1.82])
np_baseball = np.array([123.45,111.11,115.51,666.66,420.69,694.20,316.05])

# For loop over np_height
for height in np_height:
    print(str(height) + ' inches.')

# For loop over np_baseball
for x in np.nditer(np_baseball):    # np.nditer() is a Numpy function, used for 2D arrays. Pronounced N-D-Iter
    print(x)                        # The input is the array you want to iterate over.
