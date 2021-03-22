import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# File name
file = "IREMatchData(FULL).csv"
# file = r"C:\Users\peter\Desktop\UCD Data Analytics\Project\Ireland Rugby\IREMatchData(FULL).csv"

# Loading file
IrelandDF = pd.read_csv(file, index_col = 1)    # Importing in Pandas DataFrame rather than a Numpy array because there is multiple data types involved
# Alternatively loading file directly from file location below:
# IrelandDF = pd.read_csv(r"C:\Users\peter\Desktop\UCD Data Analytics\Project\Ireland Rugby\IREMatchData(FULL).csv")

# Exploring the raw data
print(IrelandDF.head())
#print(IrelandDF.shape)
#print(IrelandDF.count())   # The number of values in each column is = the number of rows seen in .shape so I can conclude there are no null values
#print(IrelandDF.info())
#print(IrelandDF.index)
#print(IrelandDF.columns)
#print(IrelandDF.dtypes)
#print(type(IrelandDF))
#print(IrelandDF['Opposition Name'].unique())   # Showing a list of all the opposition Ireland faced
#print(IrelandDF.nunique())  # Showing the total number of unique values in each column
#print(IrelandDF['Opposition Name'].value_counts())  # Shows how many times Ireland played against each team
#print(IrelandDF['Location'].value_counts()) # Shows location of games. Concerned here about home vs away
# Lansdowne Road, Croke Park, Limerick and Dublin will be changed to 'Home' because they would be considered Home Games

#missing_values = IrelandDF.isnull().sum()   # Checking if there are any missing values and if there are, how many
#print(missing_values)
# There are no null values in the data, but if there was I could delete the rows using IrelandDF.dropna() or columns using IrelandDF.dropna(axis=1)



# Filtering Wins/Losses/Ties
Games_Won = (IrelandDF[IrelandDF['Result'] > 0]) # This filters the dataframe to show only records where Ireland won a game
Games_Lost = (IrelandDF[IrelandDF['Result'] < 0])
Games_Tied = (IrelandDF[IrelandDF['Result'] == 0])
print(Games_Tied)