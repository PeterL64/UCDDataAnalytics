# SQL Relational Tables  and INNER JOINS

# - Assign to "rs" the results from the following query: select all the records, extracting the "Title" of
#   the record and "Name" of the artist of each record from the "Album" table and the "Artist"
#   table, respectively. To do so, "INNER JOIN" these two tables on the "ArtistID" column of both.
# - In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs.
#   Store them in the DataFrame df.
# - Set the DataFrame's column names to the corresponding names of the table columns.


# Import Packages and Create Engine to query file
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())