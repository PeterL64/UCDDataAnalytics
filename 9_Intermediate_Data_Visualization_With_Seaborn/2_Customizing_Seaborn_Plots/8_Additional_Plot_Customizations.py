# Additional Plot Customizations

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of 1 bedroom rents
sns.distplot(df['fmr_1'], ax=ax)

# Modify the x axis label to say "1 Bedroom Fair Market Rent".
# Change the x axis limits to be between 100 and 1500.
# Add a descriptive title of "US Rent" to the plot.
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100,1500),
       title="US Rent")

# Display the plot
plt.show()