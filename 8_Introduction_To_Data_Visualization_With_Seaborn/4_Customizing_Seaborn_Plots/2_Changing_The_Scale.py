# Changing the scale

# Use sns.set_context() to change the scale of the plot elements and labels.
# Some options, Smallest to Largest: 'paper', 'notebook', 'talk', 'poster'.


# Set the scale ("context") to "paper", which is the smallest of the scale options.
sns.set_context('paper')

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "notebook" to increase the scale.
sns.set_context('notebook')
plt.show()

# Change the context to "talk" to increase the scale.
sns.set_context('talk')
plt.show()

# Change the context to "poster", which is the largest scale available.
sns.set_context('poster')
plt.show()