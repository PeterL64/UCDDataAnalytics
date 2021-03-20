# Putting everything from the previous files together





# Add a column to homelessness, indiv_per_10k, containing the number of homeless
# individuals per ten thousand people in each state.
# Create indiv_per_10k col as homeless individuals per 10k state pop.
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]
# To add a column, use syntax: df["new_col"] = df["col_a"] / df["col_b"]

# Subset rows where indiv_per_10k is higher than 20, assigning to high_homelessness.
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
# To filter rows, use syntax: df[df["col"] > n]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)
# To sort rows, use syntax: df.sort_values("col", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]
# To select columns, use syntax: like df[["col_a", "col_b"]]

# Print the result
print(result)