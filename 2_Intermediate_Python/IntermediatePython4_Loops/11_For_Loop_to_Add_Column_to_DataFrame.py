# Adding a new column to a Pandas DataFrame

# I will be adding a column listing all the countries in Capital Letters without using a for loop


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)  # I am adding a new column here

print(cars)