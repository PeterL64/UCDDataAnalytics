# Visualising the distribution of a series of Heads or Tails coin tosses
# Trying to plot the all the tails results

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails = []
for x in range(10000):  # Running the simulation 10000 times
    tails = [0]
    for x in range(10): # Running the coin toss 10 times
        coin = np.random.randint(0, 2)  # Running one coin toss
        tails.append(tails[x] + coin)   # Adding the results of coin to the tails list
    final_tails.append(tails[-1])   # Adding the tails list to the final tails list
plt.hist(final_tails, bins=10)      # Creating a histogram with 10 bins of data
plt.show()                          # Visualizing the plot
