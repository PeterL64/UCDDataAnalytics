# Concatenating With Keys

# Concatenate the three tables together vertically in order with the oldest month first,
# adding '7Jul', '8Aug', and '9Sep' as keys for their respective months, and save
# to variable avg_inv_by_month.
inv_jul_thr_sep = pd.concat([inv_jul,inv_aug,inv_sep], keys=['7Jul','8Aug','9Sep'])

# Use the .agg() method to find the average of the total column from the grouped invoices.
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Create a bar chart of avg_inv_by_month.
avg_inv_by_month.plot(kind='bar')
plt.show()