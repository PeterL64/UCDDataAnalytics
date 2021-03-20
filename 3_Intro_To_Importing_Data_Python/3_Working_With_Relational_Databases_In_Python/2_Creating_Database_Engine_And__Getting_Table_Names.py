# Import the function create_engine from the module sqlalchemy
from sqlalchemy import create_engine

# Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
engine = create_engine('sqlite:///Chinook.sqlite')

# Using the method table_names() on the engine (I named engine), assign the table names
# of 'Chinook.sqlite' to the variable table_names.
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)
