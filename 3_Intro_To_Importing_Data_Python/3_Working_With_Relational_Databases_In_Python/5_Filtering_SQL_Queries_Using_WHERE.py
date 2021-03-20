# Filtering Database records using SQL's WHERE command


# Import Packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine for the SQLite database and store in variable: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
# - Execute the query that selects all records from the Employee table where 'EmployeeId' is greater
# than or equal to 6. Assign the results to rs.
# - Apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
# - Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())