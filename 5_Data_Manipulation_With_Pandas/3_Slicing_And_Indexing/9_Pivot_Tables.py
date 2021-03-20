# Pivot Tables

# Pivot temperature by city and year

import pandas as pd

# Add a year column to the temperatures DataFrame, from the year component of the date column
temperatures["year"] = temperatures["date"].dt.year

# Make a pivot table of the avg_temp_c column, with country and city as rows, and year as columns.
# Assign to temp_by_country_city_vs_year, and look at the result.
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# Print the result
print(temp_by_country_city_vs_year)