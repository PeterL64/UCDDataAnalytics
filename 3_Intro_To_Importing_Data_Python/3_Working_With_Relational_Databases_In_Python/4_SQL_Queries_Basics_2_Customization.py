# Customizing SQL Queries Using Python


# Import Packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine and store in variable: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager and store as con. Perform query and save results to DataFrame: df
with engine.connect() as con:                                   # Storing the engine connection in variable con
    rs = con.execute('SELECT LastName, Title FROM Employee')    # Line 13
    df = pd.DataFrame(rs.fetchmany(3))                          # Line 14   fetchmany(size=3) is in my notes but both seem to work
    df.columns = rs.keys()                                      # Line 15
# Line 13: Execute the SQL query that selects the columns LastName and Title from
# the Employee table. Store the results in the variable rs
# Line 14: Apply the method fetchmany() to rs in order to retrieve 3 of
# the records. Store them in the DataFrame df
# Line 15: Using the rs object, set the DataFrame's column names to the
# corresponding names of the table columns.

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())