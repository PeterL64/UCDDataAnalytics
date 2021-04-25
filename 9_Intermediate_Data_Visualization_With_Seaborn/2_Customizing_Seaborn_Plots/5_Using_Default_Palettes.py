# Using Default Palettes

# Seaborn includes several default palettes that can be easily applied to your plots.

# Create a for loop to show the difference between the bright and colorblind palette.
# Set the palette using the set_palette() function.
# Use a distplot of the fmr_3 column.

for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()
    # Clear the plots
    plt.clf()