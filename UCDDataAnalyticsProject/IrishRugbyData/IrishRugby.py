# Analysing Ireland Rugby match to compare Home vs Away results.

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
IrelandDF = pd.read_csv(file, index_col = 1) # Importing in Pandas DataFrame rather than a Numpy array because there is multiple data types involved
# I set the index as the date column because the values should be all unique
# Alternatively loading file directly from file location below:
# IrelandDF = pd.read_csv(r"C:\Users\peter\Desktop\UCD Data Analytics\Project\Ireland Rugby\IREMatchData(FULL).csv")


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

#######################################################################################################################
#######################################################################################################################
#Away = IrelandDF['Location'].drop_duplicates(subset='Home')
#print(IrelandDF.head(10))
#print(Away)
#Away1 = IrelandDF["Location"] != IrelandDF['Home']
#print(Away1)
#Away = IrelandDF['Location'].replace([],['Away'], inplace=True) # Not practical to write out every value for this code
#######################################################################################################################
#######################################################################################################################

missing_values = IrelandDF.isnull().sum()   # Checking if there are any missing values and if there are, how many
#print(missing_values)
# There are no null values in the data, but if there was I could delete the rows using IrelandDF.dropna() or columns using IrelandDF.dropna(axis=1)
# Or I could fill the values using IrelandDF.fillna()



#######################################################################################################################
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
#print(Toughest_Opponents) # This shows the opposition Ireland played against with the highest rating at the top of the DataFrame


# Adding a column
# For a simple demonstration of adding a column:
IrelandDF['Difference in Rating'] = IrelandDF['Rating'] - IrelandDF['Opposition Rating']
#print(IrelandDF)



######################################################################################################
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
# Tried to complete above line like this but created an error: HGW = Games_Won & Home_GamesDF
Home_Wins_Number = Home_Games_Won['Result'].count()
#print(Home_Games_Won.head())
#print(Home_Wins_Number)

# DF for Home Defeats
Home_Games_Lost = IrelandDF[(IrelandDF['Result'] < 0) & (IrelandDF['Location'] == 'Home')]
Home_Loss_Number = Home_Games_Lost['Result'].count()
#print(Home_Games_Lost.head())
#print(Home_Loss_Number)

# DF for Home Games Tied
Home_Games_Tied = IrelandDF[(IrelandDF['Result'] == 0) & (IrelandDF['Location'] == 'Home')]
Home_Tied_Number = Home_Games_Tied['Result'].count()
#print(Home_Games_Tied)
#print(Home_Tied_Number)


# DataFrame for Away Victories
Away_Games_Won = IrelandDF[(IrelandDF['Result'] > 0) & (IrelandDF['Location'] != 'Home')]
Away_Wins_Number = Away_Games_Won['Result'].count()
#print(Away_Games_Won.head())
#print(Away_Wins_Number)

# DF for Away Defeats
Away_Games_Lost = IrelandDF[(IrelandDF['Result'] < 0) & (IrelandDF['Location'] != 'Home')]
Away_Loss_Number = Away_Games_Lost['Result'].count()
#print(Away_Games_Lost.head())
#print(Away_Loss_Number)

# DF for Away Games Tied
Away_Games_Tied = IrelandDF[(IrelandDF['Result'] == 0) & (IrelandDF['Location'] != 'Home')]
Away_Tied_Number = Away_Games_Tied['Result'].count()
#print(Away_Games_Tied)
#print(Away_Tied_Number)
#####################################################################################################

# Merge two DataFrames
















##########################################################################################
# VISUALIZING THE DATA

x1 = ['Win', 'Loss', 'Tie']
y1 = [Home_Wins_Number, Home_Loss_Number, Home_Tied_Number]
y2 = [Away_Wins_Number, Away_Loss_Number, Away_Tied_Number]

# Home and Away Results Chart
plt.style.use('ggplot')
fig, ax = plt.subplots(2,1, sharey=True, figsize=(8,7))
ax[0].bar(x1, y1, color=['green','red','blue'])
ax[0].set_title('Irish Rugby Home Results 2003 - 2018')
ax[0].set_ylabel('Number of Win/Loss/Tie')
#ax[0].legend(['Win','Loss','Tie']) # Could not get the legend to cooperate
ax[0].grid(True, which='minor', axis='y')
ax[1].bar(x1, y2, label='Green', color=['green','red','blue'])
ax[1].set_title('Irish Rugby Away Results: 2003 - 2018')
ax[1].set_ylabel('Number of Win/Loss/Tie')
ax[1].grid(True, which='major', axis='y')
fig.savefig("Home_Vs_Away_Results.png")
plt.show()

# Ireland's Rating Over Time. Needs xaxis labels fixed
figa, axa = plt.subplots(figsize=(10,6))
axa.plot(IrelandDF.index, IrelandDF['Rating'], color='green', marker='.') # If I wished to change linestyle: linestyle='-.'
axa.set_title('Irelands World Rugby Rating 2003 - 2018')
axa.set_xlabel('Time')
axa.set_ylabel('World Rugby Team Rating')
axa.set_xticklabels(IrelandDF.index, rotation=90)
#axa.set_xticks(ax.get_xticks()[::10])
#axa.xaxis.set_ticks(np.arrange('2003-10-19','2018-11-24','10')
#axa.xaxis.set_major_locator(plt.MaxNLocator(50))
axa.tick_params('y', colors='red')
axa.grid(True)
figa.savefig("Ratings_Over_Time.png")
plt.show()

# Box Plot
figb, axb = plt.subplots()
axb.boxplot(IrelandDF['Rating'])
axb.set_title('Ratings Condensed')
axb.set_xlabel('Ireland')
axb.set_ylabel('World Rugby Ratings')
axb.grid(True)
figb.savefig("Ratings_Box_Plot.png")
plt.show()









# Home Results Simple Bar Chart
#plt.bar(x1, y1, color=['green','red','blue'])
#plt.title('Home Game Results')
#plt.legend(('Win','Loss'), loc='upper right')
#plt.show()

# Home Results Sample
#fig1, ax1 = plt.subplots()
#ax1.bar(x1, y1, label='Green', color=['green','red','blue'])
#ax1.set_title('Home Results')
#ax1.set_xlabel('Win/Loss/Tie')
#ax1.set_ylabel('Number of Win/Loss/Tie')
#ax1.legend()
#plt.style.use('tableau-colorblind10')
#plt.show()

# Away Results Sample
#fig2, ax2 = plt.subplots()
#ax2.bar(x1, y2, label='Green', color=['green','red','blue'])
#ax2.set_title('Away Results')
#ax2.set_xlabel('Win/Loss/Tie')
#ax2.set_ylabel('Number of Win/Loss/Tie')
#plt.style.use('ggplot')
#ax2.legend()
#plt.show()









#######################################################################################################################
# Miscellaneous code

# for loop
#fig1, ax1 = plt.subplots()
#for country in IrelandDF:
#    CountryDF = IrelandDF[IrelandDF['Opposition Name'] == country]
#    ax1.bar(country, CountryDF['Result'] > 0)
#ax1.set_ylabel('ABC')
#ax1.set_xticklabels(country, rotation=90)
#plt.show()