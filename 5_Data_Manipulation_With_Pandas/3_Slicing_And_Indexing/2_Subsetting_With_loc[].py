# Subsetting with .loc[]
# When you pass .loc[] a single argument it will take a subset of rows

import pandas as pd

# Create a list called cities that contains "Moscow" and "Saint Petersburg".
cities = ["Moscow", "Saint Petersburg"]

# Use [] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
print(temperatures[temperatures['city'].isin(cities)])

# Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.
print(temperatures_ind.loc[cities])