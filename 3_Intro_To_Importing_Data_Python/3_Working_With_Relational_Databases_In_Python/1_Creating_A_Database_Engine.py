# Creating a Database Engine

# Creating an engine to connect to SQLite databases


# Import the function create_engine() from the module sqlalchemy
from sqlalchemy import create_engine

# Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to the variable: engine
engine = create_engine('sqlite:///Chinook.sqlite')