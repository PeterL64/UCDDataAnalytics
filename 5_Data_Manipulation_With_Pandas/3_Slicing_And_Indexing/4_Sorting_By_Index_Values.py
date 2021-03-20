# Sorting By Index Values



# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the 'city' level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by ascending country then descending city
print(temperatures_ind.sort_index(level=['country', 'city'], ascending=[True, False]))