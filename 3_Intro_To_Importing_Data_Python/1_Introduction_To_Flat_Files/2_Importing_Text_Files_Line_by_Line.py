# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Line 1: Here is a context manager, where I binded the variable 'file' to the code open('moby_dick.txt')
# Line 1: This means I can use the Method readline() to print the text line by line.

