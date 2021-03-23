# Analysing Ireland Rugby match data to determine win rate Home vs Away


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

#print(IrelandDF.head())
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
Home = IrelandDF['Location'].replace(['Dublin','Limerick','Croke Park','Lansdowne Road'],['Home','Home','Home','Home'], inplace=True)
#print(IrelandDF['Location'].value_counts())

missing_values = IrelandDF.isnull().sum()   # Checking if there are any missing values and if there are, how many
#print(missing_values)
# There are no null values in the data, but if there was I could delete the rows using IrelandDF.dropna() or columns using IrelandDF.dropna(axis=1)








# Manipulating the data to suit my goals

# Creating a dataframe with only relevant columns
#print(IrelandDF[['Date, Opposition Name, Result, Location, Opposition Rating, Rating']]) # not sure about this line
IrelandDF.drop(['Opposition Debutants','Debutants','Opposition tries in last 5 games',\
                'Tries in last 5 games','Games since last loss'], inplace=True, axis=1)
# The line above I removed the columns that are irrelevant from the DataFrame
#print(IrelandDF.head(10))


# Sorting Values
# I don't think sorting any of the columns helps my understanding of the data so I will just demonstrate the ability to sort values
Toughest_Opponents = IrelandDF.sort_values('Opposition Rating', ascending=False)
#print(Toughest_Opponents)

# Adding a column
# This isn't complete, can be deleted
#Over_Performed = IrelandDF['Opposition Rating'] > IrelandDF['Rating']
#print(Over_Performed)
#IrelandDF['Won vs higher rated team'] = [Games_Won & Over_Performed]
#print(IrelandDF.head(10))

# For a simple demonstration of adding a column:
IrelandDF['Difference in Rating'] = IrelandDF['Rating'] - IrelandDF['Opposition Rating']
#print(IrelandDF)

# Filtering Wins/Losses/Ties
Games_Won = (IrelandDF[IrelandDF['Result'] > 0]) # This filters the dataframe to show only records where Ireland won a game
Games_Lost = (IrelandDF[IrelandDF['Result'] < 0])
Games_Tied = (IrelandDF[IrelandDF['Result'] == 0])
#print(Games_Won)





# Creating a DataFrame showing Home Game results
Home_GamesDF = IrelandDF[IrelandDF['Location'] == 'Home']
#print(Home_GamesDF)

# Creating a DataFrame showing Away Game results
Away_GamesDF = IrelandDF[IrelandDF['Location'] != 'Home']
#print(Away_GamesDF[['Result']] > 0) # Double square brackets to show a DF not a pandas series



# DF for Home Victories
Home_Games_Won = IrelandDF[(IrelandDF['Result'] > 0) & (IrelandDF['Location'] == 'Home')]
print(Home_Games_Won)

# DF for Home Defeats
Home_Games_Lost = IrelandDF[(IrelandDF['Result'] < 0) & (IrelandDF['Location'] == 'Home')]
#print(Home_Games_Lost.head())

# Home Games Tied
Home_Games_Tied = IrelandDF[(IrelandDF['Result'] == 0) & (IrelandDF['Location'] == 'Home')]
#print(Home_Games_Tied)








# Visualizing the data

# Home Game Win/Loss
#fig, ax = plt.subplots()
#ax.bar()










# Ireland's Rating Over Time. Needs xaxis labels fixed
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(IrelandDF.index, IrelandDF['Rating'], color='green', marker='.') # If I wished to change linestyle: linestyle='-.'
ax.set_title('Irelands World Rugby Rating 2003 - 2018')
ax.set_xlabel('Time')
ax.set_ylabel('World Rugby Team Rating')
##ax.set_xticklabels(IrelandDF.index, rotation=90)
##ax.xaxis.set_major_locator(plt.MaxNLocator(20))
ax.tick_params('y', colors='red')
plt.show()

#fig, ax = plt.subplots()
#ax.hist(IrelandDF.index, IrelandDF['Rating'])
#ax.set_xticklabels(IrelandDF.index, rotation=90)
#ax.set_ylabel('Ratings')
#plt.show()

#Sample Simple Plot
#IrelandDF['Rating'].plot(kind='line')
#plt.show()