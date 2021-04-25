# Stripplot() and Swarmplot()

# Categorical data

# Create a stripplot of the Award_Amount with the Model Selected on the y axis with jitter enabled.
sns.stripplot(data=df, x='Award_Amount', y='Model Selected', jitter=True)

plt.show()

# Create a swarmplot() of the same data, but also include the hue by Region.
sns.swarmplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         hue='Region')

plt.show()