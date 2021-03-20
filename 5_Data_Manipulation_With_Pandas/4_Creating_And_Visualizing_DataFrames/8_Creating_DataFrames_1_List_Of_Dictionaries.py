# Creating a DataFrame Using a List of dictionaries
# A DataFrame created using a list of dictionaries, the DataFrame is built up row by row,
# (as opposed to column by column as in a dictionary of lists)


# You recently got some new avocado data from 2019 that you'd like to put in
# a DataFrame using the list of dictionaries method.


# date	        small_sold	large_sold
# "2019-11-03"	10376832	7835071
# "2019-11-10"	10717154	8561348


import pandas as pd

# Create a list of dictionaries with new data
avocados_list = [{'date': '2019-11-03', 'small_sold': 10376832, 'large_sold': 7835071},
                 {'date': '2019-11-10', 'small_sold': 10717154, 'large_sold': 8561348}]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)
