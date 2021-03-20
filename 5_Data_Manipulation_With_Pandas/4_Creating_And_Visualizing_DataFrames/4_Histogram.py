# Using Histograms to show the price of conventional vs organic avocados
# In the avocados DataFrame the type column has 2 different strings of data, 'conventional' and 'organic'.

import pandas as pd
import matplotlib.pyplot as plt

# Subset avocados for the conventional type, and the average price column. Create a histogram.
# Histogram of conventional avg_price
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Create a histogram of avg_price for organic type avocados.
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend to your plot, with the names "conventional" and "organic".
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

# Modify the code above to adjust the Transparency of both Histograms to 0.5, and to have 20 bins
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)