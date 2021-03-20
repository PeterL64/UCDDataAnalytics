# Parts of a Data Frame

# To better understand DataFrame objects, it's useful to know that they consist of three components,
# stored as attributes:
# .values: A two-dimensional NumPy array of values.
# .columns: An index of columns: the column names.
# .index: An index for the rows: either row numbers or row names.

# You can usually think of indexes as a list of strings or numbers, though the pandas Index data type allows
# for more sophisticated options.


# Import pandas
import pandas as pd

# Print the values of homelessness (as a 2D Numpy Array)
print(homelessness.values)

# Print the column index (names) of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)