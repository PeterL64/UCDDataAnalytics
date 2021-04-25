# Box Plots, Violin Plots, and LV(Letter-Value) Plots

# Create and display a boxplot of the data with Award_Amount on the x axis and Model Selected on the y axis.
sns.boxplot(data=df,
         x='Award_Amount',
         y='Model Selected')

plt.show()
plt.clf()

# Create and display a similar violinplot of the data, but use the husl palette for colors.
sns.violinplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='husl')

plt.show()
plt.clf()

# Create and display an lvplot using the Paired palette and the Region column as the hue.
sns.lvplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='Paired',
         hue='Region')

plt.show()
plt.clf()