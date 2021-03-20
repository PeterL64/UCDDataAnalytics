# Merging/Joining 3 Tables/DataFrames

# Starting with the licenses table, merge to it the zip_demo table on the zip column.
# Then merge the resulting table to the wards table on the ward column. Save result of the three
# merged tables to a variable named licenses_zip_ward.
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
    .merge(wards, on='ward')

# Group the results of the three merged tables by the column alderman and find the median income.
# Print the result.
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))