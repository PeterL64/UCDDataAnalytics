# Ordering SQL Records with ORDER BY

# Importing Packages
import pandas as pd
from sqlalchemy import create_engine

# Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite
# and assign it to the variable: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# - In the context manager, execute the query that selects all records from the Employee table
#   and orders them in increasing order by the column BirthDate. Assign the result to rs.
# - In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all
#   records in rs. Store them in the DataFrame df.
# - Set the DataFrame's column names to the corresponding names of the table columns.
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame, df.
print(df.head())


# After creating a Database Engine you can get the results of any particular query using just 4 lines of code
# as shown above; Connecting, Executing the Query, Passing the results to a DataFrame, and Naming the Columns
