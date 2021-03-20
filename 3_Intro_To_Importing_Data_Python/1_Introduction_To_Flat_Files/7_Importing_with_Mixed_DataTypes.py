# Importing with Mixed Data Types 2

# Similar to the np.genfromtxt() function there is another function, np.recfromcsv() for CSV files.
# np.recfromcsv has some defaults, so you do not need to enter them. dtype=None, delimiter=',' and names=True

# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv and assign it the variable: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])
