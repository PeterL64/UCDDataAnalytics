# Inner Joins/Merge for two joined Dataframes/Tables

# Joins and Merges are the same thing.
# DataFrames and ^Tables are the same thing.

# Merge the taxi_owners and taxi_veh tables on the column vid
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Set the left and right table suffixes for overlapping columns of the merge to _own and _veh.
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

# Select the fuel_type column from taxi_own_veh and print the value_counts()
# to find the most popular fuel_types used.
print(taxi_own_veh['fuel_type'].value_counts())