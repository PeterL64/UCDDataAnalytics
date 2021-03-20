# Counting categorical variables

import pandas as pd


# Count the number of stores of each store type in store_types
store_counts = store_types["type"].value_counts()   # Select the type column of store_types, then call .value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True) # Select the department column of store_depts and call .value_counts()
print(store_props)  # The normalize argument above changes the counts into proportions of the total

# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)   # The sort argument of the value_counts method sorts the values when set to True

# Count the proportion of different departments in store_depts, sorting the proportions in descending order.
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)    # value_counts can have more than one argument