# Self Join


# To a variable called crews_self_merged, merge the crews table to itself on the id column using
# an inner join, setting the suffixes to '_dir' and '_crew' for the left and right tables respectively.
crews_self_merged = crews.merge(crews, on='id', how='inner', suffixes=('_dir', '_crew'))

# Create a Boolean index, named boolean_filter, that selects rows from the left table
# with the job of 'Director' and avoids rows with the job of 'Director' in the right table.
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())
