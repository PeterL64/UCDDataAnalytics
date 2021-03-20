# Import pickle package
import pickle

# Open pickle file and load data to variable: d
with open('data.pkl', 'rb') as file:    # The second argument of open() is a string rb, the r means read-only and
    d = pickle.load(file)               # the b means binary

# Print d
print(d)

# Print datatype of d
print(type(d))