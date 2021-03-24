import pandas as pd

netflix_data=pd.read_csv("netflix_titles.csv")

print(netflix_data.head(), netflix_data.shape())

missing_val=netflix_data.isnull().sum()   # isnull tells you how many cells are empty. says false if the value is not null and true if it is null
# .sum() calculates the total on each column and gives the total missing values

print(missing_val)
