# Slicing Dates (Time Series)

# Slicing is particularly useful for time series since it's a common thing to want to filter for
# data within a date range. Add the date column to the index, then use .loc[] to perform the
# subsetting. The important thing to remember is to keep your dates in ISO 8601 format,
# that is, yyyy-mm-dd.

# Recall that you can combine multiple Boolean conditions using logical operators (such as &). To do
# so in one line of code, you'll need to add parentheses () around each condition.

import pandas as pd

# Use Boolean conditions (not .isin() or .loc[]) to subset for rows in 2010 and 2011,
# and print the results
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)
# Note that because the date isn't set as an index, a condition that contains only a year, such as
# df["date"] == "2009", will check if the date is equal to the first day of the first month of the
# year (e.g. 2009-01-01), rather than checking whether the date occurs within the given year.
# It is recommended to write out the full date when using Boolean conditions (e.g., 2009-12-31).
# Subsetting via Boolean conditions takes the form df[(condition1) & (condition2)]

# Set date as an index and sort the index
# Use .set_index() to set the index, followed by .sort_index() to sort the index.
temperatures_ind = temperatures.set_index("date").sort_index()

# Subsetting via .loc[] takes the form df["first":"last"]
# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])