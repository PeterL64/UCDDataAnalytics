# Subsetting Rows with .query()

# Use merge_ordered() on gdp and pop on columns country and date with the fill feature,
# save to gdp_pop and print.
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')
print(gdp_pop)

# Add a column named gdp_per_capita to gdp_pop that divides gdp by pop.
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot gdp_pop so values='gdp_per_capita', index='date', and columns='country', save as gdp_pivot.
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Use .query() to select rows from gdp_pivot where date is greater than equal to 1991-01-01".
# Save as recent_gdp_pop.
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()