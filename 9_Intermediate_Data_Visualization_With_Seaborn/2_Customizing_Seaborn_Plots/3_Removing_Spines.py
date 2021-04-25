# Removing Spines

# In general, visualizations should minimize extraneous markings so that the data speaks for itself.
# Seaborn allows you to remove the lines on the top, bottom, left and right axis, which are often called spines.

# Use a white style for the plot.
sns.set_style('white')
# Create a lmplot() comparing the pop2010 and the fmr_2 columns.
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')
# Remove the top and right spines using despine().
sns.despine()
# Remove the left and bottom spine
sns.despine(left=True, bottom=True)#This removes the default, top and right spines as well as the left and bottom spines

# Show the plot and clear the figure
plt.show()
plt.clf()

