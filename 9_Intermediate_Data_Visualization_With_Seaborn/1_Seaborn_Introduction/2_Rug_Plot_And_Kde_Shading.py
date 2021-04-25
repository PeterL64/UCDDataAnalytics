# Rug Plot and kde shading


# Create a distplot of the Award_Amount column in the df.
# Configure it to show a shaded kde (using the kde_kws dictionary).
# Add a rug plot above the x axis.
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade':True})

# Plot the results
plt.show()