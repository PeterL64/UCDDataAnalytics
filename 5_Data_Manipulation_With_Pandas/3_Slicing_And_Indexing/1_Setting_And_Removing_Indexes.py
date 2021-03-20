# Setting and removing indexes

# Working with a sample dataframe named temperatures (Below code) which has columns:
# date, city, country, avg_temp_c

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))


# temperatures (sample dataframe)

#             date     city        country  avg_temp_c
# 0     2000-01-01  Abidjan  Côte D'Ivoire      27.293
# 1     2000-02-01  Abidjan  Côte D'Ivoire      27.685
# 2     2000-03-01  Abidjan  Côte D'Ivoire      29.061
# 3     2000-04-01  Abidjan  Côte D'Ivoire      28.162
# 4     2000-05-01  Abidjan  Côte D'Ivoire      27.547
# ...          ...      ...            ...         ...
# 16495 2013-05-01     Xian          China      18.979
# 16496 2013-06-01     Xian          China      23.522
# 16497 2013-07-01     Xian          China      25.251
# 16498 2013-08-01     Xian          China      24.528
# 16499 2013-09-01     Xian          China         NaN