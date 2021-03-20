# Left Join with Missing Values

# Merge the movies table, as the left table, with the financials table using a left join,
# and save the result to movies_financials.
movies_financials = movies.merge(financials, on='id', how='left') # how='left' for left Join.

# Count the number of rows in movies_financials with a null value in the budget column.
number_of_missing_fin = movies_financials['budget'].isnull().sum() # Counting the Null Values

# Print the number of movies missing financials
print(number_of_missing_fin)