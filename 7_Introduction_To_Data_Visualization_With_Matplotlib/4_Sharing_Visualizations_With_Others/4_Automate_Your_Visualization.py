# Automate Your Visualization

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Iterate over the values of sports setting sport as your loop variable.
# In each iteration, extract the rows where the "Sport" column is equal to sport.
# Add a bar to the provided ax object, labeled with the sport name, with the mean of
# the "Weight" column as its height, and the standard deviation as a y-axis error bar.

# Loop over the different sports branches
for sport in sports:
    # Extract the rows only for this sport
    sport_df = summer_2016_medals[summer_2016_medals['Sport'] == sport]
    # Add a bar for the "Weight" mean with std y error bar
    ax.bar(sport, sport_df['Weight'].mean(), yerr=sport_df['Weight'].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file and show the figure.
fig.savefig('sports_weights.png')
plt.show()