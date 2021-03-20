# Creating Box Plots

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Create a boxplot that contains the "Height" column for mens_rowing on the left
# and mens_gymnastics on the right.
ax.boxplot([mens_rowing['Height'],mens_gymnastics['Height']])

# Add x-axis tick labels: "Rowing" and "Gymnastics".
ax.set_xticklabels(['Rowing','Gymnastics'])

# Add a y-axis label: "Height (cm)".
ax.set_ylabel('Height (cm)')

plt.show()
