# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[dr]
# Code in the two lines above can be written as:
sel = cars[cars['drives_right']]

# Print sel
print(sel)