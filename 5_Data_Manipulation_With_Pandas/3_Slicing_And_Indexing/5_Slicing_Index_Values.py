# Slicing index values

# Slicing lets you select consecutive elements of an object using first:last syntax.
# DataFrames can be sliced by index values or by row/column number.

# Compared to slicing lists, there are a few things to remember:
# - You can only slice an index if the index is sorted (using .sort_index()).
# - To slice at the outer level, first and last can be strings.
# - To slice at inner levels, first and last should be tuples. If you
#   pass a single slice to .loc[], it will slice the rows.

import pandas as pd

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Use slicing with .loc[] to subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])

# Test case, try to subset rows from Lahore to Moscow. See how it returns nonsense
print(temperatures_srt.loc['Lahore':'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia','Moscow')])