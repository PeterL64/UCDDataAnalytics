# Querying an SQL Database in Python

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine and store in variable: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open the engine connection as variable con using the method connect() on the engine.
con = engine.connect()

# Execute the query that selects ALL columns from the Album table. Store the results in rs
rs = con.execute('SELECT * FROM Album')

# Store all query results in the DataFrame df by applying the fetchall() method to the results rs
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()