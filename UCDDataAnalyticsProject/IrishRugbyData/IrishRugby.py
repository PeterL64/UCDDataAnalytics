# Analysing Ireland Rugby match data to determine win rate Home vs Away


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 500)

# File name
file = "IREMatchData(FULL).csv"
# file = r"C:\Users\peter\Desktop\UCD Data Analytics\Project\Ireland Rugby\IREMatchData(FULL).csv"

# Loading file
IrelandDF = pd.read_csv(file) #(, index_col = 1 after file)   # Importing in Pandas DataFrame rather than a Numpy array because there is multiple data types involved
# Alternatively loading file directly from file location below:
# IrelandDF = pd.read_csv(r"C:\Users\peter\Desktop\UCD Data Analytics\Project\Ireland Rugby\IREMatchData(FULL).csv")

#print(IrelandDF)

# EXPLORING THE RAW DATA

#print(IrelandDF.head())    # Showing first 5 rows of data
#print(IrelandDF.shape)     # Quick view of how many rows and columns there are
#print(IrelandDF.count())   # The number of values in each column is = the number of rows seen in .shape so I can conclude there are no null values
#print(IrelandDF.info())    # Quick overview of the type of data in each column
#print(IrelandDF.index)     # A list of the index values
#print(IrelandDF.columns)   # Showing the column names
#print(IrelandDF.dtypes)    # Checking the type of data in each column
#print(type(IrelandDF))     # Checking the type of data IrelandDF is, to make sure it is a DataFrame
#print(IrelandDF['Opposition Name'].unique())   # Showing a list of all the opposition Ireland faced
#print(IrelandDF.nunique())  # Showing the total number of unique values in each column
#print(IrelandDF['Opposition Name'].value_counts())  # Shows how many times Ireland played against each team

#print(IrelandDF['Location'].value_counts()) # Shows location of games. Concerned here about home vs away
# Lansdowne Road, Croke Park, Limerick and Dublin will be changed to 'Home' because they would be considered Home Games
IrelandDF['Location'].replace(['Dublin','Limerick','Croke Park','Lansdowne Road'],['Home','Home','Home','Home'], inplace=True)
#print(IrelandDF['Location'].value_counts())

###########################################################################
#Away = IrelandDF.drop_duplicates(subset='Home')
#print(IrelandDF.head(10))
#x = IrelandDF[["Location"]] != IrelandDF[['Home']]
#print(x)
#Away = IrelandDF['Location'].replace([],['Away'], inplace=True)
#####################################################################################################

missing_values = IrelandDF.isnull().sum()   # Checking if there are any missing values and if there are, how many
#print(missing_values)
# There are no null values in the data, but if there was I could delete the rows using IrelandDF.dropna() or columns using IrelandDF.dropna(axis=1)
# Or I could fill the values using IrelandDF.fillna()



















# MANIPULATING THE DATA TO SUIT MY GOALS

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

############################################################################################
# Adding a column
# This isn't complete, can be deleted
#Over_Performed = IrelandDF['Opposition Rating'] > IrelandDF['Rating']
#print(Over_Performed)
#IrelandDF['Won vs higher rated team'] = [Games_Won & Over_Performed]
#print(IrelandDF.head(10))

# For a simple demonstration of adding a column:
IrelandDF['Difference in Rating'] = IrelandDF['Rating'] - IrelandDF['Opposition Rating']
#print(IrelandDF)
###############################################################################################








# Filtering Wins/Losses/Ties
Games_Won = (IrelandDF[IrelandDF['Result'] > 0])    # This filters the dataframe to show only records where Ireland won a game
Games_Lost = (IrelandDF[IrelandDF['Result'] < 0])   # This filters to show records where Ireland lost
Games_Tied = (IrelandDF[IrelandDF['Result'] == 0])  # This filters to show records where Ireland tied
#print(Games_Won)
#print(Games_Lost)
#print(Games_Tied)

# Creating a DataFrame showing Home Game results
Home_GamesDF = IrelandDF[IrelandDF['Location'] == 'Home']
#print(Home_GamesDF)
#print((Home_GamesDF[['Result']] > 0).value_counts())    # Counting the number of Home Games Ireland Won
#print((Home_GamesDF[['Result']] < 0).value_counts())    # Counting the number of Home Games Ireland Lost
#print((Home_GamesDF[['Result']] == 0).value_counts())   # Counting the number of Home Games Ireland Tied

# Creating a DataFrame showing Away Game results
Away_GamesDF = IrelandDF[IrelandDF['Location'] != 'Home']
#print(Away_GamesDF)
#print((Away_GamesDF[['Result']] > 0).value_counts()) # Double square brackets to show a DF not a pandas series
#print((Away_GamesDF[['Result']] < 0).value_counts())
#print((Away_GamesDF[['Result']] == 0).value_counts())

# DataFrame for Home Victories
Home_Games_Won = IrelandDF[(IrelandDF['Result'] > 0) & (IrelandDF['Location'] == 'Home')]
Home_Wins_Number = Home_Games_Won['Result'].count()
#print(Home_Games_Won.head())
print(Home_Wins_Number)

# DF for Home Defeats
Home_Games_Lost = IrelandDF[(IrelandDF['Result'] < 0) & (IrelandDF['Location'] == 'Home')]
Home_Loss_Number = Home_Games_Lost['Result'].count()
#print(Home_Games_Lost.head())
print(Home_Loss_Number)

# DF for Home Games Tied
Home_Games_Tied = IrelandDF[(IrelandDF['Result'] == 0) & (IrelandDF['Location'] == 'Home')]
Home_Tied_Number = Home_Games_Tied['Result'].count()
#print(Home_Games_Tied)
print(Home_Tied_Number)
################################################################################################



########################################################### HAVE A LOOK AT THIS AVENUE AGAIN
#Sum = IrelandDF['Opposition Name'].value_counts().sum()
#print(Sum)


#grouped = IrelandDF.groupby('Location')['Rating']
#print(grouped)














# VISUALIZING THE DATA

# Home Results Bar CHart
x = ['Win', 'Loss', 'Tie']
y = [Home_Wins_Number, Home_Loss_Number, Home_Tied_Number]
#plt.bar(x, y, color=['green','red','blue'])
#plt.title('Home Game Results')
#plt.legend(('Win','Loss'), loc='upper right')
#plt.show()

#fig, ax = plt.subplots()
#ax.bar(x, y, label='Green', color=['green','red','blue'])
#ax.set_title('Title')
#ax.set_xlabel('XLABEL')
#ax.set_ylabel('YLABEL')
#ax.legend()
#ax.set_xticklabels(x, rotation=0)
#plt.show()








# Ireland's Rating Over Time. Needs xaxis labels fixed
#fig, ax = plt.subplots(figsize=(10,6))
#ax.plot(IrelandDF.index, IrelandDF['Rating'], color='green', marker='.') # If I wished to change linestyle: linestyle='-.'
#ax.set_title('Irelands World Rugby Rating 2003 - 2018')
#ax.set_xlabel('Time')
#ax.set_ylabel('World Rugby Team Rating')
#ax.set_xticks(ax.get_xticks()[::10])
##ax.xaxis.set_ticks(np.arrange(xmin, xmax, stepsize))
##ax.set_xticks([])
##ax.set_xticklabels(IrelandDF.index, rotation=45)
##ax.xaxis.set_major_locator(plt.MaxNLocator(100))
#ax.tick_params('y', colors='red')
#ax.grid(True)
#plt.show()

# Box Plot
#figb, axb = plt.subplots()
#axb.boxplot(IrelandDF['Rating'])
#axb.set_title('Ratings Condensed')
#axb.set_xlabel('Ireland')
#axb.set_ylabel('World Rugby Ratings')
#axb.grid(True)
#plt.show()

#Mean_Rating = IrelandDF['Rating'].mean()
#print(Mean_Rating)
#print(IrelandDF['Result'])



#fig, ax = plt.subplots()
#ax.hist(IrelandDF.index, IrelandDF['Rating'])
#ax.set_xticklabels(IrelandDF.index, rotation=90)
#ax.set_ylabel('Ratings')
#plt.show()

#Sample Simple Plot
#IrelandDF['Rating'].plot(kind='line')
#plt.show()








#plt.hist(IrelandDF['Rating'],bins=10)
#plt.show()

#plt.hist(Home_Wins_Number, bins=1)
#plt.show()

#plt.bar('Home',Home_Loss_Number)
#plt.show()

#print(IrelandDF.head())
#IreLocation = IrelandDF[['Location']]
#print(IreLocation)
#IreHome
#print(IrelandDF[['Result']])


#fig1, ax1 = plt.subplots()
#for country in IrelandDF:
#    CountryDF = IrelandDF[IrelandDF['Opposition Name'] == country]
#    ax1.bar(country, CountryDF['Result'] > 0)
#ax1.set_ylabel('ABC')
#ax1.set_xticklabels(country, rotation=90)
#plt.show()

