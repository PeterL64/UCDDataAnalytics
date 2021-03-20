# Pandas for More Complex Querying

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)
print(df.head())

# Import Packages.
# Create engine for sqlite file and store as: engine.
# Execute the query and store the recorde in a DataFrame called: df
# - Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from
#   the following query: select all records from the Employee table where the EmployeeId is greater than
#   or equal to 6 and ordered by BirthDate (make sure to use WHERE and ORDER BY in this precise order).
