# Using a lmplot (LM Plot)

# The lmplot is used to plot scatter plots with regression lines on FacetGrid objects.
# The API is similar to factorplot with the difference that the default behavior of lmplot is to plot regression lines.

# Create a FacetGrid() with Degree_Type columns and scatter plot of UG and PCTPELL.
# Create a FacetGrid varying by column and columns ordered with the degree_order variable
g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)

# Map a scatter plot of Undergrad Population compared to PCTPELL
g.map(plt.scatter, 'UG', 'PCTPELL')

plt.show()
plt.clf()

# Create a lmplot() using the same values from the FacetGrid().
sns.lmplot(data=df, x='UG', y='PCTPELL', col="Degree_Type", col_order=degree_ord)

plt.show()
plt.clf()

# Create a facetted lmplot() comparing SAT_AVG_ALL to Tuition with columns varying by Ownership and rows by Degree_Type.
# In the lmplot() add a hue for Women Only Universities.
sns.lmplot(data=df, x='SAT_AVG_ALL', y='Tuition', col="Ownership", row='Degree_Type',
        row_order=['Graduate', 'Bachelors'], hue='WOMENONLY', col_order=inst_ord)

plt.show()
plt.clf()
