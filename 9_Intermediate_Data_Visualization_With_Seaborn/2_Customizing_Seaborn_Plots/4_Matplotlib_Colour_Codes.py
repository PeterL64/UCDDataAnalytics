# Matplotlib Colour(color) Codes

# Seaborn offers several options for modifying the colors of your visualizations.
# The simplest approach is to explicitly state the color of the plot.
# A quick way to change colors is to use the standard matplotlib color codes.

# Set the default Seaborn style and enable the matplotlib color codes.
sns.set(color_codes=True)

# Create a distplot for the fmr_3 column using matplotlib's magenta (m) color code.
sns.distplot(df['fmr_3'], color='m')

plt.show()


# The code above can be on top of each line
# sns.set(color_codes=True)
# sns.distplot(df['fmr_3'], color='m')
# plt.show()