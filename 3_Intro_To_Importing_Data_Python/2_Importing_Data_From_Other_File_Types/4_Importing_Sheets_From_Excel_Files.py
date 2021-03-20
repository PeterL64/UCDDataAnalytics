# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004') # parse is the method used to load a particular sheet as a Data Frame using one argument,
                        # the name of the sheet, or as seen below, the index of the sheet.

# Print the head of the DataFrame df1
print(df1.head())       # Use .head() method to get a quick overview, i.e. printing the first 5 rows & header

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)      # Loading a sheet using it's index rather than sheet name

# Print the head of the DataFrame df2
print(df2.head())