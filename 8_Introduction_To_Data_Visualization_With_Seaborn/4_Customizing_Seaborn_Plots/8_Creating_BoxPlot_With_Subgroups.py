# Box Plot with Subgroups

# Set palette to "Blues"
sns.set_palette('Blues')

# Add subgroups to colour the box plots based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data,
                kind="box", hue='Interested in Pets')

# Set the title of the FacetGrid object g to "Age of Those Interested in Pets vs. Not".
g.fig.suptitle('Age of Those Interested in Pets vs. Not')

# Make the plot display
plt.show()