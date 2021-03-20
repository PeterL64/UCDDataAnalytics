# Dice Game

# You are climbing stairs dependent on the roll of a dice.
# Roll a 1 or a 2, you take a step down.
# Roll a 3,4 or 5, you take a step up.
# Roll a 6 and you get to roll the dice again and whatever number it lands on you take that many steps up.
# If you fall (0.01% chance), you go back to step 0.


# Numpy is imported, seed is set
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = (np.random.randint(1, 7))

# Determine what action to take using if statements.
if dice <= 2:
    step = step - 1
elif dice != 6:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)

# Print out dice and step
print('Dice roll was ' + str(dice))
print('Move to step ' + str(step))
