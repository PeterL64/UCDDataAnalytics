# Using an Outer Join to select actors who were not in Both Iron man 1 and 2


# Save to iron_1_and_2 the merge of iron_1_actors (left) with iron_2_actors tables with an
# outer join on the id column, and set suffixes to ('_1','_2').
iron_1_and_2 = iron_1_actors.merge(iron_2_actors, on='id', how='outer', suffixes=('_1','_2'))

# Create an index that returns True if name_1 or name_2 are null, and False otherwise.
m = ((iron_1_and_2['name_1'].isnull()) |
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())