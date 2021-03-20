# Customizing Spreadsheet Imports
# Skipping Rows and Renaming Columns


# Assign spreadsheet filename to the variable: file
file = 'battledeath.xlsx'

# Load spreadsheet using Pandas and assign it to the variable: xls
xls = pd.ExcelFile(file)

# Parse the first sheet by index, skip the first row, rename the columns and assign to: df1
df1 = xls.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet by index, skip first row, rename the column and assign to: df2
df2 = xls.parse(1, usecols=0, skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())