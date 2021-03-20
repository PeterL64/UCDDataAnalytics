# Using pd.merge_ordered() and .plot() to plot a Philips curve of unemployment and inflation.


# Use merge_ordered() to merge the inflation and unemployment tables on date
# with an inner join, and save the results as inflation_unemploy.
inflation_unemploy = pd.merge_ordered(inflation,unemployment, on='date', how='inner')

# Print the inflation_unemploy variable.
print(inflation_unemploy)

# Using inflation_unemploy, create a scatter plot with unemployment_rate on the horizontal axis
# and cpi (inflation) on the vertical axis.
inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
plt.show()