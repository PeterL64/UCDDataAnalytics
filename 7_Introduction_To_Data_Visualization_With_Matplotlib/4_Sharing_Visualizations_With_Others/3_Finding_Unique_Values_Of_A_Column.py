# Unique Values of a column

# Create a variable called sports_column that holds the data
# from the "Sport" column of the DataFrame object.
sports_column = summer_2016_medals['Sport']

# Use the unique method of this variable to find all the unique different sports
# that are present in this data, and assign these values into a new variable called sports.
sports = sports_column.unique()

# Print the sports variable to the console.
print(sports)