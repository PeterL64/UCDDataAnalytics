# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read(Import) the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head()) # This allows you to check the first 5 rows plus the Headers