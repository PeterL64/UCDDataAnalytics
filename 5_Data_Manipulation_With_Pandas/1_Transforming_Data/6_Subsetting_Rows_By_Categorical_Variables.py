# Subsetting rows by categorical variables

# Subsetting data based on a categorical variable often involves using the "or" operator (|) to select rows
# from multiple categories. This can get tedious when you want all states in one of three different
# regions, for example. Instead, use the .isin() method, which will allow you to tackle this problem
# by writing one condition instead of three separate ones (Shown Below)
# Sample Code:
# colors = ["brown", "black", "tan"]
# condition = dogs["color"].isin(colors)
# dogs[condition]

# Filter homelessness for cases where the USA census region is "South Atlantic" or
# it is "Mid-Atlantic", assigning to south_mid_atlantic
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# Print the result
print(south_mid_atlantic)


# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter homelessness for cases where the USA census state is in the list of
# Mojave states, canu, assigning to mojave_homelessness
# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)