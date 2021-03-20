# Simulating a dice roll

# Import numpy and set seed
import numpy as np
np.random.seed(123) # Seed is a random number I picked, it can be any number.

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again to see if the results are the same
print(np.random.randint(1,7))