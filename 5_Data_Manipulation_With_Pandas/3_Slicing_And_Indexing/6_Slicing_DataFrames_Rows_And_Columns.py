# Slicing a Dataframe in both directions, Rows and Columns using .loc[]




import pandas as pd

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,'date':'avg_temp_c'])

# Subset in both directions at once from Hyderabad to Baghdad
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'),'date':'avg_temp_c'])

# The city names in this DataFrame are the Inner Indexes, so the syntax must include the Outer Index
# DataFrams.loc[('OuterIndex','InnerIndex):('Outer','Inner'),'ColumnName':'ColumnName']