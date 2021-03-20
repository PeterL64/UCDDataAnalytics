# Replacing Missing Values

# A list has been created, cols_with_missing, containing the names of columns
# with missing values: "small_sold", "large_sold", and "xl_sold".
# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()


# Replace the missing values of avocados_2016 with 0s and store the result as avocados_filled.
# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create a histogram of the cols_with_missing columns of avocados_filled.
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()