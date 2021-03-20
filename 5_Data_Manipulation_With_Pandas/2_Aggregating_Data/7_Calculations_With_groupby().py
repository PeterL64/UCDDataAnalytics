# Calculations with .groupby()
# Here I will perform the same calculations as the last exercise, but ust the .groupby() method.
# This will show that the .groupby() method is better than the previous exercise because it can
# perform the same calculations with 1 line of code

# Using the same sales DataFrame

import pandas as pd

# Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Calculate the proportion of sales at each store type by dividing by the sum of
# sales_by_type. Assign to sales_propn_by_type
sales_propn_by_type = sales.groupby('type')['weekly_sales'].agg(sum) / sum(sales_by_type)
print(sales_propn_by_type)

# Group sales by "type" and "is_holiday", take the sum of weekly_sales,
# and store as sales_by_type_is_holiday
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# x.groupby(['colA','colB'])['colC'].sum
# DataFrame.Method(argument[List])[List].Method()