# Creating two-factor subplots

# Use relplot() to create a scatter plot with "G1" on the x-axis and "G3" on the y-axis,
# using the student_data DataFrame.
sns.relplot(data=student_data, x='G1', y='G3', kind='scatter')

# Create column subplots based on whether the student received support from the school ("schoolsup"),
# ordered so that "yes" comes before "no".
sns.relplot(data=student_data, x='G1', y='G3', kind='scatter', col='schoolsup', col_order=['yes','no'])

# Add row subplots based on whether the student received support from the family ("famsup"),
# ordered so that "yes" comes before "no". This will result in subplots based on two factors.
sns.relplot(x="G1", y="G3", data=student_data, kind="scatter", col="schoolsup",col_order=["yes", "no"],
            row='famsup', row_order=['yes','no'])

plt.show()