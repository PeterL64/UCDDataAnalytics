# Using Pandas to import Excel Sheets

# Import pandas
import pandas as pd

# Assign spreadsheet filename to the variable: file
file = 'battledeath.xlsx'

# Load spreadsheet using Pandas and assign it to the variable: xls
xls = pd.ExcelFile(file)    # .ExcelFile is a function used to assign an excel file to a variable, (xls here)

# Print sheet names
print(xls.sheet_names)      # sheet_names is a command to print out the sheet names so you can see them and
                            # have the option to use them at your leisure.
