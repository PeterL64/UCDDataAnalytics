# The pandas way to query

# After creating a Database Engine you can get the results of any particular query using just 4 lines of code
# as shown below; Connecting, Executing the Query, Passing the results to a DataFrame, and Naming the Columns

from sqlalcheny import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Orders')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# All the code above can be done using 1 line of code.
# Using the pandas function read_sql_query() and passing it 2 arguments. The first argument you want to
# make is the SQL query you wish to make, the second argument is the engine you want to connect to.
df = pd.read_sql_query('SELECT * FROM Orders', engine)
