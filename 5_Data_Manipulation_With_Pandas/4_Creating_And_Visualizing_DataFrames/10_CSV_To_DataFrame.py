# CSV to DataFrame

import pandas as pd

# Read the CSV file "airline_bumping.csv" and store it as a DataFrame called airline_bumping.
airline_bumping = pd.read_csv('airline_bumping.csv')

# Take a look at the DataFrame
print(airline_bumping.head())

#                airline  year  nb_bumped  total_passengers
#     0    DELTA AIR LINES  2017        679          99796155
#     1     VIRGIN AMERICA  2017        165           6090029
#     2    JETBLUE AIRWAYS  2017       1475          27255038
#     3    UNITED AIRLINES  2017       2067          70030765
#     4  HAWAIIAN AIRLINES  2017         92           8422734

# For each airline group, select the nb_bumped, and total_passengers columns, and
# calculate the sum (for both years). Store this as airline_totals.
# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby('airline')[['nb_bumped','total_passengers']].sum()

# Create a new column of airline_totals called bumps_per_10k, which is the number of
# passengers bumped per 10,000 passengers in 2016 and 2017.
# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals['nb_bumped'] / airline_totals['total_passengers'] * 10000

print(airline_totals)

#                      nb_bumped  total_passengers  bumps_per_10k
# airline
# ALASKA AIRLINES           1392          36543121          0.381
# AMERICAN AIRLINES        11115         197365225          0.563
# DELTA AIR LINES           1591         197033215          0.081
# EXPRESSJET AIRLINES       3326          27858678          1.194
# FRONTIER AIRLINES         1228          22954995          0.535
# HAWAIIAN AIRLINES          122          16577572          0.074
# JETBLUE AIRWAYS           3615          53245866          0.679
# SKYWEST AIRLINES          3094          47091737          0.657
# SOUTHWEST AIRLINES       18585         228142036          0.815
# SPIRIT AIRLINES           2920          32304571          0.904
# UNITED AIRLINES           4941         134468897          0.367
# VIRGIN AMERICA             242          12017967          0.201