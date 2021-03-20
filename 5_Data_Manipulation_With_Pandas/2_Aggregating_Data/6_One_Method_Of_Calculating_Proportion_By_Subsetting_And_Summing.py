# What percentage of sales occurred at each store type
# Calculating grouped summary statistics without using the .groupby() method

# From the sales DataFrame, Walmart has three different store types, A, B and C

import pandas as pd

# Calculate the total weekly_sales over the whole dataset.
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum() # .agg(sum) gives the same answer

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales['type'] == 'B']['weekly_sales'].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales['type'] == 'C']['weekly_sales'].sum()

# Get proportion for each type
# Combine the A/B/C results into a list, and divide by sales_all to get the proportion of sales by type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)