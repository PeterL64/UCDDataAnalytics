# Using merge_asof() to study stocks

# Use merge_asof() to merge jpm (left table) and wells together on the date_time column,
# where the rows with the nearest times are matched, and with suffixes=('', '_wells').
# Save to jpm_wells.
jpm_wells = pd.merge_asof(jpm, wells, on='date_time',
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells (left table) and bac together on the date_time column,
# where the rows with the closest times are matched, and with suffixes=('_jpm', '_bac').
# Save to jpm_wells_bac.
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', suffixes=('_jpm', '_bac'), direction='nearest')

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Using price_diffs, create a line plot of the close price of JPM, WFC, and BAC only.
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()