# Using merge_asof() to create dataset

# Using merge_asof(), merge gdp and recession on date, with gdp as the left table.
# Save to the variable gdp_recession.
gdp_recession = pd.merge_asof(gdp, recession, on='date', direction='backward')

# Create a list using a list comprehension and a conditional expression, named is_recession,
# where for each row if the gdp_recession['econ_status'] value is equal to 'recession' then
# enter 'r' else 'g'.
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Using gdp_recession, plot a bar chart of gdp versus date, setting the
# color argument equal to is_recession.
gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
plt.show()
