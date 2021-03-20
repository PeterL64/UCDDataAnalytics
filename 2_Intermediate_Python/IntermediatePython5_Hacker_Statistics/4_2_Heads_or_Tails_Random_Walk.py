# Heads or Tails: Random Walk
# I will track the total number of tails while simulating a heads or tails game.

import numpy as np  # importing the numpy package as np for short
np.random.seed(123)
tails = [0]         # Start be creating a list with no tails in it, since no dice has yet been thrown.
for i in range(10): # We want to throw it 10 times.
    coin = np.random.randint(0,2)   # Generating a random number 0 or 1, i.e. heads or tails.
    tails.append(tails[i] + coin)   # If coin is 0, it is heads, so adding it to the list makes no change.
                                    # If coin is 1, it is tails, so adding it does change the list which is what we
                                    # want to count, the number or tails.
print(tails)

# Output: [0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3]
# The Output created a list which tells you how many tails there have been after each roll.
