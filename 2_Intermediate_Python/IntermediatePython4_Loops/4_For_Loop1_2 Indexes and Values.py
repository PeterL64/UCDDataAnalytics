# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# for loop which prints the index and list element using enumerate()
for index, a in enumerate(areas):
    print('room ' + str(index) + ': ' + str(a))  # \n prints an empty line after.
print('\n')     # Three print statements here are to print empty lines.
print('')       # I write these as often as I can to help remember them
print("")

# Updating code above so it is more intuitive to read for non-coders
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas):
    index1 = index + 1
    print("room " + str(index1) + ": " + str(area))
