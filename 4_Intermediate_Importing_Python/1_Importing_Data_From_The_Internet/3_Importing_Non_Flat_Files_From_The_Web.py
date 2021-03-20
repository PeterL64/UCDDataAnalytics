# Importing non-flat files from the web
# Importing and Reading an Excel File without saving it locally

# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
# Read the file in url into a dictionary xls using pd.read_excel() recalling that, in order to import all
# sheets you need to pass None to the argument sheet_name.
xls = pd.read_excel(url, sheet_name=None)

# Print the sheet names in the Excel spreadsheet to the shell. The sheet names are the keys of the dictionary.
print(xls.keys())

# Print the head of the first sheet (using its name, which is '1700', not its index)
print(xls['1700'].head())
