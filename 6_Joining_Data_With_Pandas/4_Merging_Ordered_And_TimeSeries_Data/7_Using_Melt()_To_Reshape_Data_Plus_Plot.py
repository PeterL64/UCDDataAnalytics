# Using .melt() to reshape data

# Use .melt() to unpivot all of the columns of ur_wide except year and ensure that
# the columns with the months and values are named month and unempl_rate, respectively.
# Save the result as ur_tall.
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')

# Add a column to ur_tall named date which combines the year and month columns as year-month format
# into a larger string, and converts it to a date data type.
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])

# Sort ur_tall by date and save as ur_sorted.
ur_sorted = ur_tall.sort_values('date')

# Using ur_sorted, plot unempl_rate on the y-axis and date on the x-axis.
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()