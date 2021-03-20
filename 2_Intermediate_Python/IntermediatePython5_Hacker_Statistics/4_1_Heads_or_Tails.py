# Creating a list of outcomes for Heads or Tails

import numpy as np

np.random.seed(123)

outcomes = []  # Here I created an open list to be updated as the coin tosses progress
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')

print(outcomes)
