# Cumulative Statistics

import pandas as pd
# sales_1_! is a sample DataFrame for data of 1 department of 1 store.
# Sort sales_1_1 by date in ascending order
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, and add it as a new column of sales_1_1 called cum_weekly_sales.
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])