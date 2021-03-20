# One-to-Many Merge/Join

# Starting with the licenses table on the left, merge it to the biz_owners table
# on the column account, and save the results to a variable named licenses_owners.
licenses_owners = licenses.merge(biz_owners, on='account')

# Group licenses_owners by title and count the number of accounts for each title.
# Save the result as counted_df.
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort counted_df by the number of accounts in descending order, and save this as
# a variable named sorted_df.
sorted_df = counted_df.sort_values('account', ascending=False)

# Print the head of sorted_df.
print(sorted_df.head())