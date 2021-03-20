# Complete Pivot Table Summarization

# The .pivot_table() method has several useful arguments, including fill_value and margins.
# fill_value replaces missing values with a real value (known as imputation).
# The simplest thing to do is replace it with a dummy value.
# margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of
# those variables separately: it gives the row and column totals of the pivot table contents.

import pandas as pd
import numpy as np

# Print the mean weekly_sales by department and type, filling in any missing values with 0
print(sales.pivot_table(values='weekly_sales', index='department', columns=type, aggfunc=np.mean, fill_value=0))


# # Print the mean weekly_sales by department and type;
# fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", aggfunc=np.mean, fill_value=0, margins=True))

# Syntax
# DataFrame.pivot_table(Argument='Column',Arg='Column',Arg='Column',Arg=NumpyFunction,Arg=ReplacementValue,Arg=TrueorFalse)
# Argument Meanings;
# values: The column that you want to summarize.

# index: The index is the column you want to group by, seen on the left most column of your new DataFrame.
# By default, pivot tables take the mean value for each group.

# aggfunc: AggregateFunction. If you want a different summary statistic, you can use aggfunc. This is
# where you place the functions you wish to use. Do not need to call them so no () at the end of each
# function. Use [] to get multiple summary statistics by using a list of functions.

# columns: To group by two variables, pass a second column name to the columns argument. This creates a table
# with the index column name being the row labels, and the column column name being the column names in your
# new DataFrame.

# fill_value: Allows you to fill in any missing values with a string or integer of your choice.

# margins=True: This sets the last row and column to contain the mean of all the values in the column
# or the row. Great for summarizing.