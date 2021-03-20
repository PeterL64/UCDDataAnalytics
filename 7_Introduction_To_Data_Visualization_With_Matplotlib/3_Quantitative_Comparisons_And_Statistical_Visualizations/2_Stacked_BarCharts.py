# Stacking BarCharts on top of one another

# Call the ax.bar method to add the "Gold" medals. Call it with the label set to "Gold".
ax.bar(medals.index, medals['Gold'], label='Gold')

# Call the ax.bar method to stack "Silver" bars on top of that, using the bottom key-word argument so
# the bottom of the bars will be on top of the gold medal bars, and label to add the label "Silver".
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'], bottom= medals['Gold'] + medals['Silver'], label='Bronze')

# Display the legend
ax.legend()

plt.show()