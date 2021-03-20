# Creating A Bar Chart with Matplotlib

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Call the ax.bar method to plot the "Gold" column as a function of the country.
ax.bar(medals.index, medals['Gold'])

# Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.
# In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by
# using the rotation key-word argument.
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label to "Number of medals".
ax.set_ylabel('Number of medals')

# Show the chart
plt.show()