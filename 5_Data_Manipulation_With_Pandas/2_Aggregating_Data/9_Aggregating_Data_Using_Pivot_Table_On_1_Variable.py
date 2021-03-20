# Pivoting on one variable

# In pandas, pivot tables are essentially just another way of performing grouped calculations.
# The .pivot_table() method is just an alternative to the .groupby() method.

import pandas as pd
import numpy as np

# Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.
# Pivot for mean weekly_sales for each store type.
mean_sales_by_type = sales.pivot_table(values='weekly_sales',index='type')

# Print mean_sales_by_type
print(mean_sales_by_type)

# Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table()
# and store as mean_med_sales_by_type.
# Pivot for mean and median weekly_sales for each store type.
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=[np.mean,np.median])
# [] for the aggfunc argument if there is a list of functions

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)


# Pivot on two variables
# Get the mean of weekly_sales by type and is_holiday using .pivot_table()
# and store as mean_sales_by_type_holiday
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales',index='type',columns='is_holiday',aggfunc=np.mean)

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

