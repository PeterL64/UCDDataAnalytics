# Adding Columns To Data Frames

# Adding a column to a DataFrame takes the form:
# df["new_col"] = df["col_a"] + df["col_b"]


# Add a new column to homelessness, named total, containing the sum of
# the individuals and family_members columns.
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add another column to homelessness, named p_individuals, containing the
# proportion of homeless people in each state who are individuals.
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

# Print the result
print(homelessness)