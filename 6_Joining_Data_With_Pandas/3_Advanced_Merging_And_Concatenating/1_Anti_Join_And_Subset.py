# Anti Join

# Merge employeesn(table) and top_cust(table) with a left join, setting indicator argument to True.
# Save the result to empl_cust.
empl_cust = employees.merge(top_cust, on='srid', how='left', indicator=True)

# Select the srid column of empl_cust and the rows where _merge is 'left_only'. Save the result to srid_list.
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Subset the employees table and select those rows where the srid is in
# the variable srid_list and print the results.
print(employees[employees['srid'].isin(srid_list)])