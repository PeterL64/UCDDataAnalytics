# Multiple grouped summaries

# .agg() method works well on multiple variables (as in prev file). It also works with Grouped Data.
# .agg() can take in a list of functions. The functions won't "be called", so no need to use parenthesis
# Syntax for code:   sales.groupby.agg()


# Numpy has many different summary statistics functions; np.min, np.max, np.mean, np.median
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])
# Parenthesis and brackets are very important. See .agg() uses [] for a LIST of functions inside it's ()

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])
# Here the .groupby() method is using a list of columns, so you use double square brackets [['LIST']]

# Print unemp_fuel_stats
print(unemp_fuel_stats)


