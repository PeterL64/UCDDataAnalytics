# Dropping Duplicates

import pandas as pd

# Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())

# Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())

# Subset the rows that are holiday weeks using the is_holiday column, and drop the
# duplicate dates, saving as holiday_dates.
holiday_dates = sales[sales['is_holiday']==True].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates)