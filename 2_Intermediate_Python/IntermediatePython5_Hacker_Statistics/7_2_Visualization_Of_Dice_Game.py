# Visualizing All Walks Dice Game

# all_walks is a list of lists, so I need to convert it to a numpy array to create better plots.

# Import numpy and matplotlib and set seed.
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# initialize and populate all_walks
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()          # This shows the plot isn't very useful

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)   # Now every row in np_aw represents the position after 1 throw for
                                # the 10 random walks
# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()