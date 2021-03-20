# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
# - Using the pandas function create_engine(), create an engine for
#   the SQLite database Chinook.sqlite and assign it to the variable engine
df = pd.read_sql_query('SELECT * FROM Album', engine)


# The remainder of the code is included to confirm that the DataFrame created
# by this method is equal to that created by the previous method I learned.

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))