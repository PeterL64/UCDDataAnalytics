# Efficient Summaries

# The .agg() method allows you to apply your own custom functions to a DataFrame, as well as
# apply functions to more than one column of a DataFrame at once, making your aggregations
# super-efficient. Syntax below:
# df['column'].agg(function)

import pandas as pd


# A custom inter-quartile range (IQR) function is available for me to use.
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Print IQR of the temperature_c column of the sales DataFrame
print(sales['temperature_c'].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))
# np.median is a pandas function