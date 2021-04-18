# Adding a title and axis labels

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean",
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title('Average MPG Over Time')

# # Label the x-axis as "Car Model Year" and the y-axis as "Average MPG".
g.set(xlabel='Car Model Year', ylabel='Average MPG')

# Show plot
plt.show()


