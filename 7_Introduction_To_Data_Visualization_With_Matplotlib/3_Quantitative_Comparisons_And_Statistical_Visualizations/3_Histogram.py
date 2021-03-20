# Plotting a Histogram of mens gymnastics vs rowing weights

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Use the ax.hist method to add a histogram of the "Weight" column from the mens_rowing DataFrame.
ax.hist(mens_rowing['Weight'])

# Use ax.hist to add a histogram of "Weight" for the mens_gymnastics DataFrame.
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)" and the y-axis label to "# of observations".
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('# of observations')
plt.show()