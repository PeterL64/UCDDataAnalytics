# Calculating on a Pivot Table

# Pivot tables are filled with summary statistics, but they are only a first step to finding something
# insightful. Often you'll need to perform further calculations on them. A common thing to do is to
# find the rows or columns where the highest or lowest value occurs.
# Recall that you can easily subset a Series or DataFrame to find rows of interest using
# a logical condition inside of square brackets. For example: series[series > value].

# temp_by_country_city_vs_year is a DataFrame from earlier.
import pandas as pd

# Calculate the worldwide mean temperature for each year, assigning to mean_temp_by_year.
# Call .mean() without arguments to get the mean of each column
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
# Use Boolean filtering of the form mean_temp_by_year equal to mean_temp_by_year.max()
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Calculate the mean temperature for each city (across columns), assigning to mean_temp_by_city.
# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
