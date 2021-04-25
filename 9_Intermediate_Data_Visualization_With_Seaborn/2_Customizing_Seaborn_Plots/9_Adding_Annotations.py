# Adding Annotations

# Create a figure and axes. Then plot the fmr_1 column distribution.
fig, ax = plt.subplots()
sns.distplot(df['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")

# Add a vertical line using axvline for the median and mean of the values which are already defined.
ax.axvline(x=634.0, color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x=706.3254351016984, color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
plt.show()