# Subsetting Pivot Tables

# A pivot table is just a DataFrame with sorted indexes, so the techniques learned previous can be used to
# subset them. In particular, the .loc[] + slicing combination is often helpful.

# assume temp_by_country_city_vs_year is loaded from prev file
import pandas as pd

# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India','Delhi')]

# Subset in both directions at once, From Egypt, Cairo to India, Delhi, and 2005 to 2010.
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010']