# Dictionary of lists

# date	        small_sold	large_sold
# "2019-11-17"	10859987	7674135
# "2019-12-01"	9291631	    6238096

import pandas as pd

# Create a dictionary of lists with the new data called avocados_dict.
avocados_dict = {'date': ['2019-11-17','2019-12-01'],"small_sold": [10859987, 9291631],"large_sold": [7674135, 6238096]}

# Convert the dictionary to a DataFrame called avocados_2019.
avocados_2019 = pd.DataFrame(avocados_dict)

# Print DataFrame
print(avocados_2019)