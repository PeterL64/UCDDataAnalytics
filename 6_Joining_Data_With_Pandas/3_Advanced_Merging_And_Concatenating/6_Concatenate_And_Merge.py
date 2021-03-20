# Concatenate and Merge to find common songs

# Concatenate the classic_18 and classic_19 tables vertically where the index goes from 0 to n-1,
# and save to classic_18_19.
classic_18_19 = pd.concat([classic_18,classic_19], ignore_index=True)

# Concatenate the pop_18 and pop_19 tables vertically where the index goes from 0 to n-1,
# and save to pop_18_19.
pop_18_19 = pd.concat([pop_18,pop_19], ignore_index=True, verify_integrity=False)
# verify_integrity is not needed here, just have it as a refresher for myself.

# With classic_18_19 on the left, merge it with pop_18_19 on tid using an inner join.
classic_pop = classic_18_19.merge(pop_18_19, on= 'tid', how='inner')

# Use .isin() to filter classic_18_19 where tid is in classic_pop.
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)