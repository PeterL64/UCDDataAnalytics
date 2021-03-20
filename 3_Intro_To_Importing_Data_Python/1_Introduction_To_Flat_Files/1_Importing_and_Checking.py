# Open a file: file
file = open('moby_dick.txt', mode = 'r')    # Opening a txt file in read-only mode and storing it in variable 'file'

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
