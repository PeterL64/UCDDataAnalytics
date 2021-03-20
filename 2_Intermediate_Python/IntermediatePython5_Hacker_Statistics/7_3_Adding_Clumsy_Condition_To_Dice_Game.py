# Adding a 0.1% chance of falling down which sends you back to step 0.


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)


all_walks = []
for i in range(250):
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

        # Implement clumsiness
        if np.random.rand() <= 0.001:   # rand() generates a number between 0 and 1. Whereas randint() generates
            step = 0                    # a number between two numberss you choose

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()