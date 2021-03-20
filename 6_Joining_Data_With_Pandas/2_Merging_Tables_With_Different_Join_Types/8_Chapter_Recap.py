# Using all I have learned in this chapter to check do Sequels earn more than Originals


# With the sequels table on the left, merge to it the financials table on index named id,
# ensuring that all the rows from the sequels are returned and some rows from
# the other table may not be returned, Save the results to sequels_fin.
sequels_fin = sequels.merge(financials, on='id', how='left')

# Merge the sequels_fin table to itself with an inner join, where the left and right tables merge
# on 'sequel' and 'id' respectively with suffixes equal to ('_org','_seq'), saving to orig_seq.
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff columns of orig_seq and save this as titles_diff.
titles_diff = orig_seq[['title_org','title_seq','diff']] # Remembering the DOUBLE SQUARE BRACKETS

# Sort by titles_diff by diff in descending order and print the first few rows.
print(titles_diff.sort_values('diff', ascending=False).head())
