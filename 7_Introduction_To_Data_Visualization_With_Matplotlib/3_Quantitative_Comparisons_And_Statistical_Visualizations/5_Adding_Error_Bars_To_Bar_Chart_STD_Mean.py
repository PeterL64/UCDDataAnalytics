# Adding Error-Bars to BarCharts - Standard Deviation and Mean


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add a bar with size equal to the mean of the "Height" column in the mens_rowing DataFrame
# and an error-bar of its standard deviation.
ax.bar("Rowing", mens_rowing['Height'].mean(), yerr=mens_rowing['Height'].std())

# Add another bar for the mean of the "Height" column in mens_gymnastics with an error-bar of
# its standard deviation.
ax.bar('Gymnastics', mens_gymnastics['Height'].mean(), yerr=mens_gymnastics['Height'].std())

# Add a label to the the y-axis: "Height (cm)".
ax.set_ylabel("Height (cm)")

plt.show()