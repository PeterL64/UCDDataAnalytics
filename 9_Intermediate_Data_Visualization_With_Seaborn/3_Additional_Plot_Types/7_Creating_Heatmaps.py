# Creating Heatmaps

# Seaborn's heatmap() function requires data to be in a grid format.
# pandas crosstab() is frequently used to manipulate the data.

pd.crosstab(df['Month'], df['Weekday'], values=df['Total_Rentals'], aggfunc='mean').round(0)
# This code creates a table/grid out of your data.

sns.heatmap(pd.crosstab(df['Month'], df['Weekday'], values=df['Total_Rentals'], aggfunc='mean'))
# This creates a heatmap out of the above grid.


# Use pandas' crosstab() function to build a table of visits by Group and Year.
# Print the pd_crosstab DataFrame.
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
print(pd_crosstab)

# Plot the data using Seaborn's heatmap().
sns.heatmap(pd_crosstab)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()


# For reference:
# print(pd_crosstab)
# YEAR            1999  2000  2001  2002  2003  2004  2005  2006  2007  2008  2009  2010  2011  2012  2013  2014  2015
#     Group
#     Academic           0     0     2     0     4     1    12     9    13     5    11     8    10     8     8    10     2
#     Acting           108   100    92    84    74    51    44    44    25    26    22    45    42    33    60    47    33
#     Advocacy           0     1     0     1     0     4     0     0     2     3     1     1     1     2     2     3     3
#     Athletics          0     3     1     2     0     2     2     5     4     1     7     5     2     7     4     4     3
#     Business           0     1     0     0     0     2     1     1     2     1     4     2     3     3     3     1     1
#     Clergy             0     0     0     1     1     1     0     0     1     0     1     0     1     2     0     0     0
#     Comedy            25    12    11     5    12     7     5     8     9     7     7     7     7     6     6     9     7
#     Consultant         0     0     0     0     1     4     1     4     2     3     2     1     0     0     0     0     0
#     Government         0     0     2     1     2     3     1     3     1     0     5     3     3     3     7     6     0
#     Media             11    21    31    42    41    45    54    47    47    77    59    50    51    52    51    53    24
#     Military           0     0     0     0     0     0     1     1     3     1     1     2     3     1     1     1     1
#     Misc               0     0     2     1     1     0     4     3     2     2     5     4     5     6     2     5     3
#     Musician          17    13    11    10     7     5    11     6     2     1     5     6     6     5     5     8     5
#     Political Aide     0     1     1     2     1     2     3     3     2     6     3     2     1     1     3     2     3
#     Politician         2    13     3     8    14    32    22    25    21    27    26    25    23    29    11    13    14
#     Science            0     0     0     0     1     2     1     1     4     1     4     3     5     2     2     1     1