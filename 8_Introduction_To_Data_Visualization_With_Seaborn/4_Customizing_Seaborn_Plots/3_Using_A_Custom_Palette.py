# Using a Custom Palette


# Example of a custom palette:
custom_palette = ['#FBB4AE','#B3CDE3','#CCEBC5','#DECBE4','#FED9A6','#FFFFCC','#E5D8BD','#FDDAEC','#F2F2F2']
# Each of the above represents a different colour.

# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette with the hex color codes "#39A7D0" and "#36ADA4".
sns.set_palette(['#39A7D0','#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age",
            data=survey_data, kind="box")

# Show plot
plt.show()# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
sns.set_palette(['#39A7D0','#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age",
            data=survey_data, kind="box")

# Show plot
plt.show()