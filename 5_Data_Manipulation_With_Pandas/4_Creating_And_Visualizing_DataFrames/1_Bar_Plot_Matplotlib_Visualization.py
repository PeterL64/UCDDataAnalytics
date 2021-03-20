# DataFrame Visualization with matplotlib.pyplot - Bar Chart

# Will use a sample DataFrame of Avocado Sales
# Bar plots are great for revealing relationships between categorical (size) and numeric (number sold)
# variables, but you'll often have to manipulate your data first in order to get the numbers
# you need for plotting.

# Import matplotlib.pyplot and pandas
import matplotlib.pyplot as plt
import pandas as pd

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar')

# Show the plot
plt.show()


# avocados.head()
#           date          type  year  avg_price   size    nb_sold
#     0  2015-12-27  conventional  2015       0.95  small  9.627e+06
#     1  2015-12-20  conventional  2015       0.98  small  8.710e+06
#     2  2015-12-13  conventional  2015       0.93  small  9.855e+06
#     3  2015-12-06  conventional  2015       0.89  small  9.405e+06
#     4  2015-11-29  conventional  2015       0.99  small  8.095e+06