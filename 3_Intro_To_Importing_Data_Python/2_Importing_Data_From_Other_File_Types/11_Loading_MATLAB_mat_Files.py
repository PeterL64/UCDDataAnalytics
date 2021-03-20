# How to load MATLAB Files using the scipy.io package
#
# Import package
import scipy.io

# Load MATLAB file and store in variable: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')
# scipy.io.loadmat() is a function from the scipy.io package for loading MATLAB files

# Print the datatype type of mat
print(type(mat))
