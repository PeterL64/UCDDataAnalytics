# Histogram Customizations, Step, Bins, Histtype, Label

fig, ax = plt.subplots()

# Use the hist method to display a histogram of the "Weight" column from the mens_rowing DataFrame.
# Label this as "Rowing", add 5 bins and add the histtype as 'step'.
ax.hist(mens_rowing['Weight'], label='Rowing', histtype='step', bins=5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'], label='Gymnastics', histtype='step', bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()