# CHanging Data Type to a type that suits you

# In this exercise, and throughout this chapter, you'll be working with bicycle ride sharing data in
# San Francisco called ride_sharing. It contains information on the start and end stations,
# the trip duration, and some user information for a bike sharing service.


# Print the information of ride_sharing.
print(ride_sharing.info())

# Use .describe() to print the summary statistics of the user_type column from ride_sharing.
print(ride_sharing['user_type'].describe())

# Convert user_type into categorical by assigning it the 'category' data type and store it in the user_type_cat column.
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Make sure you converted user_type_cat correctly by using an assert statement.
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics
print(ride_sharing['user_type_cat'].describe())
