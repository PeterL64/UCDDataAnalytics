# Visualizing the Climbing Stairs Random Walk Dice Game


# Import Numpy and set Seed
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100):
    step = random_walk[-1]          # Set step: last element in random_walk
    dice = np.random.randint(1,7)   # Roll the dice

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1) # Using x = max(0, x-1) makes sure we can't go below 0, which is ground floor.
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot random_walk graph
plt.plot(random_walk)

# Show the plot
plt.show()