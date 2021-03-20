# Importing with mixed Data Types


# Sample code importing a file of passengers of the Titanic, showing Passenger ID, Survived, Class, Sex, Age, etc.

# The Numpy function, np.genfromtxt() is used here to handle the many different data types
# Pass dtype = None to the function above and it will figure out what types each column should be.
# The argument Names tells it there is a header
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
